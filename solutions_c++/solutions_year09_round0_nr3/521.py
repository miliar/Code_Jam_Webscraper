#include <cstdio>
#include <cstring>

const int MOD = 10000;

char st[1000], word[20] = "welcome to code jam";
int dp[550][50];

void solve() {

	gets(st);
	int len = strlen(st);

	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for (int i = 1; i <= len; i++)
		for (int j = 0; j <= 19; j++) {
			dp[i][j] += dp[i - 1][j];
			if (j > 0 && st[i - 1] == word[j - 1]) dp[i][j] += dp[i - 1][j - 1];
			dp[i][j] %= MOD;
		}
	int ans = dp[len][19];
	if (ans < 10) printf("000");
	else if (ans < 100) printf("00");
	else if (ans < 1000) printf("0");
	printf("%d\n", ans);

}

int main() {

	int test;
	scanf("%d", &test); getchar();
	for (int i = 1; i <= test; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}

