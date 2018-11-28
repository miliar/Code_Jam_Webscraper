#include <cstdio>
#include <cstring>

using namespace std;

int n, test, len, dp[20], i, j;
char text[600], pattern[] = "welcome to code jam";

int main(void)
{
	scanf("%d ", &n);

	for (test = 1; test <= n; ++test) 
	{
		gets(text);
		len = strlen(text);

		memset(dp, 0, sizeof dp);

		for (i = 0; i < len; ++i) {
			for (j = 18; j; --j) if (text[i] == pattern[j]) dp[j] += dp[j - 1], dp[j] %= 10000;
			dp[0] += text[i] == 'w';
		}

		printf("Case #%d: %04d\n", test, dp[18]);
	}

	return 0;
}
