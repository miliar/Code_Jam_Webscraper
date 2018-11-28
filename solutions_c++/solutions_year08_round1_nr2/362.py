// milkshakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>

#define FILE_IN "smallin.txt"
#define FILE_OUT "smallout.txt"

int order[1024];

typedef std::pair<int, int>request;

std::vector<std::vector<request> >r;

int cmp_function(int a, int b)
{
	int n1a = 0;
	while (a)
	{
		a &= a - 1;
		n1a++;
	}
	int n1b = 0;
	while (b)
	{
		b &= b - 1;
		n1b++;
	}
	return n1a < n1b ? 1 : 0;
}


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream fin(FILE_IN);
	std::ofstream fout(FILE_OUT);

	int i, t;
	for (i = 0; i < 1024; ++i)
		order[i] = i;
	std::sort(order, order + 1023, cmp_function);

	/*for (i = 0; i < 1024; ++i)
		fout<<order[i]<<std::endl;*/

	fin>>t;
	for (i = 1; i <= t; ++i)
	{
		int n, m;
		fin>>n;
		fin>>m;
		
		r.clear();
		r.resize(m);

		for (int j = 0; j < m; ++j)
		{
			int nr;
			fin>>nr;
			r[j].resize(nr);
			for (int k = 0; k < nr; ++k)
			{
				int index, type;
				fin>>index>>type;
				index--;
				type<<= index;
				r[j][k] = std::make_pair(index, type);
			}
		}

		bool solution = false;
		for (int j = 0; j < 1024 && !solution; ++j)
		{
			if (order[j] >= (1<<n)) continue;

			bool allOk = true;

			for (int k = 0; k < m && allOk; ++k)
			{
				bool thisOk = false;
				for (int l = 0; l < r[k].size() && !thisOk; ++l)
				{
					if ( (order[j] & (1<<r[k][l].first)) == r[k][l].second)
						thisOk = true;
				}
				if (!thisOk)
					allOk = false;
			}

			if (allOk)
			{
				fout<<"Case #"<<i<<":";
				for (int k = 0; k < n; ++k)
					fout<<" "<<((order[j] & (1<<k)) > 0 ? 1 : 0);
				fout<<std::endl;
				solution = true;
			}
		}
		if (!solution)
		{
			fout<<"Case #"<<i<<": IMPOSSIBLE"<<std::endl;
		}
	}
	return 0;
}

