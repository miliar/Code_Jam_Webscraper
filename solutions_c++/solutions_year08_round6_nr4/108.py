#include <stdio.h>
#include <string.h>
char g1[11][11], g2[11][11];
char del[11], flag;
int n, m, re[11];
int order[11];
char mark[11];

int judge() {
	int i, j;
	int ii, jj;
	for (i = 1; i <= m; i++)
		for (j = i + 1; j <= m; j++) {
			ii = re[order[i]];
			jj = re[order[j]];
			if (g1[ii][jj] != g2[i][j]) return 0;
		}
	return 1;
}

void makeorder(int d) {
	int i;
	if (flag) return;
	if (d > m) {
		if (judge()) flag = 1;
		return ;
	}
	for (i = 1; i <= m; i++)
		if (!mark[i]) {
			mark[i] = 1;
			order[d] = i;
			makeorder(d + 1);
			if (flag) return;
			mark[i] = 0;
		}
}

void dfs(int x, int st) {
	int i, j;
	if (flag) return;
	if (x == n - m) {
		for (j = 0, i = 1; i <= n; i++)
			if(!del[i]) re[++j] = i;
		memset(mark, 0, sizeof(mark));
		makeorder(1);
		return ;
	}	
	for (i = st; i <= n; i++) {
		del[i] = 1;
		dfs(x + 1, i + 1);
		if (flag) return;
		del[i] = 0;
	}
}

int main() {
	int tn, i, a, b, prob = 0;
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	for (scanf("%d", &tn); tn--;) {
		memset(g1, 0, sizeof(g1));
		memset(g2, 0, sizeof(g2));
		memset(del, 0, sizeof(del));
		scanf("%d", &n);
		for (i = 0; i < n - 1; i++) {
			scanf("%d%d", &a, &b);
			g1[a][b] = g1[b][a] = 1;
		}
		scanf("%d", &m);
		for (i = 0; i < m - 1; i++) {
			scanf("%d%d", &a, &b);
			g2[a][b] = g2[b][a] = 1;
		}
		flag = 0;
		dfs(0, 1);
		if (flag) printf("Case #%d: YES\n", ++prob);
		else printf("Case #%d: NO\n", ++prob);
	}
	return 0;
}
