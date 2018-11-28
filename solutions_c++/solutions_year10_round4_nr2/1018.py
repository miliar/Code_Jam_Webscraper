// g_1.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <vector>
#include <list>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <sstream>
#include <string>


/*
MSVS 2008

The program must be run with:
first argument = text file with input data
second argument = file name to write output data
*/
int _tmain(int argc, _TCHAR* argv[])
{
	////////////////////////////////////
	const TCHAR * cfin = NULL;
	const TCHAR * cfout = NULL;

	if(argc < 3)
	{
		cfin = _T("test.txt");
		cfout = _T("test2.out");
	}
	else
	{
		cfin = argv[1];
		cfout = argv[2];
	}

	std::fstream f;
	f.open(cfin);

	std::fstream f2;
	f2.open(cfout, std::fstream::out);

	int tasks;
	f >> tasks;

	std::vector<std::vector<int>> v;
	std::vector<int> M;
	for(int t = 0; t < tasks; t++)
	{
		int p2;
		f >> p2;
		v.resize(p2);

		int np = 1 << p2;

		M.resize(np);
		for(int i = 0; i < np; i++)
		{
			int jj;
			f >> jj;
			M[i] = jj;
			M[i] = p2 - M[i];
		}

		for(int i = 0; i < p2; i++)
		{
			v[i].resize(np);
			for(int j = 0; j < 1 << (p2 - i - 1); j++)
			{
				f >> v[i][j];
			}
		}

		int money = 0;
		for(int i = p2; i > 0; i--)
		{
			int add = -1;
			for(int k = 0; k < np; k++)
			{
				if(M[k] > 0)
				{
					M[k] --;
					int nadd = k / (1 << i);
					if(nadd != add)
					{
						money += v[i - 1][nadd];
						add = nadd;
					}
				}
			}
		}

		f2 << "Case #" << t + 1 << ": " << money << std::endl;
	}

	return 0;
}

