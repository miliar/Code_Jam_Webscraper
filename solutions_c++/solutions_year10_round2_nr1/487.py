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

		int M;
		f >> M;

		std::set<std::string> havedirs;
		for(int j = 0; j < N; j++)
		{
			std::string dir;
			f >> dir;
			havedirs.insert(dir);
		}

		int create = 0;
		for(int j = 0; j < M; j++)
		{
			std::string dir;
			f >> dir;
			int pos = 0;
			while(pos = dir.find("/", pos + 1))
			{
				std::string sub = dir.substr(0, pos);
				if(havedirs.find(sub) == havedirs.end())
				{
					havedirs.insert(sub);
					create ++;
				}
			}
		}

		f2 << "Case #" << t+1 << ": " << create << std::endl;
	}

	return 0;
}

