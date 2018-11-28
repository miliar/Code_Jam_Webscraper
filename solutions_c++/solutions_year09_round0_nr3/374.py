#include <cstdio>
#include <cstring>
#include <string>

#define rep(i, n) for (int i = 0; i < n; i++)

using namespace std;

int dp[25][520];

int main() {
	int N;
	string S = "welcome to code jam";

	char line[520];
	gets(line);
	N = atoi(line);
	
	rep(n, N) {
		gets(line);
		
		memset(dp, 0, sizeof(dp));
		rep(i, 520) {
			dp[0][i] = 1;
		}

		for (int i = 1; i <= S.size(); i++) {
			for (int j = 1; j <= strlen(line); j++) {
				dp[i][j] = dp[i][j-1];

				if (line[j-1] == S[i-1]) {
					dp[i][j] += dp[i-1][j-1];
					dp[i][j] %= 10000;
				}
			}
		}

		printf("Case #%d: %04d\n", n+1, dp[S.size()][strlen(line)]);
	}
}

