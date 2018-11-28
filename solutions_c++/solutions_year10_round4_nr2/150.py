#include <stdio.h>

#define INF 999999999

int ep[1025][1025];
int em[1025];

int info2[20];
int dp[1025][1025][12];
int reg[1025][1025][12];
int ecase,ecount;

int dfs(int h, int t, int c, int l) {
	if (l == 0) {
		if (em[h] - c > 0)
			return INF;
		else
			return 0;
	}
	else {
		int m = (h + t) / 2;
		if (reg[h][t][c] != ecount) {
			reg[h][t][c] = ecount;
			int i;
			bool flag = false;
			for (i = h; i < t; i++)
				if (em[i] - c > l)
					flag = true;
			if (flag)
				dp[h][t][c] = INF;
			else {
				int re1 = ep[h][t] + dfs(h, m, c+1, l-1) + dfs(m, t, c+1, l-1);
				int re2 = dfs(h, m, c, l-1) + dfs(m, t, c, l-1);
				if (re1 < re2)
					dp[h][t][c] = re1;
				else
					dp[h][t][c] = re2;
			}
			//printf("dp[%d][%d][%d] = %d\n", h, t, c, dp[h][t][c]);
		}
		return dp[h][t][c];
	}
}

int main() {
	int en;
	int i, j;
	info2[0] = 1;
	for (i = 1; i < 20; i++)
		info2[i] = info2[i-1] * 2;
	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		scanf("%d", &en);
		for (i = 0; i < info2[en]; i++) {
			scanf("%d", &em[i]);
			em[i] = en - em[i];
		}
		for (i = 1; i <= en; i++) 
			for (j = 0; j < info2[en]; j += info2[i]){
				scanf("%d", &ep[j][j + info2[i]]);
				//printf("(%d, %d) -> %d\n", j, j + info2[i], ep[j][j + info2[i]]);
			}
		printf("Case #%d: %d\n", ecount, dfs(0, info2[en], 0, en));
	}
	return 0;
}
