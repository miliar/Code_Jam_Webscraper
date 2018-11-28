#include "stdafx.h"

#include <vector>
#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

void solve(FILE* fin, FILE* fout)
{
	int m,n;
	fscanf(fin, "%d%d", &m, &n);

	vector<vector<pair<int,int>>> cs;
	for (int i = 0; i < n; ++i)
	{
		int x;
		fscanf(fin, "%d", &x);
		cs.push_back(vector<pair<int,int>>());
		for (int j = 0; j < x; ++j)
		{
			int a,b;
			fscanf(fin, "%d%d", &a, &b);
			cs.back().push_back(make_pair(a-1,b));
		}
	}

	int ans = -1;
	for (int i = 0; i < (1<<m); ++i)
	{
		bool ok = true;
		for (int j = 0; j < n; ++j)
		{
			bool good = false;
			for (int k = 0; k < cs[j].size(); ++k)
			{
				int q = (i>>cs[j][k].first)&1;
				if (q == cs[j][k].second)
				{
					good = true;
					break;
				}
			}
			if (!good)
			{
				ok = false;
				break;
			}
		}
		if (ok) { ans = i; break; }
	}
	if (ans == -1)
	{
		fprintf(fout, " IMPOSSIBLE\n");
	}
	else
	{
		//printf("%d\n", ans);
		for (int i = 0; i < m; ++i)
		{
			fprintf(fout, " %d", (ans&1<<i) != 0);
		}
		fprintf(fout, "\n");
	}
}

int main()
{
	FILE *fin, *fout;
	fin = fopen("B.in", "rt");
	fout = fopen("B.out", "wt");

	int c;
	fscanf(fin, "%d", &c);

	for (int i = 1; i <= c; ++i)
	{
		fprintf(fout, "Case #%d: ", i);
		solve(fin, fout);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}
