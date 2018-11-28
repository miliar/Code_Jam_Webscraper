#include <cstdio>

#define CODE C-large

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MAXN 1001

long long solve() {
	int r, k, n;
	int g[MAXN];
	scanf("%d %d %d\n", &r, &k, &n);
	for (int i = 0; i < n; ++i)
		scanf("%d", &g[i]);
	int pr[MAXN], fw[MAXN];
	int rnd[MAXN];
	for (int i = 0; i < n; ++i) {
		pr[i] = 0;
		fw[i] = i;
		rnd[i] = -1;
		for (int j = i; pr[i] + g[j] <= k && (pr[i] == 0 || j != i); pr[i] += g[j], fw[i] = j = (j + 1 == n ? 0 : j + 1));
	}
	long long profit = 0;
	for (int i = 0, j = 0; i < r; ++i) {
		//printf("%d %d %lld\n", i, j, profit);
		if (rnd[j] >= 0) {
			int len = i - rnd[j];
			if (r - i >= len) {
				int cnt = (r - i) / len;
				long long rprofit = 0;
				for (int k = j; rprofit == 0 || k != j; rprofit += pr[k], k = fw[k]);
				profit += rprofit * cnt;
				i += cnt * len - 1;
				continue;
			}
		}
		rnd[j] = i;
		profit += pr[j];
		j = fw[j];
	}
	return profit;
}

int main() {
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: %lld\n", i, solve());
	}
	return 0;
}
