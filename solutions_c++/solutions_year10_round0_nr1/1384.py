#include "stdafx.h"
#include <fstream>
#include <vector>
#include <list>
#include <iostream>

/*
MSVS 2008 sp1 

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
		int n;
		__int64 k;
		f >> n;
		f >> k;

		__int32 divider = 1 << n;
		__int64 divResult = (k + 1) % divider;

		f2 << "Case #" << t+1 << ":";
		if(0 == divResult)
		{
			f2 << " ON" << std::endl;
		}
		else
		{
			f2 << " OFF" << std::endl;
		}
	}

	return 0;
}

