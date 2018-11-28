// google.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

const double mega_pi = 3.1415926535897932384626433832795;

std::string garbage;

void solve_case(int cas, std::ifstream & fs, std::ofstream & ofs)
{
	int K = 0;
	fs >> K;
	int n = 0;
	fs >> n;

	ofs << "Case #" << cas << ": ";
	for(int i = 0; i != n; ++i)
	{
		int d = 0;
		fs >> d;
		int next_value = 1;
		int before = d - 1;
		int after = K - d;
		for(;true; next_value += 1)
		{
			int rotate = next_value - 1;
			rotate %= (K + 1 - next_value);
			if( rotate < before )
			{
				before -= rotate;
				after += rotate;
				before -= 1; // remove card
				continue;
			}
			if( rotate > before )
			{
				rotate -= before + 1;
				before += after;
				after = 0;

				before -= rotate;
				after += rotate;
				before -= 1; // remove card
				continue;
			}
			if( before == rotate )
			{
				break; // solution
			}
		}
		ofs << next_value << " ";
	}
	ofs << std::endl;
/*
	std::vector<__int64> x(len);
	std::vector<__int64> y(len);
	for(int i = 0; i != len; ++i)
	{
		fs >> x[i];
	}
	for(int i = 0; i != len; ++i)
	{
		fs >> y[i];
	}
	__int64 total = 0;
	for(int i = 0; i != len; ++i)
	{
		std::vector<__int64>::iterator xmi = std::min_element(x.begin(), x.end());
		std::vector<__int64>::iterator xma = std::max_element(x.begin(), x.end());
		std::vector<__int64>::iterator ymi = std::min_element(y.begin(), y.end());
		std::vector<__int64>::iterator yma = std::max_element(y.begin(), y.end());
		__int64 xmiyma = *xmi * *yma;
		__int64 xmaymi = *xma * *ymi;
		if( xmiyma < xmaymi )
		{
			total += xmiyma;
			x.erase(xmi);
			y.erase(yma);
		}
		else
		{
			total += xmaymi;
			x.erase(xma);
			y.erase(ymi);
		}
	}
*/
/*	if( !r )
		ofs << "IMPOSSIBLE" << std::endl;
	else
	{
		for(int i = 0; i != flavors; ++i)
		{
			int fl = (used_flavours[i+1] == 1);
			ofs << fl << " ";
		}
		ofs << std::endl;
	}*/
}

int main(int argc, char * argv[])
{
	std::ifstream fs("input.txt");
	std::ofstream ofs("output.txt");
	int n_cases = 0;
	fs >> n_cases;
	std::getline(fs, garbage);
	for(int c = 0; c != n_cases; ++c)
	{
		solve_case(c + 1, fs, ofs);
	}
	return 0;
}
