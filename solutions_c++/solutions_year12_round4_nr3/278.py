#include <iostream>
#include <cstdio>
using namespace std;
const int inf = 1000000000;
int f[10000];
int next[10000];
int n, test;
bool flag;
int q[2005][2005];
int solve(int a, int b, int c) {
	if (b == c) return inf;
	return (int)f[b] - (f[c] - f[b]) / (c - b) * (b - a);
}

void dfs(int l, int r, int d) {
	int tl = l, tmp = 0;
	if (l == r) return ;
	while (l != r) {
		q[tl][++tmp] = l;
		l = next[l];
	}
	l = tl;
	q[l][++tmp] = r;
	f[q[l][tmp - 1]] = d ;
	for (int i = tmp - 2; i >= 1; --i) {
		if (tl != 1) f[q[l][i]] = solve(q[l][i], q[l][i + 1], q[l][i + 2]);
		else f[q[l][i]] = inf;
	}
	l = tl;
	while (l != r) {
		dfs(l + 1, next[l], f[l] - 1);
		l = next[l];
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &test);
	for (int tt = 1; tt <= test; ++tt) {
		scanf("%d", &n);
		for (int i = 1; i < n; ++i) scanf("%d", &next[i]);
		next[n] = n + 1;
		flag = true;
		for (int i = 1; i <= n ; ++i) 
		for (int j = i + 1; j <= n; ++j)
		if (next[i] > j && next[i] < next[j]) flag = false;
		if (flag) {
			dfs(1, n + 1, inf);
			printf("Case #%d:", tt);
			for (int i = 1; i <= n; ++i) printf(" %d", f[i]);
			printf("\n");
		} else printf("Case #%d: Impossible\n", tt);
	}
	return 0;
}