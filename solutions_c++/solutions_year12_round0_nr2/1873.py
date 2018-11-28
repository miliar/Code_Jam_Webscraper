#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>


#define clr(a) memset(a, 0, sizeof(a))

typedef std::pair<int, int> pii;
typedef long long ll;

void dbg(const char * fmt, ...)
{
	#if 1
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
		fflush(stdout);
	#endif
}

int norm[32][16];
int surp[32][16];

int dp[128][128];
int sum[128];

void solve(int test_num)
{
	clr(dp);
	int n, s, p;
	scanf("%d%d%d", &n, &s, &p);
	dp[0][0] = 0;
		
	for(int i = 0; i < n; i++)
		scanf("%d", &sum[i]);
	for(int i = 0; i < n; i++)
		for(int j = 0; j <= i; j++)
		{
			int s = sum[i];
			dp[i+1][j+1] = std::max(dp[i+1][j+1], dp[i][j] + surp[s][p]);
			dp[i+1][j] = std::max(dp[i+1][j], dp[i][j] + norm[s][p]);
		}
	
	printf("Case #%d: %d\n", test_num, dp[n][s]);
}

int main()
{
	for(int i = 0; i <= 10; i++)
		for(int j = 0; j <= 10; j++)
			for(int k = 0; k <= 10; k++)
			{
				int min = std::min(i, std::min(j, k));
				int max = std::max(i, std::max(j, k));
				int s = i + j + k;
				if (max - min > 2)
					continue;
				if (max - min == 2)
					surp[s][max] = 1;
				else
					norm[s][max] = 1;
			}
	for(int i = 0; i <= 30; i++)
		for(int j = 10; j > 0; j--)
		{
			norm[i][j-1] |= norm[i][j];
			surp[i][j-1] |= surp[i][j];
		}
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
		solve(i+1);


	return 0;
}
