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

const int nmax = 2000;

int m[nmax];
int c[20][nmax];

int f(int L, int R, int d)
{
	int i;
	int ans = 0;
	bool g = false;
	for(i = L; i < R; ++i)
	{
		if (m[i] - d > 0)
		{
			g = true;
			break;
		}
	}
	if (g)
	{
		ans = 1;
		ans += f(L, (L + R) >> 1, d + 1);
		ans += f((L + R) >> 1, R, d + 1);
	}
	return ans;
}

void solveTest()
{
	int p;
	scanf("%d", &p);
	int n = 1 << p;
	int i, j;
	for(i = 0; i < n; ++i)
	{
		scanf("%d", &m[i]);
		m[i] = p - m[i];
	}
	int lim = n;
	for(j = 0; j < p; ++j)
	{
		lim >>= 1;
		for(i = 0; i < lim; ++i)
		{
			scanf("%d", &c[j][i]);
		}
	}
	printf("%d\n", f(0, n, 0));
}

int main()
{
	int t;
	int i;
	freopen("B.txt", "r", stdin);
	freopen("B_out.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		cerr << i + 1 << " Done!\n";
		solveTest();
	}
	return 0;
}
