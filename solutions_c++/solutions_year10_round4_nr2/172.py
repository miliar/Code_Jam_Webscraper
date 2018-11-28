#include <iostream>
using namespace std;

const int maxlog = 12;
const int maxn = 1 << maxlog;
const int inf = 1000000000;

int tcase, n, p, m[maxn], f[maxn][maxlog], val[maxn];

void init() {
	scanf("%d", &p);
	n = 1 << p;
	for (int i = 1; i <= n; ++i)
		scanf("%d", m + i), m[i] = p - m[i];
	for (int i = p - 1; i >= 0; --i)
		for (int j = (1 << i); j <= (1 << i + 1) - 1; ++j)
			scanf("%d", val + j);
}

void dp(int u, int k) {
	if (f[u][k] != -1) return;
	if (u * 2 >= n * 2) {
		f[u][k] = (k >= m[u - n + 1]) ? 0 : inf;
		return;
	}
	dp(u * 2, k);
	dp(u * 2, k + 1);
	dp(u * 2 + 1, k);
	dp(u * 2 + 1, k + 1);
    f[u][k] = min(f[u*2][k]+f[u*2+1][k],f[u*2][k+1]+f[u*2+1][k+1]+val[u]);
    if (f[u][k]>inf) f[u][k]= inf;
}

int solve() {
	memset(f, -1, sizeof(f));
	dp(1, 0);
	return f[1][0];
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int c = 1; c <= tcase; ++c) {
		init();
		printf("Case #%d: %d\n", c, solve());
	}
	return 0;
}
