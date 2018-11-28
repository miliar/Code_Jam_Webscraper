// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

#include <math.h>

using namespace std;

typedef	long long llong;
typedef pair<llong, llong>	TCoord;

TCoord	divisors[10001];

bool GetTrg(llong A, llong N, llong M, TCoord trg[3])
{
	for (llong a = N; a > 0; --a)
	{
		llong b = A/a;
		b = min(b, M);
		llong q = A - a*b;
		llong c, d = -1;
		if (q != 0)
		{
			for (c = 1; c*c <= q; ++c)
			{
				if (a + c <= N && q % c == 0 && (q/c <= M))
				{
					d = q/c;
					break;
				}
			}
		}
		else
		{
			c = d = 0;
		}

		if (d != -1)
		{
			trg[2].first = a + c;
			trg[2].second = b;
			trg[0].second = d;
			trg[0].first = 0;
			trg[1].first = a;
			trg[1].second = 0;
			llong S = (trg[0].second + trg[1].second)*(trg[1].first - trg[0].first) + 
				(trg[1].second + trg[2].second)*(trg[2].first - trg[1].first) + 
				(trg[2].second + trg[0].second)*(trg[0].first - trg[2].first);
			if (A != abs((long)S))
				cout << "FAILURE";
			return true;
		}
	}
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream	infile("B-small.in");
	ofstream	outfile("B-small.out");

	size_t		nCases;

	infile >> nCases;
	for (size_t i = 0; i < nCases; ++i)
	{
		llong	A, N, M;
		infile >> N >> M >> A;
		cout << i+1 << " ";
		TCoord		trg[3];
		outfile << "Case #" << i+1 << ": ";
		if (GetTrg(A, N, M, trg))
		{
			for (size_t j = 0; j < 3; ++j)
				outfile <<  trg[j].first << " " << trg[j].second << " ";
		}
		else
			outfile << "IMPOSSIBLE";
		outfile << std::endl;
		cout << endl;

	}

	return 0;
}

