#include <stdio.h>

#define INF 999999999

const int bound = 256;

int dp[110][256];

inline int abs(int n) {
	if (n < 0)
		return -n;
	return n;
}

int main() {
	int ecase, ecount;
	int ed, ei, em, en;
	int i, j, k;
	scanf("%d", &ecase);
	for(ecount = 1; ecount <= ecase;ecount++) {
		scanf("%d%d%d%d", &ed, &ei, &em, &en);
//		printf("[%d, %d, %d, %d]", ed, ei, em, en);
		for (i = 0; i < en + 2; i++)
			for (j = 0; j < bound; j++)
					dp[i][j] = INF;
		for (i = 0; i < bound; i++)
			dp[0][i] = 0;
		for (i = 1; i <= en+1; i++) {
			int et;
			if (i <= en) {
				scanf("%d", &et);
			}
			for (j = 0; j < bound; j++)
				for (k = 0; k < bound; k++) {
					int t;
					int cch;
					if (i <= en)
						cch = abs(et - k);
					else
						cch = 0;
					if (ed + ei < cch)
						cch = ed + ei;
					int cp;
					if (j == k)
						cp = 0;
					else if (em == 0)
						cp = INF;
					else {
						cp = ((abs(j - k) - 1) / em) * ei;
						//printf("%d %d--->%d\n", j, k, cp);
					}
					t = dp[i-1][j] + cch + cp;
					if (t < dp[i][k]) {
						dp[i][k] = t;
						//printf("I: dp[%d][%d]=%d + %d + %d -> dp[%d][%d] = %d\n", i-1, j, dp[i-1][j], cch, cp, i, k, dp[i][k]);
					}
				}
			for (j = 0; j < bound; j++)
				if (dp[i-1][j] + ed < dp[i][j]) {
					dp[i][j] = dp[i-1][j] + ed;
					//printf("D: dp[%d][%d]=%d + %d  -> dp[%d][%d] = %d\n", i-1, j, dp[i-1][j], ed, i, j, dp[i][j]);
				}
//			for (j = 0; j < bound; j++)
//				printf("dp[%d][%d] = %d\n", i, j, dp[i][j]);
		}
		int ans = INF;
		for (i = 0; i < bound; i++)
			if (dp[en + 1][i] < ans)
				ans=dp[en + 1][i];
		printf("Case #%d: %d\n", ecount, ans);
	}

	return 0;
}
