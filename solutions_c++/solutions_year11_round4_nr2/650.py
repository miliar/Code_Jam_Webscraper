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
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
#endif
	solve();
	return 0;
}

#endif

typedef long long LL;

int R, C, D;
char tmp[1000][1000];
int w[500][500];

bool can(int lx, int ly, int k)
{
	if (k % 2 == 0)
	{
		double cx = lx + k / 2 - 0.5;
		double cy = ly + k / 2 - 0.5;
		double sx = 0, sy = 0;

		for (int i = lx; i < lx + k; i++)
		{
			for (int j = ly; j < ly + k; j++)
			{
				if (i == lx && j == ly)
					continue;
				if (i == lx && j == ly + k - 1)
					continue;
				if (i == lx + k - 1 && j == ly)
					continue;
				if (i == lx + k - 1 && j == ly + k - 1)
					continue;

				sx += w[i][j] * (cx - i);
				sy += w[i][j] * (cy - j);
			}
		}
		return fabs(sx) < 1.0E-6 && fabs(sy) < 1.0E-6;

	}
	else
	{
		int cx = lx + k / 2;
		int cy = ly + k / 2;
		int sx = 0, sy = 0;
		for (int i = lx; i < lx + k; i++)
		{
			for (int j = ly; j < ly + k; j++)
			{
				if (i == lx && j == ly)
					continue;
				if (i == lx && j == ly + k - 1)
					continue;
				if (i == lx + k - 1 && j == ly)
					continue;
				if (i == lx + k - 1 && j == ly + k - 1)
					continue;
				sx += w[i][j] * (cx - i);
				sy += w[i][j] * (cy - j);
			}
		}
		return (sx == 0) && (sy == 0);
	}
}

void solve()
{
	int T;
	scanf("%d", &T);
	rep(tc, T)
	{
		printf("Case #%d: ", tc + 1);

		scanf("%d%d%d", &R, &C, &D);
		gets(tmp[0]);
		rep(i, R)
		{
			gets(tmp[i]);
		}
		rep(i, R)
		{
			rep(j, C)
			{
				w[i][j] = D + tmp[i][j] - '0';
			}
		}

		int ans = 0;
		rep(i, R)
		{
			rep(j, C)
			{
				int maxK = min(R - i, C - j);
				for (int k = max(ans, 3); k <= maxK; k++)
				{
					if (can(i, j, k))
					{
						ans = max(ans, k);
					}
				}
			}
		}

		if (ans == 0)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
}
