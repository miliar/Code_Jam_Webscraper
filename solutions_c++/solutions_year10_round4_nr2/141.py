#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#define clr(a) memset(a, 0, sizeof(a))

#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

int dp[10000][20];
int cost[10000];

const int infty = 1e9;

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	for(int i = 0; i < 10000; i++)
		for(int j = 0; j < 20; j++)
			dp[i][j] = infty;
	int p;
	scanf("%d", &p);
	p = 1<<p;
	for(int i = 0; i < p; i++)
	{
		int d;
		scanf("%d", &d);
		dp[2*p-1-i][d] = 0;
	}
	for(int i = p - 1; i >= 1; i--)
		scanf("%d", &cost[i]);
	for(int i = 2*p-1; i >= 1; i--)
	{
		for(int j = 18; j >= 0; j--)
		{
			dp[i][j] = std::min(dp[i][j], dp[i][j+1]);
			dp[i][j] = std::min(dp[i][j], (dp[2*i][j+1] + dp[2*i+1][j+1]));
			dp[i][j] = std::min(dp[i][j], cost[i] + (dp[2*i][j] + dp[2*i+1][j]));
		}
//		dbg("%d (%d, %d, %d)\n", i, dp[i][0], dp[i][1], dp[i][2]);
	}
	printf("%d\n", dp[1][0]);

}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
