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
		int n;
		f >> n;

		std::vector<__int64> candies;
		candies.resize(n);

		__int64 check = 0;
		__int64 sum = 0;
		for(int i = 0; i < n; i++)
		{
			f >> candies[i];
			check ^= candies[i];
			sum += candies[i];
		}

		if(0 != check)
		{
			f2 << "Case #" << t+1 << ": " << "NO" << std::endl;
		}
		else
		{
			__int64 m = candies[0];
			for(int k = 0; k < n; k++)
				m = std::min(candies[k], m);
			f2 << "Case #" << t+1 << ": " << (sum - m) << std::endl;
		}
	}

	return 0;
}

