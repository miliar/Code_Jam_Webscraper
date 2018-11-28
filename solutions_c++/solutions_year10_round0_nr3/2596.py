#include <stdio.h>
int g[2000];
int sum[2000];

int main(int argc, char *argv[]) {
	int r, k, n;
	int x, ans, t;
	int start, fin;
	scanf ("%d", &t);
	for (int z = 1; z <= t; z++) {
		ans = 0;
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d", &g[i]);
			sum[i] = g[i] + sum[i-1];
		}
		start = fin = 1;
		int prev_fin = 0;
		for (int i = 0; i < r; i++) {
			int count = 0;
			while (count < n) {
				if (fin >= start) {
					if (sum[fin] - sum[start-1] <= k) {
						count++;
						prev_fin = fin;
						fin++;
					}
					else break;
				}
				else {
					if (sum[fin]+sum[n] - sum[start-1] <= k) {
						count++;
						prev_fin = fin;
						fin++;
					}
					else break;
				}

				if (fin > n) fin = 1;
			}
			if (prev_fin >= start) ans += sum[prev_fin] - sum[start-1];
			else ans += sum[prev_fin]+sum[n] - sum[start-1];
			start = fin;
		}
		printf("Case #%d: %d\n", z, ans);
	}
	return 0;
}
