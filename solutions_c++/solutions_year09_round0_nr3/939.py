#include <cstdio>
#include <cstring>

const int MAX_N = 20;
const int MAX_LEN = 500 + 5;
const int MOD = 10000;

char s[] = "welcome to code jam";

int T;
int N = strlen(s);
int dp[MAX_N];
char in[MAX_LEN];
int main()
{
	scanf("%d\n", &T);
	for(int t = 0; t < T; t ++)
	{
		gets(in);
		memset(dp, 0, sizeof(dp));
		dp[0] = 1;
		for(int i = 0; in[i]; i ++)
			for(int j = 0; s[j]; j ++)
				if(in[i] == s[j])
				{
					dp[j + 1] += dp[j];
					if(dp[j + 1] >= MOD)	dp[j + 1] -= MOD;
				}
		printf("Case #%d: %04d\n", t + 1, dp[N]);
	}
    return 0;
}
