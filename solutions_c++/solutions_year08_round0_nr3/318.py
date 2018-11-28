// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>

#include <math.h>

using namespace std;

typedef	long long llong;

double Int(double x, double rsq)
{
	return 0.5*(x*sqrt(rsq - x*x) + rsq*asin(x/sqrt(rsq)));
}
double GetA(double x1, double x2, double rsq)
{
	return Int(x2, rsq) - Int(x1, rsq);
}

double GetA(double x1, double x2, double y1, double y2, double rsq)
{
	if (x1*x1 + y1*y1 >= rsq)
		return 0;
	double x = min(sqrt(rsq - y2*y2), x2);
	if (x1 < x)
		return (x-x1)*(y2-y1) + GetA(x, x2, y1, y2, rsq);
	else
	{
		x2 = min(x2, sqrt(rsq - y1*y1));
		return GetA(x1, x2, rsq) - y1*(x2-x1);
	}
}

double GetProb(double f, double R, double t, double r, double g)
{
	if (2*f >= g || R-t-f-r <= 0.0)
		return 1;
	double	dA = 0.0;
	double	dStep = 2*r+g;
	double	dMax = (R - t - r - f)/dStep;
	double rsq = (R-t-f)*(R-t-f);
	for (int i = 0; i <= dMax; ++i)
	{
		for (int j = 0; j < dMax; ++j)
			dA += GetA(r + f + i*dStep, r + g-f + i*dStep, r + f + j*dStep, r + g-f + j*dStep, rsq);
	}
	return 1.0 - 4*dA/(3.14159265358979323846*R*R);
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream	infile("C-large.in");
	ofstream	outfile("C-large.out");

	size_t		nCases;

	infile >> nCases;
	for (size_t i = 0; i < nCases; ++i)
	{
		double f, R, t, r, g;
		infile >> f >> R >> t >> r >> g;
		outfile << "Case #" << i+1 << ": " << GetProb(f, R, t, r, g) << std::endl;
	}

	return 0;
}

