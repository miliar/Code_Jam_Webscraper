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

const int nmax = 1000;
const int vmax = 256;

int a[nmax][vmax];
int c[nmax];

void solveTest()
{
	int del, ins, m, n;
	scanf("%d%d%d%d", &del, &ins, &m, &n);
	int i, j;
	for(i = 0; i < n; ++i)
	{
		scanf("%d", &c[i]);
	}
	int diff, comp, val;
	int k, p;
	memset(a, 127, sizeof(a));
	for(k = 0; k < vmax; ++k)
	{
		a[0][k] = abs(k - c[0]);
	}
	for(i = 1; i < n; ++i)
	{
		for(k = 0; k < vmax; ++k)
		{
			for(j = 0; j < i; ++j)
			{
				for(p = 0; p < vmax; ++p)
				{
					diff = abs(k - p);
					if (m == 0)
					{
						if (diff == 0)
						{
							a[i][k] = min(a[i][k], a[j][p] + (i - j - 1) * del + abs(k - c[i]));
						}
					}
					else
					{
						comp = diff / m;
						if (comp && (diff % m == 0))
						{
							--comp;
						}

						a[i][k] = min(a[i][k], a[j][p] + (i - j - 1) * del + comp * ins + abs(k - c[i]));
					}
				}
			}
		}
	}
	int ans = del * n;
	for(i = n - 1; i >= 0; --i)
	{
		for(j = 0; j < vmax; ++j)
		{
			ans = min(ans, a[i][j] + del * (n - i - 1));
		}
	}
	printf("%d\n", ans);
}

int main()
{
	int t;
	int i;
	freopen("B.txt", "r", stdin);
	freopen("B_out_new.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solveTest();
	}
	return 0;
}
