// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


/*
ID: BlackMagic
PROG: B
LANG: C++
*/
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>

using namespace std;

const int CAPACITY = 700;
const int MAXN = 500010;
const int MAGIC = 1000000007;
__int64 bucket[MAXN / CAPACITY + 1], a[MAXN];

int T;
int bitCnt(int v)
{
	return v ? 1 + bitCnt(v & (v-1)) : 0;
}

bool fileCom()
{
	ifstream fin1("A.out"), fin2("A.o");
	string s1, s2;
	for(int i = 0; i < T; i++)
	{
		getline(fin1, s1);
		getline(fin2, s2);
		if(s1 != s2)
			return false;
	}
	return true;
}

int Min(int a, int b)
{
	if(a < 0) return b;
	return a < b ? a : b;
}

bool g[10011], c[10011];
int dp[10011][2];
int M,V;

void go(int v)
{
	int sa = 2 * v;
	int sb = sa + 1;
	if(g[v])	//and
	{
		if(dp[sa][1] >= 0 && dp[sb][1] >= 0)
			dp[v][1] = Min(dp[v][1], dp[sa][1] + dp[sb][1]);

		if(dp[sa][1] >= 0 && dp[sb][0] >= 0)
			dp[v][0] = Min(dp[v][0], dp[sa][1] + dp[sb][0]);
		if(dp[sa][0] >= 0 && dp[sb][0] >= 0)
			dp[v][0] = Min(dp[v][0], dp[sa][0] + dp[sb][0]);
		if(dp[sa][0] >= 0 && dp[sb][1] >= 0)
			dp[v][0] = Min(dp[v][0], dp[sa][0] + dp[sb][1]);

		if(c[v])//or
		{
			if(dp[sa][1] >= 0 && dp[sb][1] >= 0)
				dp[v][1] = Min(dp[v][1], dp[sa][1] + dp[sb][1] + 1);
			if(dp[sa][1] >= 0 && dp[sb][0] >= 0)
				dp[v][1] = Min(dp[v][1], dp[sa][1] + dp[sb][0]+1);
			if(dp[sa][0] >= 0 && dp[sb][0] >= 0)
				dp[v][0] = Min(dp[v][0], dp[sa][0] + dp[sb][0]+1);
			if(dp[sa][0] >= 0 && dp[sb][1] >= 0)
				dp[v][1] = Min(dp[v][1], dp[sa][0] + dp[sb][1]+1);
		}
	}
	else	//or
	{
		if(dp[sa][1] >= 0 && dp[sb][1] >= 0)
			dp[v][1] = Min(dp[v][1], dp[sa][1] + dp[sb][1]);
		if(dp[sa][1] >= 0 && dp[sb][0] >= 0)
			dp[v][1] = Min(dp[v][1], dp[sa][1] + dp[sb][0]);
		if(dp[sa][0] >= 0 && dp[sb][0] >= 0)
			dp[v][0] = Min(dp[v][0], dp[sa][0] + dp[sb][0]);
		if(dp[sa][0] >= 0 && dp[sb][1] >= 0)
			dp[v][1] = Min(dp[v][1], dp[sa][0] + dp[sb][1]);
		if(c[v])//and
		{
			if(dp[sa][1] >= 0 && dp[sb][1] >= 0)
				dp[v][1] = Min(dp[v][1], dp[sa][1] + dp[sb][1]+1);

			if(dp[sa][1] >= 0 && dp[sb][0] >= 0)
				dp[v][0] = Min(dp[v][0], dp[sa][1] + dp[sb][0]+1);
			if(dp[sa][0] >= 0 && dp[sb][0] >= 0)
				dp[v][0] = Min(dp[v][0], dp[sa][0] + dp[sb][0]+1);
			if(dp[sa][0] >= 0 && dp[sb][1] >= 0)
				dp[v][0] = Min(dp[v][0], dp[sa][0] + dp[sb][1]+1);
		}
	}
}
int main()
{
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");	
	fin >> T;
	
	for(int caseId = 1; caseId <= T; caseId++)
	{
		int res = 0;
		fin >> M >> V;
		memset(dp, -1, sizeof(dp));
		for(int i = 0; i < (M-1)/2; i++)
		{
			int tg,tc;
			fin >> tg >> tc;
			g[i+1] = tg;
			c[i+1] = tc;
			//fout << g[i+1] << "\t" << c[i+1] << endl;
		}
		for(int i = 0; i < (M+1)/2; i++)
		{
			int tg; fin >> tg;
			g[i+(M+1)/2] = tg;
			dp[i+(M+1)/2][(int)tg] = 0;
		}
		
		for(int i = (M-1)/2; i >= 1; i--)
		{
			//fout << i << "\t" << dp[i][0] << "\t" << dp[i][1] << endl;
			go(i);
		}
		if(dp[1][V] >= 0)
			fout << "Case #" << caseId << ": " << dp[1][V] << endl;	
		else
			fout << "Case #" << caseId << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}