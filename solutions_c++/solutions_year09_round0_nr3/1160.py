#include <stdio.h>
#define MOD 10000

char *p = "welcome to code jam";
const int len = 19;
char s[1024];
int dp[32];

void Solve()
{
	for (int i=0; i<len; i++)
		dp[i] = 0;
	gets(s);
	for (int i=0; s[i]; i++)
		for (int j=len-1; j>=0; j--)
			if (p[j] == s[i])
				dp[j] = (dp[j] + (j == 0 ? 1 : dp[j-1])) % MOD;
	printf("%04d\n", dp[len-1]);
}

int main()
{
	int t;
	scanf("%d", &t);
	gets(s);
	for (int i=1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
