#include <stdio.h>
#include <string.h>
#define MAXN 10010
int n, d[MAXN], l[MAXN], D;
int dp[MAXN], mrk[MAXN];
int q[MAXN * 10], head, tail;

void update(int u, int v) {
	int cost;
	cost = u>v?d[u]-d[v]:d[v]-d[u];
	if (l[v] < cost) cost = l[v];
	//printf("%d %d %d\n", u, v, cost);
	if (dp[v] >= cost) {
		return;
	}
	dp[v] = cost;
	if (!mrk[v]) {
		mrk[v] = true;
		q[tail++] = v;
	}
}

int main() {
	int t, ca=0, i, j, u;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (i=0;i<n;++i) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &d[n]);
		l[n] = 0;
		memset(dp, -1, sizeof(dp));
		memset(mrk, 0, sizeof(mrk));
		dp[0] = d[0];
		head = tail = 0;
		q[tail++] = 0;
		while (head < tail) {
			int u = q[head++];
			mrk[u] = false;
			for (i = u+1; i <= n && d[i] - d[u] <= dp[u];++i) {
				update(u, i);
			}
			for (i = u-1; i >= 0 && d[u] - d[i] <= dp[u];--i) {
				update(u, i);
			}
		}
		printf("Case #%d: ", ++ca);
		if (dp[n] != -1) {
			puts("YES");
		} else {
			puts("NO");
		}
	}
	return 0;
}