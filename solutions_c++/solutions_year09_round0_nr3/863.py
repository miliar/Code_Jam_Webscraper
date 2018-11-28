#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#define clr(a) memset(a, 0, sizeof(a))

void dbg(const char * fmt, ...)
{
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
}


char s[10000];

const char welcome[] = "welcome to code jam";
const int l = strlen(welcome);

int dp[20];


void solve(int n)
{
	gets(s);
	clr(dp);
	dp[0] = 1;
	for(int i = 0; s[i]; i++)
	{
		for(int j = l-1; j >= 0; j--)
		{
			if (s[i] == welcome[j])
			{
				dp[j+1] += dp[j];
				dp[j+1] %= 10000;
			}
		}
	}
	printf("Case #%d: %04d\n", n, dp[l]);
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d\n", &n);
	for(int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}
