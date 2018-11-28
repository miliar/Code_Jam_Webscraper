#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <sstream>

using namespace std;

#define PROB_LETTER "C"
#define INTYPE "large"

#define SQR(x) ((x)*(x))

double chordArea(double chordLength, double circleRadius)
{ // done with mathematica: integral is sqrt(circleRadius^2 - x^2) * x + circleRadius^2 * sin^{-1}(x/circleRadius)
	double y = chordLength / 2;
	double x = sqrt(SQR(circleRadius) - SQR(y));

	return (M_PI*SQR(circleRadius)/2.0) - (sqrt(SQR(circleRadius) - SQR(x)) * x + SQR(circleRadius) * asin(x / circleRadius));
}

double findDistance(pair<double, double> p1, pair<double, double> p2)
{
	return sqrt(SQR(p1.first-p2.first) + SQR(p1.second-p2.second));
}

double openArea(double x, double y, double sideLength, double circleRadius)
{ // how much of the area of the square centered at (x,y) lies within circleRadius
	// WLOG, x and y are both positive
	x = fabs(x);
	y = fabs(y);
	
	// the square and the circle cross each other at 2 points (circle is monotonic at any square)
	if (x > y)
	{ // WLOG, x <= y
		double tmp = x;
		x = y;
		y = tmp;
	}

	double left = x-sideLength/2.0;
	double right = x+sideLength/2.0;
	double bottom = y-sideLength/2.0;
	double top = y+sideLength/2.0;

	if (SQR(right) + SQR(top) <= SQR(circleRadius))
		return SQR(sideLength);
	if (SQR(left) + SQR(bottom) >= SQR(circleRadius))
		return 0.0;

	bool leftSideIntersects = SQR(circleRadius)-SQR(left) <= SQR(top) * 1.001 &&
							SQR(circleRadius)-SQR(left) >= SQR(bottom) * .999;
	bool rightSideIntersects = SQR(circleRadius)-SQR(right) <= SQR(top) * 1.001 &&
							SQR(circleRadius)-SQR(right) >= SQR(bottom) * .999;
	bool topSideIntersects = SQR(circleRadius)-SQR(top) <= SQR(right) * 1.001 &&
							SQR(circleRadius)-SQR(top) >= SQR(left) * .999;
	bool bottomSideIntersects = SQR(circleRadius)-SQR(bottom) <= SQR(right) * 1.001 &&
							SQR(circleRadius)-SQR(bottom) >= SQR(left) * .999;

	double topLeftDistance = findDistance(make_pair(0.0, 0.0), make_pair(left, top));
	double bottomRightDistance = findDistance(make_pair(0.0, 0.0), make_pair(right, bottom));

	if (circleRadius < bottomRightDistance && circleRadius < topLeftDistance)
	{ // left and bottom intersect
		pair<double, double> leftPoint = make_pair(left, sqrt(SQR(circleRadius)-SQR(left)));
		pair<double, double> bottomPoint = make_pair(sqrt(SQR(circleRadius)-SQR(bottom)), bottom);

		// area of triangle
		double triangleArea = (leftPoint.second - bottom)*(bottomPoint.first - left)/2.0;
		double theChordArea = chordArea(findDistance(leftPoint, bottomPoint), circleRadius);
		return triangleArea + theChordArea;
	}
	else if (circleRadius < topLeftDistance && circleRadius >= bottomRightDistance)
	{ // left and right intersect
		pair<double, double> leftPoint = make_pair(left, sqrt(SQR(circleRadius)-SQR(left)));
		pair<double, double> rightPoint = make_pair(right, sqrt(SQR(circleRadius)-SQR(right)));

		// area of trapezoid
		double trapezoidArea = (((leftPoint.second - bottom)+(rightPoint.second - bottom))/2.0) * sideLength;
		double theChordArea = chordArea(findDistance(leftPoint, rightPoint), circleRadius);
		return trapezoidArea + theChordArea;
	}
	else if (circleRadius >= topLeftDistance && circleRadius >= bottomRightDistance)
	{ // top and right intersect
		pair<double, double> topPoint = make_pair(sqrt(SQR(circleRadius)-SQR(top)), top);
		pair<double, double> rightPoint = make_pair(right, sqrt(SQR(circleRadius)-SQR(right)));
		
		// subtract out area of triangle
		double totalArea = SQR(sideLength);
		double triangleArea = (right-topPoint.first)*(top-rightPoint.second)/2.0;
		double theChordArea = chordArea(findDistance(topPoint, rightPoint), circleRadius);
		return totalArea - triangleArea + theChordArea;
	}
	else
	{
		printf("bad case!\n");
		return 0;
	}
}

string findResult(FILE *inFile)
{
	char inBuffer[1000];
	fgets(inBuffer, 1000, inFile);

	double flyRadius, racquetRadius, racquetThickness, stringRadius, gapLength;
	sscanf(inBuffer, "%lf %lf %lf %lf %lf", &flyRadius, &racquetRadius, &racquetThickness, &stringRadius, &gapLength);

	double totalArea = M_PI*racquetRadius*racquetRadius;

	double safeArea = 0;

	racquetThickness += flyRadius;
	stringRadius += flyRadius;
	gapLength -= 2*flyRadius;

	if (gapLength <= 0)
		return "1.0000000000";

	// the problem is now to find the area covered by the racquet

	double openRadius = racquetRadius - racquetThickness;
	double squareOffset = gapLength + stringRadius*2;

	for(int i = -int(openRadius / squareOffset) - 1; i <= int(openRadius / squareOffset) + 2; i++)
	{ // 0 and lower is to the left; 1 and higher is to the right
		double xVal = i*squareOffset - (squareOffset/2.0);
		for(int j = -int(openRadius / squareOffset) - 1; j <= int(openRadius / squareOffset) + 2; j++)
		{
			double yVal = j*squareOffset - (squareOffset/2.0);
			safeArea += openArea(xVal, yVal, gapLength, openRadius);
		}
	}

	char outBuffer[1000];
	double result = 1-(safeArea / totalArea);
	if (result < .0000001)
		result = 0;

	sprintf(outBuffer, "%.10f", result);
	return string(outBuffer);
}

int main()
{
	char *inFilename = PROB_LETTER "-" INTYPE ".in";
	char *outFilename = PROB_LETTER "-" INTYPE ".out";

	FILE *inFile = fopen(inFilename, "r");
	FILE *outFile = fopen(outFilename, "w");

	if (inFile == NULL)
	{
		printf("inFile does not exist!\n");
		system("PAUSE");
		return 1;
	}
	if (outFile == NULL)
	{
		printf("Failed to open outFile!\n");
		system("PAUSE");
		return 1;
	}

	char inBuffer[1000];
	fgets(inBuffer, 1000, inFile);

	int numCases;
	sscanf(inBuffer, "%d", &numCases);

	for(int i = 1; i <= numCases; i++)
	{
		string result = findResult(inFile);

		fprintf(outFile, "Case #%d: %s\n", i, result.c_str());
		printf("done with case %d\n", i);
	}

	fclose(inFile);
	fclose(outFile);

	printf("Success!\n");
	system("PAUSE");
}