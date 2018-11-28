#include <iostream>
#include <fstream>

#include <cmath>

using namespace std;



int main()
{
	ifstream inputFile("input.txt");
	ofstream outputFile("output.txt");

	int T, X;

	int n;
	int thisX, thisY, thisZ, thisVX, thisVY, thisVZ;
	int sumX, sumY, sumZ, sumVX, sumVY, sumVZ;

	double cmX, cmY, cmZ;
	double allVX, allVY, allVZ;
	double minX, minY, minZ;

	double innerProdVel;

	double dMin, tMin;
	

	int i, j;

	inputFile>>T;
	outputFile.precision(8);
	outputFile<<showpoint<<fixed;
	for (X = 1; X <= T; ++X)
	{
		sumX = 0; sumY = 0; sumZ = 0;
		sumVX = 0; sumVY = 0; sumVZ = 0;
		inputFile>>n;
		for (i = 0; i < n; ++i)
		{
			inputFile>>thisX>>thisY>>thisZ>>thisVX>>thisVY>>thisVZ;
			sumX += thisX;  sumY += thisY;  sumZ += thisZ;
			sumVX += thisVX;  sumVY += thisVY;  sumVZ += thisVZ;
		}
		cmX = (double)sumX / (double)n;
		cmY = (double)sumY / (double)n;
		cmZ = (double)sumZ / (double)n;
		allVX = (double)sumVX / (double)n;
		allVY = (double)sumVY / (double)n;
		allVZ = (double)sumVZ / (double)n;
		
		innerProdVel = (allVX * -cmX) + (allVY * -cmY) + (allVZ * -cmZ);
		if (innerProdVel <= 0)
		{
			// Swarm goes to far
			tMin = 0.0;
			dMin = sqrt(cmX * cmX + cmY * cmY + cmZ * cmZ);
		}
		else
		{
			// Get nearest Pos
			tMin = innerProdVel / (allVX * allVX + allVY * allVY + allVZ * allVZ);
			minX = cmX + tMin * allVX;
			minY = cmY + tMin * allVY;
			minZ = cmZ + tMin * allVZ;
			dMin = sqrt(minX * minX + minY * minY + minZ * minZ);
		}
		outputFile<<"Case #"<<X<<": "<<dMin<<" "<<tMin<<endl;
	}

	inputFile.close();
	outputFile.close();
}
