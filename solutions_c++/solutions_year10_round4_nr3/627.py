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

const int nmax = 200;

int a[nmax][nmax];
int b[nmax][nmax];

bool has()
{
	int i, j;
	for(i = 0; i < nmax; ++i)
	{
		for(j = 0; j < nmax; ++j)
		{
			if (a[i][j])
			{
				return true;
			}
		}
	}
	return false;
}

void simulate()
{
	memcpy(b, a, sizeof(b));
	int i, j;
	for(i = 1; i < nmax; ++i)
	{
		for(j = 1; j < nmax; ++j)
		{
			if (a[i - 1][j] && a[i][j - 1])
			{
				b[i][j] = 1;
			}
			if (a[i - 1][j] == 0 && a[i][j - 1] == 0)
			{
				b[i][j] = 0;
			}
		}
	}
	memcpy(a, b, sizeof(b));
}

void solveTest()
{
	int r;
	int i, j;
	int x1, x2, y1, y2;
	scanf("%d", &r);
	int k;
	memset(a, 0, sizeof(a));
	for(i = 0; i < r; ++i)
	{
		scanf("%d%d", &x1, &y1);
		scanf("%d%d", &x2, &y2);
		for(j = x1; j <= x2; ++j)
		{
			for(k = y1; k <= y2; ++k)
			{
				a[j][k] = 1;
			}
		}
	}
	int ans = 0;
	while(has())
	{
		simulate();
		++ans;
	}
	printf("%d\n", ans);
}

int main()
{
	int t;
	int i;
	freopen("C.txt", "r", stdin);
	freopen("C_out_tt.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		cerr << i + 1 << " Done!\n";
		solveTest();
	}
	return 0;
}
