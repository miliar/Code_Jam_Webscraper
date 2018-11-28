#include <stdio.h>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

////////////////////////////////////////////////////////////////////////////////////
//
/*
Input

One line containing an integer N, the number of test cases in the input file.

The next N lines will each contain the numbers f, R, t, r and g separated
by exactly one space. Also the numbers will have at most 6 digits after the decimal point.

Output

N lines, each of the form "Case #k: P", where k is the number of the test case
and P is the probability of hitting the fly with a piece of the racquet.

Answers with a relative or absolute error of at most 10^(-6) will be considered correct.
*/

#define PI	3.1415926535f

double calcShapeArea( const double& crossX, const double& crossY, const double& rad )
{
	double angle = asin( crossY / rad );
	double fanArea = rad * rad * angle * 0.5f;
	return fanArea - crossX * crossY * 0.5f;
}

double calcArea( const double& top, const double& left, const double& g,
				 const double& topCross, const double& bottomCross, const double& rad )
{
	double right = left + g, bottom = top - g;

	if ( topCross < left && bottomCross > left ) {
		// left-bottom
		double up = sqrt( rad * rad - left * left );
		double width = bottomCross - left;
		double bigArea = calcShapeArea( left, up, rad );
		double smallArea = calcShapeArea( bottomCross, bottom, rad );
		return bigArea - smallArea - width * bottom;
	}
	else if ( topCross >= left && bottomCross > left && bottomCross <= right ) {
		// top-bottom
		double width = bottomCross - topCross;
		double bigArea = calcShapeArea( topCross, top, rad );
		double smallArea = calcShapeArea( bottomCross, bottom, rad );
		return bigArea - smallArea - width * top + g * ( bottomCross - left );
	}
	else if ( topCross < right && bottomCross > right ) {
		// right-top
		double down = sqrt( rad * rad - right * right );
		double width = right - topCross;
		double bigArea = calcShapeArea( topCross, top, rad );
		double smallArea = calcShapeArea( right, down, rad );
		return bigArea - smallArea - width * top + g * g;
	}

	return 0.f;
}

double calcHoleArea( const double& rad, const double& stringRad, const double& g )
{
	double limit = rad * sin( PI / 4.f ), step = g + 2.f * stringRad;
	double area = 0.f, unitArea = g * g, base;

	int squareCount = ( int ) ( ( limit - stringRad ) / step );
	base = step * squareCount + stringRad;
	if ( limit - base >= g ) {
		squareCount++;
		base += step;
	}
	area += unitArea * squareCount * squareCount * 0.5f;

	for ( double bottom = stringRad; bottom < limit; bottom += step ) {
		double top = bottom + g;
		double topCross = ( rad >= top ) ? sqrt( rad * rad - top * top ) : 0.f;
		double bottomCross = ( rad >= bottom ) ? sqrt( rad * rad - bottom * bottom ) : 0.f;

		if ( top <= limit ) {
			// general case
			squareCount = ( int ) ( ( topCross - base ) / step );
			area += ( unitArea * squareCount );

			double temp = step * squareCount + base;
			if ( topCross - temp < g ) {
				// cut square
				area += calcArea( top, temp, g, topCross, bottomCross, rad );
			}
			else {
				area += unitArea;
			}

			if ( bottomCross - temp > step ) {
				// cut square
				area += calcArea( top, temp + step, g, topCross, bottomCross, rad );
			}
		}
		else {
			// last case
			// left and bottom is symmetric
			if ( topCross >= bottom && topCross < bottom + g ) {
				double localArea = calcArea( top, bottom, g, topCross, bottomCross, rad ) * 0.5f;
				area += localArea;
			}
			else if ( bottomCross >= bottom && bottomCross < bottom + g ) {
				double localArea = calcArea( top, bottom, g, topCross, bottomCross, rad ) * 0.5f;
				area += localArea;
			}

			double rightLeft = bottom + step;
			double sarea = calcArea( top, rightLeft, g, topCross, bottomCross, rad );
			area += sarea;
		}
	}

	return area * 8.f;
}

double calcProb( const double& f, const double& ringRad, const double& t, const double& stringRad, const double& g )
{
	double totalArea = PI * ringRad * ringRad;
	double holeArea = calcHoleArea( ringRad - t - f, stringRad + f , g - f * 2.f );

	return 1.f - holeArea / totalArea;
}

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("correct.in");
//#define cin fin

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		double f, ringRad, t, stringRad, g, prob;

		cin >> f >> ringRad >> t >> stringRad >> g;

		prob = calcProb( f, ringRad, t, stringRad, g );
		printf( "Case #%d: %0.6f\n", i, prob );
	}

	return 0;
}
