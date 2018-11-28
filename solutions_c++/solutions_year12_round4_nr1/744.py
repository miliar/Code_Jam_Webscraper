/*
 * $File: prog.cc
 * $Date: Sat May 26 22:39:36 2012 +0800
 * $Author: jiakai <jia.kai66@gmail.com>
 */

// f{{{ 

#include <stdint.h>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <limits>

#define ITER_VECTOR(v, var) \
	for (typeof((v).begin()) var = (v).begin(); var != (v).end(); var ++)

#define ITER_VECTOR_IDX(v, var) \
	for (typeof((v).size()) var = 0; var < (v).size(); var ++)

using namespace std;

// f}}}

namespace Solve
{
	struct Vine
	{
		int dist, len,
			reach_max;

		Vine(int d = 0, int l = 0):
			dist(d), len(l)
		{}
		inline bool operator < (const Vine &v) const
		{ return dist < v.dist; }
	};
	vector<Vine> vines;

	bool work();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		vines.clear();
		int n;
		fscanf(fin, "%d", &n);
		while (n --)
		{
			vines.push_back(Vine());
			fscanf(fin, "%d%d", &vines.back().dist, &vines.back().len);
		}
		int d;
		fscanf(fin, "%d", &d);
		vines.push_back(Vine(d, 0));
		fprintf(fout, "Case #%d: %s\n", casenu, work() ? "YES" : "NO");
	}
}

bool Solve::work()
{
	vines.push_back(Vine(0, 0));
	sort(vines.begin(), vines.end());
	vines[0].len = vines[1].dist;
	vines.back().reach_max = vines.size();
	for (int i = vines.size() - 2; i >= 0; i --)
	{
		int l0 = vines[i].len, d0 = vines[i].dist, r = -2, j = i + 1,
			b = i - 1, tdist;
		while (j < (int)vines.size() && (tdist = vines[j].dist - d0) <= l0)
		{
			while (b >= 0 && d0 - vines[b].dist < tdist)
				b --;
			if (vines[j].reach_max >= i)
			{
				r = b;
				break;
			}
			j ++;
		}
		vines[i].reach_max = r;
	}
	return vines[0].reach_max != -2;
}

// f{{{ main
int main()
{
#if defined(INPUT) && defined(OUTPUT) && !defined(STDIO) && !defined(ONLINE_JUDGE)
	FILE *fin = fopen(INPUT, "r"),
		 *fout = fopen(OUTPUT, "w");
	Solve::solve(fin, fout);
	fclose(fin);
	fclose(fout);
#else
	Solve::solve(stdin, stdout);
#endif
}
// f}}}
// vim: filetype=cpp foldmethod=marker foldmarker=f{{{,f}}}

