#include <cstdio>
#include <cstring>

const int M = 10010;
const int INF = 100000;
int n, v;
bool type[M], chg[M], value[M];
int dp[2][M];


bool isleaf(int node) {
	return node > (n - 1) / 2;
}
int costtrue(bool ad, int node) {
	int lc = node * 2, rc = node * 2 + 1;
	if (ad) {
		return dp[1][lc] + dp[1][rc];
	} else {
		return dp[1][lc] + dp[1][rc] <? dp[1][lc] + dp[0][rc] <? dp[0][lc] + dp[1][rc];
	}
}
int costfalse(bool ad, int node) {
	int lc = node * 2, rc = node * 2 + 1;
	if (ad) {
		return dp[0][lc] + dp[0][rc] <? dp[1][lc] + dp[0][rc] <? dp[0][lc] + dp[1][rc];
	} else {
		return dp[0][lc] + dp[0][rc];
	}
}
void calc(int node) {
	if (node > n) return ;
	calc(node * 2);
	calc(node * 2 + 1);
	if (!isleaf(node)) {
		if (chg[node]) {
			dp[0][node] = costfalse(type[node], node) <? costfalse(!type[node], node) + 1;
			dp[1][node] = costtrue(type[node], node) <? costtrue(!type[node], node) + 1;
		} else {
			dp[0][node] = costfalse(type[node], node);
			dp[1][node] = costtrue(type[node], node);
		}
	} else {
		dp[value[node]][node] = 0;
		dp[!value[node]][node] = INF;
	}
	//printf("#### %d\n", dp[0][9]);
}
int main() {
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; ++k) {
		scanf("%d%d", &n, &v);
		memset(type, 0, sizeof(type));
		memset(chg, 0, sizeof(chg));
		memset(value, 0, sizeof(value));
		for (int i = 0; i < (n - 1) / 2; ++i) {
			scanf("%d%d", type+i+1, chg+i+1);
		}
		for (int i =  (n - 1) / 2 + 1; i <= n; ++i) {
			scanf("%d", value+i);
		}
		calc(1);
		if (dp[v][1] < INF) {
			printf("Case #%d: %d\n", k+1, dp[v][1]);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", k + 1);
		}
	}
	return 0;
}

