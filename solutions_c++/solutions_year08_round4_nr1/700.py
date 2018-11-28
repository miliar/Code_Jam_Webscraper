// booltree.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <algorithm>

const int INFI = 1<<28;
const int NMAX = 10000;

int main()
{
	std::ifstream fin("bigin.txt");
	std::ofstream fout("bigout.txt");

	int t;
	fin>>t;
	for (int nt = 1; nt <= t; ++nt)
	{
		int n, v, i;
		fin>>n>>v;
		int type[NMAX]; //or, and
		int ch[NMAX]; //changeable
		int need[2][NMAX];

		for (i = 0; i < n; ++i)
			need[0][i] = need[1][i] = INFI;

		for (i = 0; i < (n - 1) / 2; ++i)
		{
			fin>>type[i]>>ch[i];
		}
		for (; i < n; ++i)
		{
			int val;
			fin>>val;
			need[val][i] = 0;
		}
		for (i = (n - 1) / 2 - 1; i >= 0; --i)
		{
			int l = 2 * i + 1;
			int r = 2 * i + 2;

			//false

			//or
			int cost = need[0][l] + need[0][r];
			if (type[i]) 
			{
				if (ch[i]) cost++;
				else cost = INFI;
			}
			need[0][i] = std::min(need[0][i], cost);
			//and
			if (type[i] || ch[i])
			{
				cost = need[0][l] + std::min(need[0][r], need[1][r]);
				cost = std::min(cost, std::min(need[0][l], need[1][l]) + need[0][r]);
				if (!type[i]) cost++;
				need[0][i] = std::min(need[0][i], cost);
			}

			//true;
			//or
			if (!type[i] || ch[i])
			{
				cost = need[1][l] + std::min(need[0][r], need[1][r]);
				cost = std::min(cost, std::min(need[0][l], need[1][l]) + need[1][r]);
				if (type[i]) cost++;
				need[1][i] = std::min(need[1][i], cost);
			}

			//and
			if (type[i] || ch[i])
			{
				cost = need[1][l] + need[1][r];
				if (!type[i]) cost++;
				need[1][i] = std::min(need[1][i], cost);
			}
		}
		fout<<"Case #"<<nt<<": ";
		if (need[v][0] == INFI)
			fout<<"IMPOSSIBLE"<<std::endl;
		else
			fout<<need[v][0]<<std::endl;
	}
	fin.close();
	fout.close();
	return 0;
}

			


	
