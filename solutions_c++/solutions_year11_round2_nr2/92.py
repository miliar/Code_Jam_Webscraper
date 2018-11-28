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

long long mabs(long long x)
{
	if (x < 0LL)
	{
		return -x;
	}
	return x;
}

const int nmax = 1 << 20;

int a[nmax];
int d;
int n;

bool can(long long t)
{
	long long L = a[0] - t, g;
	for(int i = 1; i < n; ++i)
	{
		g = max(a[i] - t, L + d);
		if (mabs(a[i] - g) > t)
		{
			return false;
		}
		L = g;
	}
	return true;
}

void solveTest()
{
	int c;
	scanf("%d%d", &c, &d);
	n = 0;
	for(int i = 0; i < c; ++i)
	{
		int p, v;
		scanf("%d%d", &p, &v);
		for(int j = 0; j < v; ++j)
		{
			a[n] = 2 * p;
			++n;
		}
	}
	d *= 2;
	long long L = 0;
	long long R = 10000000000000LL;
	long long M;
	for(int i = 0; i < 512; ++i)
	{
		M = (L + R) >> 1;
		if (can(M))
		{
			R = M;
		}
		else
		{
			L = M;
		}
	}
	if (can(L))
	{
		M = L;
	}
	else
	{
		M = R;
	}
	char buf[100];
	sprintf(buf, "%.9lf", (double)(M % 2) / 2.0);
	printf("%lld%s\n", M / 2, buf + 1);
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
