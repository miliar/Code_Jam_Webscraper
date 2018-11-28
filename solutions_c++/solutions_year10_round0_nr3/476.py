#include <cstdio>
#include <cstring>

int t, r, k, n, g[1001];
bool chk[1001];
int round[1001], next[1001];
int round_cyc;
long long money[1001], cnt, tot, money_cyc;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int i, j, p, q;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		scanf("%d%d%d", &r, &k, &n);
		for (j = 1; j <= n; j++)
			scanf("%d", &g[j]);
		memset(chk, 0, sizeof(chk));
		q = 1;
		tot = 0;
		chk[q] = true;
		round[q] = 0;
		money[q] = tot;
		for (j = 1; j <= r; j++) {
			p = q;
			cnt = 0;
			while (cnt + g[q] <= k) {
				cnt += g[q];
				q++;
				if (q > n) q = 1;
				if (p == q) break;
			}
			tot += cnt;
			next[p] = q;
			if (chk[q]) break;
			chk[q] = true;
			round[q] = j;
			money[q] = tot;
		}
		if (j < r) {
			round_cyc = j - round[q];
			money_cyc = tot - money[q];
			r -= j;
			tot += money_cyc * (r / round_cyc);
			r %= round_cyc;
			p = q;
			while (r) {
				q = next[q];
				r--;
			}
			tot += money[q] - money[p];
		}
		printf("Case #%d: %lld\n", i, tot);
	}
	return 0;
}