#include <cstdio>

using namespace std;

int g[1000], was[1000];
long long res[1000];

int main () {
	int tt;
	scanf ("%d", &tt);
	for (int it = 1; it <= tt; it++) {
		int n, r, k;
		scanf ("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i++) {
			scanf ("%d", &g[i]);
			was[i] = 0;
		}
		long long ans = 0;
		int cyc = 0;
		for (int i = 0, j = 0; i < r; i++) {
			if (was[j] != 0 && !cyc) {
				int per = i - was[j] + 1;
				long long rper = ans - res[j];
				if (i + per < r) {
					int k = (r - i - 1) / per;
					ans += k * rper;
					i += k * per;
				}
				cyc = 1;
			}
			if (!cyc) {
				res[j] = ans;
				was[j] = i + 1;
		        }
			int s = 0, l = 0;
			for (; l < n && s + g[(j + l) % n] <= k; l++) s += g[(j + l) % n];
			j = (j + l) % n;
			ans += s;
		}
		printf ("Case #%d: %I64d\n", it, ans);
	}
}