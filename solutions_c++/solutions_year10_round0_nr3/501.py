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

const int nmax = 2010;

int a[nmax];
int next[nmax];
long long s[nmax];

void solveTest()
{
	int R, k, n;
	scanf("%d%d%d", &R, &k, &n);
	int i;
	for(i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);
	}
	for(i = 0; i < n; ++i)
	{
		long long cs = a[i];
		int j;
		for(j = (i + 1) % n; j != i; j = (j + 1) % n)
		{
			if (cs + a[j] > k)
			{
				break;
			}
			cs += a[j];
		}
		next[i] = j;
		s[i] = cs;
	}

	long long ans = 0LL;
	int x = 0;
	for(i = 0; i < R; ++i)
	{
		ans += s[x];
		x = next[x];
	}
	printf("%lld\n", ans);
}

int main()
{
	int t;
	int i;
	freopen("C.txt", "r", stdin);
	freopen("C_out_large.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solveTest();
	}
	return 0;
}
