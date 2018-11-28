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

typedef std::pair<char, int> STEP;
std::vector<STEP>::const_iterator GetNextBtn(std::vector<STEP>::const_iterator cur, std::vector<STEP> & vec, char r, bool inc = true)
{
	if(cur == vec.end())
		return cur;
	if(inc)
		cur ++;
	for(; cur != vec.end(); cur++)
	{
		if(cur->first == r)
			break;
	}
	return cur;
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
		int N;
		f >> N;

		std::vector<STEP> steps;
		for(int n = 0; n < N; n++)
		{
			STEP s;
			f >> s.first;
			f >> s.second;
			steps.push_back(s);
		}

		int time = 0;
		int oPos = 1;
		int bPos = 1;
		std::vector<STEP>::const_iterator o = GetNextBtn(steps.begin(), steps, 'O', false);
		std::vector<STEP>::const_iterator b = GetNextBtn(steps.begin(), steps, 'B', false);
		std::vector<STEP>::const_iterator now = steps.begin();
		while(o != steps.end() || b != steps.end())
		{
			bool incNow = false;

			if(o != steps.end())
			{
				if(oPos < o->second)
					oPos ++;
				else if(oPos > o->second)
					oPos --;
				else
				{
					if(now->first == 'O')
					{
						o = GetNextBtn(o, steps, 'O');
						incNow = true;
					}
				}
			}

			if(b != steps.end())
			{
				if(bPos < b->second)
					bPos ++;
				else if(bPos > b->second)
					bPos --;
				else
				{
					if(now->first == 'B')
					{
						b = GetNextBtn(b, steps, 'B');
						incNow = true;
					}
				}
			}

			if(incNow)
				now ++;
			time ++;
		}

		f2 << "Case #" << t+1 << ": " << time << std::endl;
	}

	return 0;
}

