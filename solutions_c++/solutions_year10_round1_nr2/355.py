/*
 * $File: smooth.cpp
 * $Date: Sat May 22 10:58:50 2010 +0800
 */
#include <cstdio>
#include <cmath>

namespace Solve
{
	const int INF = 1 << 28;
	inline int abs(int x)
	{return x >= 0 ? x : -x;}
	inline int min(int a, int b)
	{return a < b ? a : b;}
	const int SEQLEN_MAX = 105;
	int seq[SEQLEN_MAX], seqlen, cost_d, cost_i, max_dist;
	int f[2][256];
	inline int get_insert_cost(int s0, int t);
	int work();

	int s1[10], ns1, check_ans, best_s1[10], best_ns1;
	void check(int pos, int cost);

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int t;
	fscanf(fin, "%d", &t);
	for (int id = 1; id <= t; id ++)
	{
		fscanf(fin, "%d%d%d%d", &cost_d, &cost_i, &max_dist, &seqlen);
		for (int i = 0; i < seqlen; i ++)
			fscanf(fin, "%d", &seq[i]);
		int ans;
		check_ans = INF;
		check(0, 0);
		fprintf(fout, "Case #%d: %d\n", id, check_ans);
		/*
		if (check_ans != ans)
		{
			fprintf(stderr, "D=%d I=%d M=%d N=%d A={%d", cost_d, cost_i, max_dist, seqlen, seq[0]);
			for (int i = 1; i < seqlen; i ++)
				fprintf(stderr, ", %d", seq[i]);
			fprintf(stderr, "}\nans=%d check_ans=%d\nMethod: ", ans, check_ans);
			for (int i = 0; i < best_ns1; i ++)
				fprintf(stderr, "%d ", best_s1[i]);
			fprintf(stderr, "\n");
		}
		*/
	}
}

void Solve::check(int pos, int cost)
{
	if (pos == seqlen)
	{
		for (int i = 1; i < ns1; i ++)
		{
			int d = abs(s1[i] - s1[i - 1]);
			if (d > 0 && max_dist == 0)
				return;
			if (d <= max_dist)
				continue;
			cost += cost_i * ((int)ceil(double(d) / max_dist) - 1);
		}
		if (cost < check_ans)
		{
			check_ans = cost;
			best_ns1 = ns1;
			for (int i = 0; i < ns1; i ++)
				best_s1[i] = s1[i];
		}
		return;
	}
	check(pos + 1, cost + cost_d);
	for (int i = 0; i < 256; i ++)
	{
		s1[ns1 ++] = i;
		check(pos + 1, cost + abs(i - seq[pos]));
		ns1 --;
	}
}

int Solve::work()
{
	for (int i = 0; i < 256; i ++)
		f[0][i] = min(abs(i - seq[0]), min(get_insert_cost(seq[0], i), cost_d + cost_i));
	int cur = 0;
	for (int i = 1; i < seqlen; i ++)
	{
		int prev = cur;
		cur ^= 1;
		static int cost_chg[256];
		for (int j = 0; j < 256; j ++)
		{
			int ans = INF;
			for (int j1 = 0; j1 < 256; j1 ++)
				if (abs(j - j1) <= max_dist)
					ans = min(ans, f[prev][j1] + abs(seq[i] - j));
			cost_chg[j] = ans;
		}
		for (int j = 0; j < 256; j ++)
		{
			int ans = min(f[prev][j] + cost_d, cost_chg[j]);
			for (int j1 = 0; j1 < 256; j1 ++)
			{
				if (abs(seq[i] - j1) <= max_dist)
					ans = min(ans, f[prev][j1] + get_insert_cost(seq[i], j));
				if (abs(j - j1) <= max_dist)
				{
					ans = min(ans, cost_chg[j1] + get_insert_cost(j1, j));
					ans = min(ans, f[prev][j1] + abs(j - seq[i]));
				}
			}
			f[cur][j] = ans;
		}
	}
	int ans = f[cur][0];
	for (int i = 1; i < 256; i ++)
		ans = min(ans, f[cur][i]);
	return ans;
}

int Solve::get_insert_cost(int s0, int t)
{
	if (s0 == t)
		return 0;
	int d = abs(s0 - t);
	if (max_dist == 0)
		return d == 0 ? 0 : INF;
	return ((d - 1) / max_dist + 1) * cost_i;
}

int main()
{
	Solve::solve(stdin, stdout);
}

