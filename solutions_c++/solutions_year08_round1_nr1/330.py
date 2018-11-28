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

int main()
{
	ofstream fout("A-small.out");
	ifstream fin("A-small.in");
	int T,N,temp;
	fin >> T;
	vector<int> va,vb;
	for(int caseId = 1; caseId <= T; caseId++)
	{
		fin >> N;
		va.clear(), vb.clear();
		for(int i = 0; i < N; i++)
		{
			fin >> temp;
			va.push_back(temp);
		}
		for(int i = 0; i < N; i++)
		{
			fin >> temp;
			vb.push_back(temp);
		}
		sort(va.begin(),va.end());
		sort(vb.begin(), vb.end());
		__int64 res = 0;
		for(int i = 0; i < N; i++)
			res += va[i] * vb[N-1-i];
		fout << "Case #" << caseId << ": " << res << endl;
	}
	return 0;
}

