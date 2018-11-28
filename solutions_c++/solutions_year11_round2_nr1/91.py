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

#pragma comment(linker, "/STACK:16777216")

const int nmax = 1 << 7;

int a[nmax][nmax];
double d[3][nmax];

void solveTest()
{
	int n;
	memset(a, -1, sizeof(a));
	scanf("%d", &n);
	char c;
	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			cin >> c;
			if (c == '0')
			{
				a[i][j] = 0;
			}
			if (c == '1')
			{
				a[i][j] = 1;
			}
		}
	}
	memset(d, 0, sizeof(d));
	for(int i = 0; i < n; ++i)
	{
		int cnt = 0;
		int w = 0;
		for(int j = 0; j < n; ++j)
		{
			if (a[i][j] != -1)
			{
				++cnt;
			}
			if (a[i][j] == 1)
			{
				++w;
			}
		}
		d[0][i] = (double)w / cnt;
	}

	for(int i = 0; i < n; ++i)
	{
		int cnt = 0;
		double s = 0;
		for(int j = 0; j < n; ++j)
		{
			if (a[i][j] != -1)
			{
				int w = 0;
				int ccnt = 0;
				for(int k = 0; k < n; ++k)
				{
					if (a[j][k] != -1 && k != i)
					{
						++ccnt;
						if (a[j][k] == 1)
						{
							++w;
						}
					}

				}
				++cnt;
				s += (double)w / ccnt;
			}
		}
		d[1][i] = s / cnt;
	}

	for(int i = 0; i < n; ++i)
	{
		int cnt = 0;
		double s = 0;
		for(int j = 0; j < n; ++j)
		{
			if (a[i][j] != -1)
			{
				++cnt;
				s += d[1][j];
			}
		}
		d[2][i] = s / cnt;
	}

	for(int i = 0; i < n; ++i)
	{
		double ans = 0.25 * d[0][i] + 0.5 * d[1][i] + 0.25 * d[2][i];
		printf("%.9lf\n", ans);
	}
}

int main()
{
	int t;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d:\n", i + 1);
		solveTest();
		cerr << i + 1 << " Done!\n";
	}
	return 0;
}
