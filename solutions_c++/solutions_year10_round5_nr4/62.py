/*
 * $File: d_force.cpp
 * $Date: Sun Jun 13 00:13:53 2010 +0800
 */

#include <cstdio>
#include <cstring>

namespace Solve
{
	int ans, base;
	bool used[10][11];
	void dfs(int min, int remain) __attribute__ ((fastcall));

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase = 0;
	fscanf(fin, "%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		int n, b;
		fscanf(fin, "%d%d", &n, &b);
		ans = 0;
		memset(used, 0, sizeof(used));
		base = b;
		dfs(1, n);
		fprintf(fout, "Case #%d: %d\n",id, ans);
	}
}

void Solve::dfs(int min, int remain)
{
	if (!remain)
	{
		ans ++;
		return;
	}
	for (int i = min; i <= remain; i ++)
	{
		bool ok = true;
		for (int p = 0, x = i, t; x; x /= base, p ++)
			if (used[p][t = x % base])
			{
				ok = false;
				break;
			}
		if (!ok)
			continue;
		for (int p = 0, x = i; x; x /= base, p ++)
			used[p][x % base] = true;
		dfs(i + 1, remain - i);
		for (int p = 0, x = i; x; x /= base, p ++)
			used[p][x % base] = false;
	}
}

int main()
{
	Solve::solve(stdin, stdout);
}

