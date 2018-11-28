// g_4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <list>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <sstream>
#include <string>

__int64 euclid(__int64 a, __int64 b)
{
	if(b == 0)
	{
		return a;
	}
	else
	{
		return euclid(b, a % b);
	}
}

/*
MSVS 2008

The program must be run with:
first argument = text file with input data
second argument = file name to write output data
*/
int _tmain(int argc, _TCHAR* argv[])
{
	////////////////////////////////////
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
		f >> N;
		std::vector<__int64> vec;
		vec.resize(N);

		for(int n = 0; n < N; n++)
		{
			std::string s;
			f >> s;
			vec[n] = _atoi64(s.c_str());
		}

		std::sort(vec.begin(), vec.end());
		std::vector<__int64> diff;
		for(size_t j1 = 0; j1 < vec.size(); j1++)
		{
			for(size_t j2 = j1 + 1; j2 < vec.size(); j2++)
			{
				__int64 a = vec[j2] - vec[j1];
				if(0 != a)
				{
					diff.push_back(a);
				}
			}
		}

		std::sort(diff.begin(), diff.end());
		__int64 T = 0;

		if(diff.size() > 1)
		{
			std::vector<__int64> vec2 = diff;
			std::vector<__int64> vec3;

			while(true)
			{
				vec3.clear();

				for(size_t i1 = 1; i1 < vec2.size(); i1++)
				{
					vec3.push_back(euclid(vec2[i1 - 1], vec2[i1]));
				}

				if(vec3.size() == 1)
				{
					break;
				}

				vec2 = vec3;
			}

			T = vec3[0];
		}
		else
		{
			T = diff[0];
		}
	
		__int64 y = 0;
		int n = 1;

		while(true)
		{
			if(n * T >= vec[0])
			{
				y = n * T - vec[0];

				bool ok = true;
				for(size_t j = 1; j < vec.size(); j++)
				{
					if((vec[j] + y) % T != 0)
					{
						ok = false;
						break;
					}
				}

				if(ok)
				{
					break;
				}
			}
			else
			{
				n++;
			}
		}

		f2 << "Case #" << t+1 << ": " << y << std::endl;
	}

	return 0;
}

