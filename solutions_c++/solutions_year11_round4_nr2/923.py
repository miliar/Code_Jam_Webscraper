#define _CRT_SECURE_NO_DEPRECATE

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
#include <numeric>

using namespace std;

#define INF (2000000000)

#pragma comment(linker, "/STACK:167772160")

const int nmax = 100;

int a[nmax][nmax];
int n, m, d;

bool cent(int x, int y, int k)
{
	if (x + k > n &&
		y + k > m)
	{
		return false;
	}

	int cx = 0;
	int cy = 0;

	int s = 0;
	int pp = 0;
	for(int i = 0; i < k; ++i)
	{
		for(int j = 0; j < k; ++j)
		{
			if (i == 0 && j == 0)
			{
				continue;
			}
			if (i == 0 && j == k - 1)
			{
				continue;
			}
			if (i == k - 1 && j == 0)
			{
				continue;
			}
			if (i == k - 1 && j == k - 1)
			{
				continue;
			}
			cx += a[i + x][j + y] * i;
			cy += a[i + x][j + y] * j;
			s += a[i + x][j + y];
			++pp;
		}
	}
	return	2 * cx == s * (k - 1) &&
			2 * cy == s * (k - 1);
}

void solveTest()
{
	char buf[nmax];
	scanf("%d%d%d\n", &n, &m, &d);
	for(int i = 0; i < n; ++i)
	{
		gets(buf);
		for(int j = 0; j < m; ++j)
		{
			a[i][j] = buf[j] - '0' + d;
		}
	}
	int best = -1;
	for(int k = max(n, m); k >= 3; --k)
	{
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j)
			{
				if (cent(i, j, k))
				{
					best = k;
					i = n;
					k = -1;
					break;
				}
			}
		}
	}
	if (best == -1)
	{
		puts("IMPOSSIBLE");
	}
	else
	{
		printf("%d\n", best);
	}
}

int main()
{
	int t;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solveTest();
		cerr << i + 1 << " Done!\n";
	}
	return 0;
}
