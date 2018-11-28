// FlySwatter.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
//#include <string.h>
#include <math.h>
#pragma warning(disable : 4996)

double SQR(double x) {return x*x;}
bool PointWithinRadius (double x, double y, double r) {
	return SQR(x) + SQR(y) <= SQR(r);
}
double PI = 3.14159265358979;

double AreaTrapezoidApprox(double x0, double x1, double r) {
	if (r < x1)
		x1 = r;
	double y0 = sqrt(SQR(r)-SQR(x0)),
		y1 = sqrt(SQR(r)-SQR(x1)),
		deltaX = x1-x0;
	return ((y0 + y1)/2.0f) * deltaX;
}

double AreaUnderCurve(double x0, double x1, double r) {
	// Multiple trapezoid approximation.
	const int numIters = 1000;
	double toReturn=0, deltaX = (x1-x0)/numIters;
	for (int i=0; i<numIters; ++i) {
		double rightBound = x0 + deltaX;
		if (rightBound > x1)
			rightBound = x1;
		if (rightBound > r)
			rightBound = r;
		if (x0 >= rightBound || x0 >= r)
			break;
		toReturn += AreaTrapezoidApprox(x0, rightBound, r);
		x0 += deltaX;
	}
	return toReturn;
}

double AreaInRadius(double x0, double y0, double x1, double y1, double r) {
	if (x0 > x1 || y0 > y1)
		return 0.0f;
	if (PointWithinRadius(x1, y1, r))
		return (x1 - x0) * (y1 - y0);
	if (!PointWithinRadius(x0, y0, r))
		return 0.0f;
	double toReturn = 0;
	if (PointWithinRadius(x0, y1, r)) {
		// Move up x0.
		double x2 = sqrt(SQR(r)-SQR(y1));
		toReturn += (x2 - x0) * (y1 - y0);
		x0 = x2;
	}
	if (!PointWithinRadius(x1, y0, r)) {
		// Move back x1.
		x1 = sqrt(SQR(r)-SQR(y0));
	}
	if (x0 > x1 || y0 > y1)
		return 0;
	// Get the area under the curve.
	toReturn += AreaUnderCurve(x0, x1, r) - (x1-x0)*y0;
	return toReturn;
}

void ProcessCase(FILE *instream, FILE *outstream, int caseNum, int totalCases) {
	printf("Processing %d out of %d\n", caseNum, totalCases);
	float f, R, t, r, g;
	fscanf(instream, "%f %f %f %f %f ", &f, &R, &t, &r, &g);
	double missArea=0, totalArea = 0;
	for (double x0=0; x0<R; x0+=g+2*r) {
		for (double y0=0; y0<R; y0+=g+2*r) {
			missArea += AreaInRadius(x0+r+f, y0+r+f, x0+r+g-f, y0+r+g-f, R-t-f);
			totalArea += AreaInRadius(x0, y0, x0+g+2*r, y0+g+2*r, R);
		}
	}
	// totalArea = PI * SQR(R) / 4.0f;
	float probability = (float)((totalArea - missArea) / totalArea);
	fprintf(outstream, "Case #%d: %f\n", caseNum, probability);
}

int main(int argc, char* argv[])
{
	if (argc < 3)
		return 1;
	FILE *inStream = fopen(argv[1], "r");
	if (!inStream)
		return 1;

	FILE *outStream = fopen(argv[2], "w");
	if (!outStream)
		return 1;

	int numCases;
	fscanf(inStream, "%d ", &numCases);
	for (int i=0; i<numCases; ++i)
		ProcessCase(inStream, outStream, i+1, numCases);

	fclose(inStream);
	fclose(outStream);

	return 0;
}
