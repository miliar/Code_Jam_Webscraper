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

const int MAXN = 210;
int bitCnt(int v)
{
	return v ? 1 + bitCnt(v & (v-1)) : 0;
}

int main()
{
	ofstream fout("B-small.out");
	ifstream fin("B-small.in");
	int T,N,M,temp;
	fin >> T;
	
	vector< map<int, int> > vi;
	for(int caseId = 1; caseId <= T; caseId++)
	{
		fin >> N >> M;
		vi.clear();
		vi.resize(M);
		for(int i = 0; i < M; i++)
		{
			int cnt;
			fin >> cnt;
			for(int j = 0; j < cnt; j++)
			{
				int a,b;
				fin >> a >> b;
				vi[i].insert(make_pair(a-1,b));
			}
		}
		int res = 0;
		int minR = 1000000;
		for(int i = 0;  i < (1 << N); i++)
		{
			bool flag = true;
			for(int j = 0; flag && j < M; j++)
			{
				int satify = 0;
				for(int k = 0; k < N; k++)
				{					
					if(vi[j].find(k) != vi[j].end())
					{
						int s = (int)((i & (1 << k)) != 0);
						if(vi[j].find(k)->second == s)
							satify++;
					}
				}
				if(!satify) flag = false;
			}
			if(flag)
			{
				int cnt = bitCnt(i);
				if(cnt < minR)
				{
					res = i;
					minR = cnt;
				}
			}
		}
		if(minR < 1000000)
		{			
			fout << "Case #" << caseId << ": " ;
			for(int x = 0; x < N-1; x++)
				if((1 << x) & res)
					fout << 1 << " ";
				else
					fout << 0 << " ";
			if((1 << (N-1)) & res)
				fout << 1 << endl;
			else
				fout << 0 << endl;
		}
		else
		{
			fout << "Case #" << caseId << ": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}

