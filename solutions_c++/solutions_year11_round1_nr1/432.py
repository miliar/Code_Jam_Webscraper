#include <cstdio>

long long gcd(long long x, long long y) {
	return x == 0 ? y : gcd(y % x, x);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int re = 1; re <= t; ++re) {
		long long n, pd, pg;
		scanf("%lld%lld%lld", &n, &pd, &pg);

		printf("Case #%d: ", re);

		bool ok = false;
		for (long long i = 0; i <= 100 && i < n; ++i) {
			if ((n - i) * pd % 100 == 0) {
				ok = true;
				break;
			}
		}

		if ((pd != 0 && pg == 0) || (pd != 100 && pg == 100)) {
			ok = false;
		}
		puts(ok ? "Possible" : "Broken");
	}
	return 0;
}
