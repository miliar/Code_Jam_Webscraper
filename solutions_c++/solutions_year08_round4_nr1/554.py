#include<stdio.h>
#include<string>
#include<algorithm>
const int maxn = 10005;
const int inf = 100000;
int f[maxn][2];
int n, V;
int v[maxn];
int g[maxn];
int c[maxn];
int calc(int u) {
	if (v[u] != -1) {
		return v[u];
	}
	if (g[u] == 0) {
		return v[u] = (calc(u * 2) || calc(u * 2 + 1));
	} else {
		return v[u] = (calc(u * 2) && calc(u * 2 + 1));
	}
}
int solve(int u, int s) {
	if (f[u][s] != -1) {
		return f[u][s];
	}
	if (v[u] == s) {
		return f[u][s] = 0;
	}
	if (u > (n - 1) / 2) { // leaf node
		return f[u][s] = inf;
	}
	
	f[u][s] = inf;
	
	if (s == 0) {
		if (g[u] == 0) { // OR = 0
			f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 0));
		} else { // AND = 0
			f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 0));
			f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 1));
			f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 0));
		}
	} else {
		if (g[u] == 0) { // OR = 1
			f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 1));
			f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 0));
			f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 1));
		} else { // AND = 1
			f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 1));
		}
	}
	
	if (c[u] == 1) {
		if (s == 0) {
			if (g[u] == 1) { // OR = 0
				f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 0) + 1);
			} else { // AND = 0
				f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 0) + 1);
				f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 1) + 1);
				f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 0) + 1);
			}
		} else {
			if (g[u] == 1) { // OR = 1
				f[u][s] = std::min(f[u][s], solve(u * 2, 0) + solve(u * 2 + 1, 1) + 1);
				f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 0) + 1);
				f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 1) + 1);
			} else { // AND = 1
				f[u][s] = std::min(f[u][s], solve(u * 2, 1) + solve(u * 2 + 1, 1) + 1);
			}
		}
	}
	
	return f[u][s];
}
int main() {
	int T;
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		scanf("%d%d", &n, &V);
		memset(c, 0, sizeof(c));
		for (int i = 1; i <= (n - 1) / 2; i++) {
			scanf("%d%d", &g[i], &c[i]);				
		}
		memset(v, -1, sizeof(v));
		for (int i = (n - 1) / 2 + 1; i <= n; i++) {
			scanf("%d", &v[i]);
		}
		calc(1);
		memset(f, -1, sizeof(f));
		int ans = solve(1, V);
		if (ans < inf) {
			printf("Case #%d: %d\n", casen, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", casen);
		}
	}
	return 0;
}
