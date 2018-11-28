#include <cstdio>

#define For(i,n) for (int i = 0; i < n; ++i)

const char t[] = "welcome to code jam";

int T, dp[20][1 << 10], n;
char s[1 << 10];

int main() {
	scanf("%d", &T), gets(s);
	For(r,T) {
		printf("Case #%d: ", r + 1);
		gets(s);
		n = -1; while (s[++n]);
		For(i,n) { dp[0][i] = (i ? dp[0][i - 1] : 0); if (s[i] == 'w') ++dp[0][i]; }
		For(j,19) if (j) dp[j][0] = 0;
		For(i,n) if (i) For(j,19) if (j) {
			dp[j][i] = dp[j][i - 1];
			if (s[i] == t[j]) dp[j][i] = (dp[j][i] + dp[j - 1][i - 1])%10000;
		}
		printf("%04d\n", dp[18][n - 1]);
	}
	return 0;
}
