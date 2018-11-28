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
const int MAGIC = 10007;
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

int r[2][2] = {{1,2},{2,1}};
int dp[110][110];
bool m[110][110];
int H,W,R;

void go()
{
	//queue<int> q;
	//q.push(1);q.push(1);
	//b[1][1] = true;
	//while(!q.empty())
	//{
	//	int x = q.front();q.pop();
	//	int y = q.front();q.pop();
	//	for(int i = 0; i < 2; i++)
	//	{
	//		int tx = x + r[i][0];
	//		int ty = y + r[i][1];
	//		if(tx >= 1 && ty >= 1 && tx <= H && ty <= W && !m[tx][ty])
	//		{
	//			dp[tx][ty] = (dp[tx][ty] + dp) % MAGIC;
	//			//b[tx][ty] = true;
	//		}
	//	}
	//}
	dp[1][1] = 1;
	for(int i = 1; i <= H; i++)
	{
		for(int j = 1; j <= W; j++)
		{
			for(int k = 0; k < 2; k++)
			{
				int tx = i + r[k][0];
				int ty = j + r[k][1];
				if(tx >= 1 && ty >= 1 && tx <= H && ty <= W && !m[tx][ty])
				{
					//fout << tx << "\t" << ty << endl;
					dp[tx][ty] = (dp[tx][ty] + dp[i][j]) % MAGIC;
				}
			}
		}
	}
}
int main()
{
	ofstream fout("D-small.out");
	ifstream fin("D-small.in");	
	fin >> T;
	
	for(int caseId = 1; caseId <= T; caseId++)
	{
		fin >> H >> W >> R;
		memset(dp, 0, sizeof(dp));
		dp[1][1] = 0;
		memset(m, 0, sizeof(m));
		for(int i = 0; i < R; i++)
		{
			int r, c;
			fin >> r >> c;
			m[r][c] = true;
		}
		go();
		int res = dp[H][W];
		
		fout << "Case #" << caseId << ": " << res << endl;	
	}
	return 0;
}