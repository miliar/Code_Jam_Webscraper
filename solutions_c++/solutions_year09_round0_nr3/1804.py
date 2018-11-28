#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
char s[600];
char t[25] = "welcome to code jam\0";
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas, cass = 0;
	for (scanf("%d\n", &cas); cas--; ) {
		gets(s);
		int pre = 0, nxt = 1;
		int dp[2][20];
		memset(dp[pre], 0, sizeof(dp[pre]));
		if (s[0]=='w') dp[0][0] = 1;
		for (int i=1; s[i]!='\0'; ++i) {
			memset(dp[nxt], 0, sizeof(dp[nxt]));
			for (int j=0; t[j]!='\0'; ++j) if (s[i]==t[j]) {
				if (j) dp[nxt][j] = dp[pre][j-1];
				else dp[nxt][j] = 1;
			}
			for (int j=0; t[j]!='\0'; ++j) {
				dp[nxt][j] += dp[pre][j];
				if (dp[nxt][j]>10000) dp[nxt][j] -= 10000;
			}
			swap(pre, nxt);
		}
		printf("Case #%d: %04d\n", ++cass, dp[pre][18]);
	}
	return 0;
}


