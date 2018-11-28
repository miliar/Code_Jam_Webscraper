#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <cctype>
#include <cassert>

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair

typedef long long li;
typedef pair<int, int> pt;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const ld PI = 2 * acos(0.0);
const ld EPS = 1e-9;
const int N = 105;

bool a[2][N][N];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int test;
	scanf("%d", &test);
	for1(itm, test)
	{
		int k;
		scanf("%d", &k);

		memset(a, 0, sizeof a);

		forn(i, k)
		{
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int x = x1; x <= x2; ++x)
				for(int y = y1; y <= y2; ++y)
					a[1][x][y] = 1;
		}

		int tm = 0;
		bool found = true;
		while(found)
		{
			found = false;
			int cur = tm % 2;
			int prev = 1 - cur;
			memset(a[cur], 0, sizeof a[cur]);
			for1(i, N - 1)
			{
				for1(j, N - 1)
				{
					if(a[prev][i][j])
					{
						if(a[prev][i - 1][j] || a[prev][i][j - 1])
						{
							found = true;
							a[cur][i][j] = 1;
						}
					}
					else if(a[prev][i - 1][j] && a[prev][i][j - 1])
					{
						found = true;
						a[cur][i][j] = 1;
					}
				}
			}
			++tm;
		}

		printf("Case #%d: %d\n", itm, tm);
	}

	

	return 0;
}
