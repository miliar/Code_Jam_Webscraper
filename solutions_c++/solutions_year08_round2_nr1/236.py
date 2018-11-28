// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <limits>
#include <stdexcept>

#include <math.h>
static const double pi = 3.1415926535;

using namespace std;


typedef long long LL;
typedef pair<LL, LL> PLL;

#define sz(v) ((int)v.size())


bool pllless(PLL p1, PLL p2)
{
	return (p1.first < p2.first) || ((p1.first == p2.first) && (p1.second < p2.second));
}

bool neq(PLL p1, PLL p2)
{
	return ((p1.first != p2.first) || (p1.second != p2.second));
}

class Q11
{
private:
	Q11() {};
public:
	static void go(string inputFilePath, string outputFilePath)
	{
		ifstream inpf(inputFilePath.c_str());
		ofstream outf(outputFilePath.c_str());

		if (!inpf.good() || !outf.good())
		{
			throw(std::invalid_argument("Can't open input or output file!"));
		}

		int N;
		inpf >> N;

		for (int n = 1; n <= N; ++n)
		{
			LL nn, A, B, C, D, x0, y0, M;
			inpf >> nn >> A >> B >> C >> D >> x0 >> y0 >> M;

			vector<PLL> v;
			LL X = x0;
			LL Y = y0;
			v.push_back(PLL(X, Y));
			for (int i = 1; i <= nn - 1; ++i)
			{
			  X = (A * X + B) % M;
			  Y = (C * Y + D) % M;
			  v.push_back(PLL(X, Y));
			}

			sort(v.begin(), v.end(), pllless);

			int ctr = 0;
			for (int i1 = 0; i1 < sz(v); ++i1)
			{
				for (int i2 = i1 + 1; i2 < sz(v); ++i2)
				{
					for (int i3 = i2 + 1; i3 < sz(v); ++i3)
					{
						if (neq(v[i1], v[i2]) && neq(v[i1], v[i3]) && neq(v[i2], v[i3]))
						{
							if ((((v[i1].first + v[i2].first + v[i3].first) % 3) == 0) &&
							    (((v[i1].second + v[i2].second + v[i3].second) % 3) == 0))
							{
								++ctr;
							}
						}
					}	
				}
			}

			outf << "Case #" << n << ": " << ctr << endl;
		}
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	Q11::go("input.txt", "output.txt");

	cout << endl;
	getchar();
	return 0;
}

