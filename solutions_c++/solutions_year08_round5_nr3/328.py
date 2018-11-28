#include<stdio.h>
#include<string>
int n, m;
int ans;
char g[15][15];
char G[15][15];
int ok(int r, int c) {
	if (G[r][c] == 'x') {
		return 0;
	}
	if (c > 0 && g[r][c - 1] == 1) {
		return 0;
	}
	if (c < m - 1 && g[r][c + 1] == 1) {
		return 0;
	}
	if (r > 0) {
		if (c > 0 && g[r - 1][c - 1] == 1) {
			return 0;
		}
		if (c < m - 1 && g[r - 1][c + 1] == 1) {
			return 0;
		}
	}
	return 1;
}
void solve(int r, int c, int s) {
//	printf("%d %d %d\n", r, c, s);
	ans = std::max(ans, s);

	if (r == n) {
		return;
	}
	if (c == m) {
		solve(r + 1, 0, s);
		return;
	}	
	
	if (ok(r, c) && s + 1 + (m - c) / 2 + ((n - 1 - r) * m + 1) / 2 > ans) {
		g[r][c] = 1;
		solve(r, c + 1, s + 1);
		g[r][c] = 0;
	}
	
	if (s - c + m * (n - r) - 1 > ans) {
		solve(r , c + 1, s);
	}
}
int main() {
	int T;
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", G[i]);
		}
		ans = 0;		
		memset(g, 0, sizeof(g));	
		solve(0, 0, 0);
		printf("Case #%d: %d\n", casen, ans);
	}
	
	return 0;
}

