from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import mlflow
import os

# Initialize FastAPI app
app = FastAPI(
    title="Enterprise AI Model Serving",
    description="Production-grade API for AI and MLOps Engineer-driven systems.",
    version="1.0.0"
)

# Request schema
class PredictionRequest(BaseModel):
    features: list
    model_version: str = "v1"

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Enterprise AI / MLOps Engine is Live!"}

# Prediction endpoint
@app.post("/predict")
def predict(request: PredictionRequest):
    # Dummy logic to represent model inference
    if not request.features:
        raise HTTPException(status_code=400, detail="Features must not be empty.")
    
    # Log prediction to MLflow
    # with mlflow.start_run(run_name="Inference"):
    #     mlflow.log_param("model_version", request.model_version)
    
    prediction = sum(request.features) / len(request.features)
    return {
        "prediction": prediction,
        "model_version": request.model_version,
        "status": "success"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)