// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <limits>
#include <stdexcept>

#include <math.h>
static const double pi = 3.1415926535;

using namespace std;


class QC
{
private:
	double f, R, t, r, g;

	double IndefIntegral(double x);
	double DefIntegral(double a, double b);
	double Area(double xblo, double yblo);
	double WholeArea();	
	double Probability();	

public:
	static void go(string inputFilePath, string outputFilePath);
};

double QC::IndefIntegral(double x)
{
	const double K = R - t - f;
	return .5 * (x * sqrt(K * K - x * x) + K * K * asin(x / K));
}

double QC::DefIntegral(double a, double b)
{
	return IndefIntegral(b) - IndefIntegral(a);
}

double QC::Area(double xblo, double yblo)
{
	double xbli = xblo + r + f;
	double ybli = yblo + r + f;

	double xtri = xblo + r + g - f;
	double ytri = yblo + r + g - f;

	if ((xbli >= xtri) ||
		(ybli >= ytri))
		return 0;

	if ((xbli > R - t - f) || 
		(ybli > R - t - f))
		return 0;

	double ylc = sqrt((R - t - f) * (R - t - f) - xbli * xbli);
	double yrc = (xtri < R - t - f) ? sqrt((R - t - f) * (R - t - f) - xtri * xtri) : ybli;

	double xtc = (ytri < R - t - f) ? sqrt((R - t - f) * (R - t - f) - ytri * ytri) : xbli;
	double xbc = sqrt((R - t - f) * (R - t - f) - ybli * ybli);

	double boxl;
	double boxr;
	double intl;
	double intr;

	if (ylc < ybli)
	{
		boxl = boxr = intl = intr = 0;
	}
	else if (yrc > ytri)
	{
		boxl = xbli;
		boxr = xtri;
		intl = intr = 0;
	}
	else if (ylc < ytri)
	{
		boxl = boxr = 0;
		intl = xbli;
		intr = min(xtri, xbc);
	}
	else
	{
		boxl = xbli;
		intl = boxr = xtc;
		intr = min(xtri, xbc);
	}

	double boxArea = (boxr - boxl) * (ytri - ybli);
	double intArea =  DefIntegral(intl, intr) - ybli * (intr - intl);

	return boxArea + intArea;
}

double QC::WholeArea()
{
	double curY = 0;
	double wholeArea = 0;
	while (curY < R)
	{
		double curX = 0;
		while (curX < R)
		{
			wholeArea += Area(curX, curY);
			curX += g + 2 * r;
		}
		curY += g + 2 * r;
	}

	return wholeArea * 4;
}

double QC::Probability()
{
	if (t + f < R)
		return 1. - WholeArea() / (pi * R * R);
	else
		return 1;
}

void QC::go(string inputFilePath, string outputFilePath)
{
	ifstream inpf(inputFilePath.c_str());
	ofstream outf(outputFilePath.c_str());

	if (!inpf.good() || !outf.good())
	{
		throw(std::invalid_argument("Can't open input or output file!"));
	}

	outf.precision(6);
	outf << fixed;

	int N;
	inpf >> N;

	for (int n = 1; n <= N; ++n)
	{
		QC qc;
		inpf >> qc.f >> qc.R >> qc.t >> qc.r >> qc.g;

		double p = qc.Probability();
		outf << "Case #" << n << ": " << p << endl;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	QC::go("input.txt", "output.txt");

	cout << endl;
	getchar();
	return 0;
}

