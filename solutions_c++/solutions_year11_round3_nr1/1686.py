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

bool set_square(char * tbl, int R, int C, int i, int j)
{
	if(i >= R - 1 || j >= C - 1)
		return false;

	if(tbl[i*C+j] != '#' || tbl[i*C+j+1] != '#'
		|| tbl[(i+1)*C+j] != '#' || tbl[(i+1)*C+j+1] != '#')
		return false;

	tbl[i*C+j] = '/';
	tbl[i*C+j+1] = '\\';
	tbl[(i+1)*C+j] = '\\';
	tbl[(i+1)*C+j+1] = '/';

	return true;
}

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
		int R, C;
		f >> R >> C;

		char * tiles = new char[R*C];

		for(int i = 0; i < R; i++)
		{
			std::string row;
			f >> row;
			for(int j = 0; j < C; j++)
			{
				tiles[i*C+j] = row[j];
			}			
		}

		bool possible = true;
		for(int i = 0; i < R && possible; i++)
		{
			for(int j = 0; j < C && possible; j++)
			{
				if(tiles[i*C+j] == '#')
				{
					if(!set_square(tiles, R, C, i, j))
					{
						possible = false;
						break;
					}
				}
			}			
		}

		if(!possible)
		{
			f2 << "Case #" << t+1 << ": " << std::endl << "Impossible" << std::endl;
// 			for(int i = 0; i < R; i++)
// 			{
// 				if(i > 0)
// 					f2 << std::endl;
// 
// 				for(int j = 0; j < C; j++)
// 				{
// 					f2 << tiles[i*C+j];
// 				}			
// 			}
// 			f2 << std::endl;
		}
		else
		{
			f2 << "Case #" << t+1 << ": " << std::endl;
			for(int i = 0; i < R; i++)
			{
				if(i > 0)
					f2 << std::endl;

				for(int j = 0; j < C; j++)
				{
					f2 << tiles[i*C+j];
				}			
			}
			f2 << std::endl;
		}
		delete tiles;
		//f2 << "Case #" << t+1 << ": " << time << std::endl;
	}

	return 0;
}

