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

const int nmax = 100;

char a[nmax][nmax];
int n;

void rotate()
{
	int i, j;
	for(i = 0; i < (n >> 1); ++i)
	{
		for(j = 0; j < n; ++j)
		{
			swap(a[i][j], a[n - i - 1][j]);
		}
	}
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < i; ++j)
		{
			swap(a[i][j], a[j][i]);
		}
	}
}

void drop()
{
	int i, j;
	for(j = 0; j < n; ++j)
	{
		int p = n - 1;
		char x;
		for(i = n - 1; i >= 0; --i)
		{
			x = a[i][j];
			a[i][j] = '.';
			if (x != '.')
			{
				a[p][j] = x;
				--p;
			}
		}
	}
}

int d[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int maxInRow(char what, int K)
{
	int i, j, k, kx, ky;
	int ans = 0;
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < n; ++j)
		{
			if (a[i][j] == what)
			{
				for(k = 0; k < 8; ++k)
				{
					int t = 1;
					kx = i + d[k][0];
					ky = j + d[k][1];
					while(	kx >= 0 && kx < n &&
							ky >= 0 && ky < n &&
							a[kx][ky] == what)
					{
						++t;
						kx += d[k][0];
						ky += d[k][1];
					}
					ans = max(ans, t);
				}
			}
		}
	}
	return ans >= K;
}

void solveTest()
{
	int k;
	scanf("%d%d", &n, &k);
	int i, j;
	for(i = 0; i < n; ++i)
	{
		scanf("%s", &a[i]);
	}
	rotate();
	drop();
	int ans = (maxInRow('R', k) << 1) | maxInRow('B', k);
	switch(ans)
	{
		case 0: printf("Neither\n"); break;
		case 1: printf("Blue\n"); break;
		case 2: printf("Red\n"); break;
		case 3: printf("Both\n"); break;
	}
}

int main()
{
	int t;
	int i;
	freopen("A.txt", "r", stdin);
	freopen("A_out_large.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solveTest();
	}
	return 0;
}
