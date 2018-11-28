#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 50 + 1;
const int INF = 1012345678;

int N, K, B, T, X[MAXN], V[MAXN], mmin, dp[MAXN][MAXN];
bool tag[MAXN];

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		scanf("%d%d%d%d", &N, &K, &B, &T);
		for (int i = 0; i < N; i++) {
			scanf("%d", &X[i]);
		}
		for (int i = 0; i < N; i++) {
			scanf("%d", &V[i]);
		}
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			tag[i] = (X[i] + V[i] * T >= B);
//printf("%d", tag[i]);
			cnt += tag[i];
		}
//printf("\ncnt = %d\n", cnt);
		printf("Case #%d: ", oo + 1);
		if (K == 0) {
			puts("0");
			continue;
		}
		if (cnt < K) {
			puts("IMPOSSIBLE");
			continue;
		}
		memset(dp, 0, sizeof(dp));
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j <= N; j++) {
				dp[i][j] = INF;
			}
		}
		dp[N][0] = 0;
		for (int i = N; i > 0; i--) {
			if (tag[i - 1]) {
				for (int j = 0; j <= N; j++) {
					if (dp[i][j] == INF) continue;
					int cnt = 0;
					for (int k = i; k < N; k++) {
						if (!tag[k]) cnt++;
					}
//printf("cnt = %d (%d %d)\n", cnt, i, N - 1);
					dp[i - 1][j + 1] = min(dp[i - 1][j + 1], dp[i][j] + cnt);
				}
			}
			for (int j = 0; j <= N; j++) {
				dp[i - 1][j] = min(dp[i - 1][j], dp[i][j]);
			}
		}
		int mmin = dp[0][K];
		for (int i = K + 1; i <= N; i++) {
			mmin = min(mmin, dp[0][i]);
		}
		printf("%d\n", mmin);
/*		printf("~~mmin~~\n");
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j <= N; j++) {
				printf("%d ", dp[i][j]);
			}
			putchar('\n');
		}
		printf("~~mmin~~\n");*/
	}
	return 0;
}
