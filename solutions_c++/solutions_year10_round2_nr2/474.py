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

	for(int t = 0; t < tasks; t++)
	{
		int N, K, B, T;
		f >> N >> K >> B >> T;

		std::vector<int> X;
		X.resize(N);
		for(int j = 0; j < N; j++)
		{
			f >> X[j];
		}

		std::vector<int> V;
		V.resize(N);
		for(int j = 0; j < N; j++)
		{
			f >> V[j];
		}

		std::vector<double> time;
		time.resize(N);
		for(int j = 0; j < N; j++)
		{
			time[j] = (double(B) - double(X[j])) / double(V[j]);
		}

		int count = 0;
		int got = 0;
		int ng = 0;
		for(int j = N - 1; j >= 0; j--)
		{
			if(time[j] <= T)
			{
				got ++;
				count += ng;
			}
			else
			{
				ng ++;
			}

			if(got >= K)
			{
				break;
			}
		}

		f2 << "Case #" << t+1 << ": ";
		if(got < K)
		{
			f2 << "IMPOSSIBLE";
		}
		else
		{
			f2 << count;
		}
		f2 << std::endl;
	}

	return 0;
}

