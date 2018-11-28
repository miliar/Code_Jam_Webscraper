#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define INF (2000000000)

const int nmax = 100;

const int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int p[nmax][nmax][2];
int a[nmax][nmax];
int r[nmax][nmax];
bool b[nmax][nmax];
char c[nmax];
int n, m;

void dfs(int x, int y, int cl)
{
	int k, kx, ky;
	b[x][y] = true;
	r[x][y] = cl;
	for(k = 0; k < 4; ++k)
	{
		kx = x + d[k][0];
		ky = y + d[k][1];
		if (kx >= 0 && kx < n &&
			ky >= 0 && ky < m &&
			p[kx][ky][0] == x &&
			p[kx][ky][1] == y && !b[kx][ky])
		{
			dfs(kx, ky, cl);
		}
	}
}

void solve()
{
	int i, j;
	scanf("%d%d", &n, &m);
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < m; ++j)
		{
			scanf("%d", &a[i][j]);
		}
	}

	int k, mn, kx, ky, im;

	vector<pair<int, int> > vp;
	memset(p, -1, sizeof(p));
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < m; ++j)
		{
			mn = INF;
			for(k = 0; k < 4; ++k)
			{
				kx = i + d[k][0];
				ky = j + d[k][1];
				if (kx >= 0 && kx < n &&
					ky >= 0 && ky < m)
				{
					if (a[kx][ky] < mn)
					{
						mn = a[kx][ky];
						im = k;
					}
				}
			}
			if (mn >= a[i][j])
			{
				vp.push_back(make_pair(i, j));
			}
			else
			{
				p[i][j][0] = i + d[im][0];
				p[i][j][1] = j + d[im][1];
			}

		}
	}
	memset(b, 0, sizeof(b));
	for(i = 0; i < (int)vp.size(); ++i)
	{
		dfs(vp[i].first, vp[i].second, i);
	}
	memset(c, -1, sizeof(c));
	char cl = 'a';
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < m; ++j)
		{
			if (c[r[i][j]] == -1)
			{
				c[r[i][j]] = cl;
				++cl;
			}
		}
	}

	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < m; ++j)
		{
			if (j)
			{
				printf(" ");
			}
			printf("%c", c[r[i][j]]);
		}
		printf("\n");
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i, t;
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d:\n", i + 1);
		solve();
	}
	return 0;
}