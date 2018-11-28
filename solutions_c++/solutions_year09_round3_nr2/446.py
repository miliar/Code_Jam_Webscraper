#include <vector>
#include <fstream>
#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

typedef struct 
{
    int x;
    int y;
    int z;
    int dx;
    int dy;
    int dz;
}particle;

particle particles[500];

double calcDistAtTime(double t, int nParticles);

void calcDistTime(double& dOut, double& tOut, int nParticles)
{
    double delta = 5;
    double t = 10;
    double minValue = calcDistAtTime(t, nParticles);
    while(delta > 1e-10)
    {
        double rightValue = calcDistAtTime(t + delta, nParticles);
        if(rightValue < minValue)
        {
            minValue = rightValue;
            t = t + delta;
            continue;
        }

        double leftT = t - delta;
        if(leftT < 0)
            leftT = 0;
        double leftValue = calcDistAtTime(leftT, nParticles);
        if(leftValue <= minValue && leftT < t)
        {
            minValue = leftValue;
            t = leftT;
            continue;
        }

        delta /= 2.0;
    }

    tOut = t;
    dOut = minValue;
}

double calcDistAtTime(double t, int nParticles)
{
    double x = 0;
    double y = 0;
    double z = 0;
    for(int i = 0; i < nParticles; i++)
    {
        x += particles[i].x + t * particles[i].dx;
        y += particles[i].y + t * particles[i].dy;
        z += particles[i].z + t * particles[i].dz;
    }
    x /= (double)nParticles;
    y /= (double)nParticles;
    z /= (double)nParticles;
    return sqrt(x * x + y * y + z * z);
}

int main()
{
    ifstream myFile("problem2.txt");
    FILE* myAnswer;
    myAnswer = fopen("answer2.txt", "w");
    if (myFile.is_open())
    {
        int T;
        myFile >> T;
        string temp;
        getline(myFile, temp);
        
        for(int tc = 1; tc <= T; tc++)
        {
            string nextCase;
            getline(myFile, nextCase);
            int numOfParticles = atoi(nextCase.c_str());
            for(int i = 0; i < numOfParticles; i++)
            {
                string particleString;
                getline(myFile, particleString);
                stringstream str(particleString);
                str >> particles[i].x;
                str >> particles[i].y;
                str >> particles[i].z;
                str >> particles[i].dx;
                str >> particles[i].dy;
                str >> particles[i].dz;
            }
            double tOut;
            double dOut;
            calcDistTime(dOut, tOut, numOfParticles);
            fprintf(myAnswer, "Case #%d: %0.8f %0.8f\n", tc, dOut, tOut);
        }
    }
}