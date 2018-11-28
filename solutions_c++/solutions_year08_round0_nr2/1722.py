// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <algorithm>
#include <fstream>

int conv(std::string s)
{
	int d1 = (s[0]-'0');
	int d2 = (s[1]-'0');
	int d3 = (s[3]-'0');
	int d4 = (s[4]-'0');
	return d4 + 10*d3 + 60*(d2+10*d1);
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream fin("input.txt");
	std::ofstream fout("output.txt");

	if( !fin )
		return 0;

	int N;
	fin >> N;
	for( int case_no = 1; case_no <= N; case_no++ )
	{
		int T, NA, NB;
		fin >> T;
		fin >> NA >> NB;
		std::vector<int> v1, v2;
		int TIME = 60*24 + 100;
		v1.resize( TIME );
		v2.resize( TIME );
		for( int i = 0; i < NA+NB; i++ )
		{
			std::string s1, s2;
			fin >> s1 >> s2;
			int t1 = conv(s1);
			int t2 = conv(s2);
			if( i < NA )
			{
				v1[t1]--;
				v2[t2+T]++;
			}
			else
			{
				v2[t1]--;
				v1[t2+T]++;
			}
		}
		int min1 = 0, min2 = 0;
		int c1 = 0, c2 = 0;
		for( size_t t = 0; t < TIME; t++ )
		{
#define min(a,b) a<b?a:b
			c1 += v1[t];
			min1 = min(c1,min1);
			c2 += v2[t];
			min2 = min(c2,min2);
		}
		fout << "Case #" << case_no << ": " << -min1 << " " << -min2 << "\n";
	}

	return 0;
}

