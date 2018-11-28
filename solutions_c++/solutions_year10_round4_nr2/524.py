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

#define DBG2 1

void dbg(const char * fmt, ...)
{
#ifdef DBG1
#if DBG2
	va_list args;
	va_start(args, fmt);
	vfprintf(stderr, fmt, args);
	va_end(args);
#endif
#endif
}

#ifdef DBG1
#define LL "%I64d"
#else
#define LL "%lld"
#endif


using namespace std;

#define clr(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))

#define TASKNAME ""

typedef long long ll;
typedef unsigned long long ull;

typedef pair<int,int> pii;

const int INF = 1 << 29;
const int N = 12;

int dp[1 << N][N];
int cost[1 << N];
int m[1 << N];
int p;

int getMin(int x, int y)
{
	int res = INF;
	for (int i = y; i <= p; ++i)
		res = min(res, dp[x][i]);
	return res;
}

int main()
{
	freopen(TASKNAME "input.txt", "r", stdin);
	freopen(TASKNAME "output.txt", "w", stdout);


#ifdef DBG1
#if DBG2

	freopen(TASKNAME ".err", "w", stderr);
#endif
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		scanf("%d", &p);
		int n = 1 << p;
		for (int i = 0; i < n; ++i)
			scanf("%d", &m[i + n]);

		for (int i = p - 1; i >= 0; --i)
		{
			for (int j = 0; j < (1 << i); ++j)
				scanf("%d", &cost[(1 << i) + j]);
		}

		for (int i = n - 1; i > 0; --i)
			m[i] = min(m[2 * i], m[2 * i + 1]);

		for (int i = 0; i < n; ++i)
			for (int j = 0; j <= p; ++j)
				dp[i + n][j] = (j <= m[i + n]) ? 0 : INF;

		for (int i = n - 1; i > 0; --i)
		{
			for (int j = 0; j <= p; ++j)
				if (true)
				{
					dp[i][j] = INF;
					int cur = getMin(2 * i, j) + getMin(2 * i + 1, j) + cost[i];
					if (dp[i][j] > cur)
						dp[i][j] = cur;
					cur = getMin(2 * i, j + 1) + getMin(2 * i + 1, j + 1);
					if (dp[i][j] > cur)
						dp[i][j] = cur;
				}	
				else
					dp[i][j] = INF;
		}

		printf("Case #%d: %d\n", ii, dp[1][0]);
	}

	return 0;
}