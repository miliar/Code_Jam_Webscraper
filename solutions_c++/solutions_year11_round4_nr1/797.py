#include "stdafx.h"
#if 1
#pragma comment(linker, "/STACK:36777216")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstring>
#include <cctype>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <list>
#include <algorithm>
#include <utility>
#include <queue>
#include <cassert>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;

#define rep(i, n) for (int i = 0; i < n; i++)
#define fori(i, b, e) for (int i = b; i < e; i++)
#define mp(x, y) make_pair(x, y)
#define sz(v) (int) ((v).size())

void solve();

int main()
{
#ifdef __USER_HOME__
	//freopen("1.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	solve();
	return 0;
}

#endif

typedef long long LL;

int X, R, S, t, N;
pair<pair<int, int>, int> a[1000];
vector<pair<int, int> > b;

void solve()
{
	int T;
	scanf("%d", &T);
	rep(tc, T)
	{
		printf("Case #%d: ", tc + 1);

		b.resize(0);
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		rep(i, N)
		{
			scanf("%d%d%d", &a[i].first.first, &a[i].first.second, &a[i].second);
			b.push_back(mp(a[i].second, a[i].first.second - a[i].first.first));
		}
		int p = 0;
		rep(i, N)
		{
			int dx = a[i].first.first - p;
			if (dx > 0)
			{
				b.push_back(mp(0, dx));
			}
			p = a[i].first.second;
		}
		if (p < X)
		{
			b.push_back(mp(0, X - p));
		}

		sort(b.begin(), b.end());
		double tRun = 0;
		double ans = 0;
		rep(i, sz(b))
		{
			if (tRun < t)
			{
				double tt = (double) b[i].second / (R + b[i].first);
				if (tRun + tt <= t)
				{
					tRun += tt;
					ans += tt;
				}
				else
				{
					tt = t - tRun;
					double s = tt * (R + b[i].first);
					tRun = t + 1.0E-6;
					ans += (tt + ((double) b[i].second - s) / (S + b[i].first));
				}
			}
			else
			{
				ans += (double) b[i].second / (S + b[i].first);
			}
		}

		printf("%.10lf\n", ans);
	}
}
