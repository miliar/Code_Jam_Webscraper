/*
 * $File: b.cpp
 * $Date: Sat Jun 05 22:44:46 2010 +0800
 */

#include <cstdio>
#include <cstring>

namespace Solve
{
	const int NMATCH_MAX = 2050, DEP_MAX = 15, INF = (1 << 30) - 1;
	inline int min(int a, int b)
	{return a < b ? a : b;}
	int f[NMATCH_MAX][DEP_MAX], price[NMATCH_MAX], min_watch[NMATCH_MAX],
		leaf_start;
	bool f_done[NMATCH_MAX][DEP_MAX];
	int calc_f(int vtx, int al);

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		memset(f_done, 0, sizeof(f_done));
		int p;
		fscanf(fin, "%d", &p);
		leaf_start = (1 << (p - 1)) - 1;
		for (int i = 0; i < (1 << p); i += 2)
		{
			int a, b;
			fscanf(fin, "%d%d", &a, &b);
			if (b < a)
				a = b;
			a = p - a;
			if (a < 0)
				a = 0;
			min_watch[leaf_start + (i >> 1)] = a;
		}
		for (int s = leaf_start, i = p - 1; i >= 0; i --)
		{
			for (int j = 0; j < (1 << i); j ++)
				fscanf(fin, "%d", &price[s + j]);
			s = (s - 1) >> 1;
		}
		fprintf(fout, "Case #%d: %d\n", id, calc_f(0, 0));
	}
}

int Solve::calc_f(int vtx, int al)
{
	if (f_done[vtx][al])
		return f[vtx][al];
	f_done[vtx][al] = true;
	int &ans = f[vtx][al];
	if (vtx >= leaf_start)
	{
		if (al >= min_watch[vtx])
			return ans = 0;
		if (al == min_watch[vtx] - 1)
			return ans = price[vtx];
		return ans = INF;
	}
	int chl = vtx * 2 + 1, chr = vtx * 2 + 2;
	ans = calc_f(chl, al + 1) + calc_f(chr, al + 1);
	if (ans < INF)
		ans += price[vtx];
	ans = min(ans, calc_f(chl, al) + calc_f(chr, al));
	if (ans > INF)
		ans = INF;
	return ans;
}

int main()
{
	Solve::solve(stdin, stdout);
}

