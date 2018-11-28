#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
using namespace std;
typedef long long ll;

double sumA;
vector<int> X, dX;
vector<double> Y, dY, A;

double findArea(double target)
{
	int loc = 0, start = 0;
	while (A[loc] < target)
	{
		start += dX[loc];
		target -= A[loc];
		++loc;
		
	}

	double f = Y[loc], g= dY[loc];
	if (g!=0.0)
	{
		double sqrTerm = (2.0 * target / g) + ((f/g)*(f/g));
		double term = sqrt(sqrTerm);
		double myX = term - (f/g);
		if (myX < 0.0 || myX > dX[loc])
			myX = -term -(f/g);
		return start + myX;
	}

	double extra = target/f;
	return start + extra;
}

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");

	fout << std::setprecision(20);

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int W,L,U,G;
	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> W >> L >> U >> G;
		vector<int> loX(L), loY(L), hiX(U), hiY(U);
		set<int> sAllX;
		for (int i=0; i<L; ++i)
		{
			fin >> loX[i] >> loY[i];
			sAllX.insert(loX[i]);
		}

		for (int i=0; i<U; ++i)
		{
			fin >> hiX[i] >> hiY[i];
			sAllX.insert(hiX[i]);
		}

		X.assign(sAllX.begin(), sAllX.end());
		Y.assign(X.size(), 0);
		dX.assign(X.size()-1, 0);
		dY.assign(X.size()-1, 0);
		A.assign(X.size()-1, 0);
		sumA = 0;

		Y[0] = hiY[0]-loY[0];
		//Y.back() = hi.back() - lo.back();
		int nextLo=1, nextHi=1, loc = 1;
		for (;loc < X.size();++loc)
		{
			dX[loc-1] = X[loc] - X[loc-1];

			bool onLo = X[loc] == loX[nextLo];
			bool onHi = X[loc] == hiX[nextHi];
			if (onLo && onHi)
			{
				Y[loc] = hiY[nextHi]-loY[nextLo];
				++nextHi; ++nextLo;
			}
			else if (onLo)
			{
				double yHi = double(hiY[nextHi-1]) + (double(hiY[nextHi]-hiY[nextHi-1]) / double(hiX[nextHi]-hiX[nextHi-1])) * (X[loc]-hiX[nextHi-1]);
				Y[loc] = yHi-loY[nextLo];
				++nextLo;
			}
			else if (onHi)
			{
				double yLo = double(loY[nextLo-1]) + (double(loY[nextLo]-loY[nextLo-1]) / double(loX[nextLo]-loX[nextLo-1])) * (X[loc]-loX[nextLo-1]);
				Y[loc] = hiY[nextHi]-yLo;
				++nextHi;
			}

			dY[loc-1] = (Y[loc] - Y[loc-1])/(X[loc]-X[loc-1]);
			A[loc-1] = Y[loc-1] * dX[loc-1] + 0.5 * dY[loc-1] * dX[loc-1] * dX[loc-1];
			sumA += A[loc-1];
		}

		fout << "Case #" << zz << ": " << endl;
		for (int i=1; i<G; ++i)
		{
			double target = (i * sumA) / G;
			double thisX = findArea(target);
			fout << thisX << endl;
		}
	}

	return 0;
}