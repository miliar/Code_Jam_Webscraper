// Was build with STL libraries of standard MS VisualStudio 2005 SP1
// Target application was console win 32 application with multibite character set setting. 
// Used software were licensed to Align Technology Inc

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
#define M_PI       3.14159265358979323846

/////////////////////////////////////////////////////////////////

double sectorArea(double R, double X)
{
	return 0.5*(R*R*asin(X/R)+X*sqrt(R*R-X*X));
}

double isectArea(double sqrCtX, double sqrCtY, double sqrSz, double R)
{
	double lower = sqrCtY - sqrSz / 2;
	double upper = sqrCtY + sqrSz / 2;
	double left = sqrCtX - sqrSz / 2;
	double right = sqrCtX + sqrSz / 2;
	double lowerCross = R*R - lower*lower;
	if(lowerCross < left*left)
		return 0;
	if(lowerCross < right*right)
		right = sqrt(lowerCross);
	double upperCross = R*R - upper*upper;
	if(upperCross >= right*right)
		return (right-left)*sqrSz;
	double result = 0;
	if(upperCross > left*left)
	{
		double nLeft = sqrt(upperCross);
		result += sqrSz*(nLeft-left);
		left = nLeft;
	}
	result+=sectorArea(R, right) - sectorArea(R, left) - (right-left)*lower;
	return result;
}

int main(int argc, char* argv[])
{
	int numOfCases;
	std::cin >> numOfCases;
	for(int cn = 0; cn < numOfCases; cn++)
	{
		double f, R, t, r, g;
		std::cin >> f >> R >> t >> r >> g;
		double cell = 2*r+g;
		double square = g-2*f;
		double inbound = R-t-f;
		if(square <= 0 || inbound <= 0)
		{
			std::cout << "Case #" << (cn+1) << ": "<< 1 <<"\n";
			continue;
		}
		double totalArea = M_PI*R*R;
		double squaresArea = 0;
		int outboundRaw = ceil(inbound / cell);
		for(int i = 0; i < outboundRaw; i++)
		{
			double nextStripe = (i+1)*cell-r-f;
			double thisStripe = i*cell+r+f;
			double nextHeightSqr = inbound*inbound-nextStripe*nextStripe;
			int fullBlocks = 0;
			if(nextHeightSqr > 0)
				fullBlocks = (sqrt(nextHeightSqr)+r+f)/cell;
			squaresArea += square*square*fullBlocks;
			double thisHeightSqr = inbound*inbound-thisStripe*thisStripe;
			int partialBlocks = 0;
			if(thisHeightSqr > 0)
				partialBlocks = ceil((sqrt(thisHeightSqr)-r-f)/cell);
			for(int c=fullBlocks; c < partialBlocks; c++)
			{
				double centerX = (i+0.5)*cell;
				double centerY = (c+0.5)*cell;
				squaresArea+=isectArea(centerX, centerY, square, inbound);
			}
		}
		std::cout << "Case #" << (cn+1) << ": "<< (1-4*squaresArea / totalArea) <<"\n";
	}
	return 0;
}

