// g_4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <list>
#include <iostream>

class cycleInfo
{
public:
	cycleInfo() :
	  money(0), ng(0)
	  {
	  }

	  __int64 money;
	  int ng;
};

/*
MSVS 2008

The program must be run with:
first argument = text file with input data
second argument = file name to write output data
*/
int _tmain(int argc, _TCHAR* argv[])
{
	const TCHAR * cfin = argv[1];
	const TCHAR * cfout = argv[2];

	std::fstream f;
	f.open(cfin);

	std::fstream f2;
	f2.open(cfout, std::fstream::out);

	int tasks;
	f >> tasks;

	for(int t = 0; t < tasks; t++)
	{
		int N;
		__int64 R, k;
		f >> R >> k >> N;

		std::vector<__int64> g;
		g.resize(N);

		std::vector<__int64> tg;
		tg.resize(2*N);

		for(int y = 0; y < N; y++)
		{
			f >> g[y];
			tg[y + N] = tg[y] = g[y];
		}

		std::vector<cycleInfo> p;
		p.resize(N);

		for(int y = 0; y < N; y++)
		{
			p[y].ng = y;
			for(int y2 = y; y2 < y + N; y2++)
			{
				if(p[y].money + tg[y2] <= k)
				{
					p[y].money += tg[y2];
					p[y].ng ++;
				}
				else
				{
					break;
				}
			}
		}

		for(int y = 0; y < N; y++)
		{
			p[y].ng %= N;
		}

		std::vector<int> wh;
		wh.resize(N);

		std::vector<__int64> kc;

		int K = 0;
		__int64 Kmoney = 0;
		int iCur = 0;
		int cStart = 0;
		while(!wh[iCur])
		{
			K ++;
			Kmoney += p[iCur].money;
			kc.push_back(Kmoney);
			wh[iCur] = K;
			iCur = p[iCur].ng;
			cStart = wh[iCur] - 1;
		}

		R -= cStart;
		__int64 fullCycles = R / (K - cStart);
		__int64 remaindCycles = R % (K - cStart);

		Kmoney -= cStart > 0 ? kc[cStart - 1] : 0;
		__int64 totalMoney = cStart > 0 ? kc[cStart - 1] : 0;
		totalMoney += fullCycles * Kmoney;
		if(remaindCycles > 0)
		{
			totalMoney += kc[int(remaindCycles - 1) + cStart] - (cStart > 0 ? kc[cStart - 1] : 0);
		}

		f2 << "Case #" << t+1 << ": " << totalMoney << std::endl;
	}

	return 0;
}

