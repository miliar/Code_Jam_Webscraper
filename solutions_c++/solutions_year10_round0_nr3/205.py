#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <cmath>

#include <cstdarg>

#pragma comment(linker,"/STACK:128000000")

#define DBG1
#define DBG2 1

void dbg(const char * fmt, ...)
{
#ifdef DBG1
#if DBG2
	va_list args;
	va_start(args, fmt);
	vfprintf(stderr, fmt, args);
	va_end(args);

	fflush(stderr);
#endif
#endif
}

using namespace std;

#define clr(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))

#define TASKNAME ""

typedef long long ll;
typedef unsigned long long ull;

typedef pair<int,int> pii;

const int N = 2048;

int next[N];
int sum[N];
int a[N];


int main()
{
#ifdef DBG1
#if DBG2
//	freopen(TASKNAME ".in", "r", stdin);
	freopen(TASKNAME ".out", "w", stdout);
	freopen(TASKNAME ".err", "w", stderr);
#endif
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		printf("Case #%d: ", ii);
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);

		for (int i = 0; i < n; ++i)
		{
			int j = (i + 1) % n;
			sum[i] = a[i];
			while (j != i && sum[i] + a[j] <= k)
			{
				sum[i] += a[j];
				j = (j + 1) % n;
			}

			next[i] = j;
		}

		ll res = 0;
		int cur = 0;
		for (int i = 0; i < r; ++i)
		{
			res += sum[cur];
			cur = next[cur];
		}

		printf("%I64d\n", res);
	}


	return 0;
}