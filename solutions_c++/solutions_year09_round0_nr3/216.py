#include <cstdio>
#include <cstring>

const int MAXN = 21;
const int MAXL = 10240;
const int MOD = 10000;
const char * welcome = "welcome to code jam";

int L, dp[MAXN];
char line[MAXL];

int main() {
	int task;
	scanf("%d", &task);
	gets(line);
	for (int oo = 0; oo < task; oo++) {
		gets(line);
		L = (int)strlen(line);
		memset(dp, 0, sizeof(dp));
		dp[0] = 1;
		for (int i = 0; i < L; i++) {
			for (int j = 18; j >= 0; j--) {
				if (line[i] == welcome[j]) {
					dp[j + 1] += dp[j];
					if (dp[j + 1] >= MOD) dp[j + 1] -= MOD;
				}
			}
		}
//		for (int i = 0; i < MAXN; i++) printf("dp[%d] = %d\n", i, dp[i]);
		printf("Case #%d: %04d\n", oo + 1, dp[19]);
	}
	return 0;
}
