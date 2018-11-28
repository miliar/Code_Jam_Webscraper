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

llong GetTrgCount(int n, llong A, llong B, llong C, llong D, llong x0, llong y0, llong M)
{
	int		N[3][3] = {{0, 0, 0},{0, 0, 0},{0, 0, 0}};
	llong X = x0, Y = y0;
	for (int i = 0; i < n; ++i)
	{
		N[X % 3][Y % 3]++;
		X = (A*X + B) % M;
		Y = (C*Y + D) % M;
	}
	llong res = 0;
	for (int i = 0; i < 3; ++i)
	{
		for (int j = 0; j < 3; ++j)
		{
			llong add = 0;
			for (int k = 0; k < 3; ++k)
			{
				for (int l = 0; l < 3; ++l)
				{
					llong addd = 0;
					int s = (6 - (i + k)) % 3;
					int t = (6 - (j + l)) % 3;

					if (k==i && l==j)
					{
						if (s == i && t == j)
							addd = N[i][j]*((N[i][j]-1)*(N[i][j]-2));
						else
							addd = N[i][j]*((N[i][j]-1)*N[s][t]);
					}
					else
					{
						if (s == i && t == j || s == k && t == l)
							addd = N[i][j]*N[k][l]*(N[s][t]-1);
						else
							addd = N[i][j]*N[k][l]*N[s][t];
					}
					add += addd;
				}
			}
			res += add;
		}
	}
	return res/6;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream	infile("A-small.in");
	ofstream	outfile("A-small.out");

	size_t		nCases;

	infile >> nCases;
	for (size_t i = 0; i < nCases; ++i)
	{
		int n;
		llong	A, B, C, D, x0, y0, M;
		infile >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		outfile << "Case #" << i+1 << ": " << GetTrgCount(n, A, B, C, D, x0, y0, M) << std::endl;
	}

	return 0;
}

