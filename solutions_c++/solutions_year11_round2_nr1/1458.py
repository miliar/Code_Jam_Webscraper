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
#include <set>

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
		int N;
		f >> N;

		char * table = new char[N * N];

		double * WPI = new double[N];
		double * OWP = new double[N];
		double * OOWP = new double[N];
		int * wins = new int[N * N];
		int * loses = new int[N * N];

		for(int i = 0; i < N; i ++)
		{
			std::string s;
			f >> s;
			WPI[i] = 0;
			int nWin = 0;
			int nLoose = 0;
			for(int j = 0; j < N; j ++)
			{
				table[i*N+j] = s[j];
				if(s[j] == '1')
					nWin ++;
				else if(s[j] == '0')
					nLoose ++;
			}
			for(int j = 0; j < N; j ++)
			{
				if(s[j] == '1')
				{
					wins[i*N + j] = nWin - 1;
					loses[i*N + j] = nLoose;
				}
				else if(s[j] == '0')
				{
					wins[i*N + j] = nWin;
					loses[i*N + j] = nLoose - 1;
				}
			}
			WPI[i] = double(nWin) / double(nWin + nLoose);
		}

		for(int i = 0; i < N; i ++)
		{
			OWP[i] = 0;
			int nGames = 0;
			for(int j = 0; j < N; j ++)
			{
				if(table[i*N+j] != '.')
				{
					OWP[i] += double(wins[j*N + i]) / double(wins[j*N + i] + loses[j*N + i]);
					nGames ++;
				}
			}
			OWP[i] /= double(nGames);
		}

		for(int i = 0; i < N; i ++)
		{
			OOWP[i] = 0;
			int nGames = 0;
			for(int j = 0; j < N; j ++)
			{
				if(table[i*N+j] != '.')
				{
					nGames ++;
					OOWP[i] += OWP[j];
				}
			}
			OOWP[i] /= double(nGames);
		}

		f2 << "Case #" << t+1 << ": " << std::endl;
		for(int i = 0; i < N; i ++)
		{
			char buff[100];
			sprintf(buff, "%.12lf", (0.25 * WPI[i] + 0.5*OWP[i] + 0.25*OOWP[i]));
			f2 << buff << std::endl;
		}
		//f2 << "Case #" << t+1 << ": " << time << std::endl;

		delete table;
		delete OWP;
		delete OOWP;
		delete wins;
		delete loses;
		delete WPI;
	}

	return 0;
}

