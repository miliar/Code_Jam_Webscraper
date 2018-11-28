// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	char bf[10000];
	vector<string> dict;
	vector<set<char> > pool;
	set<char> charpool;
	int cnt = 0;
	int L,D,N;
	FILE* fin = fopen("D:\\A-small.in", "r");
	FILE* fout = fopen("D:\\a.txt", "w");

	fscanf(fin, "%d%d%d\n", &L, &D, &N);
	for (int i = 0; i < D; i++)
	{
		string buf;
		buf.clear();
		fgets(bf, 10000, fin);
		for (int kk = 0; bf[kk] != '\0' && bf[kk] != '\r' && bf[kk] != '\n'; kk++)
			buf += bf[kk];
		dict.push_back(buf);
	}
	
	for (int i = 0; i < N; i++)
	{
		string buf;
		pool.clear();
		buf.clear();
		fgets(bf, 10000, fin);
		for (int kk = 0; bf[kk] != '\0' && bf[kk] != '\r' && bf[kk] != '\n'; kk++)
			buf += bf[kk];
		
		charpool.clear();
		bool isin = false;

		for (int j = 0; j < buf.size(); j++)
		{
			switch (buf[j]) {
			case '(':
					isin = true;
					charpool.clear();
					break;
			case ')':
					pool.push_back(charpool);
					isin = false;
					break;
			default:
					charpool.insert(buf[j]);
					if (!isin)
					{
						pool.push_back(charpool);
						charpool.clear();
					}
					break;
			}
		}

		cnt = 0;
		for (int j = 0; j < D; j++)
		{
			
			bool isMatch = true;
			for (int k = 0; k < L; k++)
			{
				if (pool[k].find(dict[j][k]) == pool[k].end())
				{
					isMatch = false;
					break;
				}
			}

			if (isMatch)
			{
				cnt++;
			}			
		}
		fprintf(fout, "Case #%d: %d\n", i+1, cnt);
	}

	fclose(fin);
	fclose(fout);
	return 0;			
}

