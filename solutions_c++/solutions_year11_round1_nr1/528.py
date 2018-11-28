#include <cstdio>
#include <cstring>

int m, pd, pg;
long long n;

int gcd(int a, int b) {
	while (a > 0) {
		int t = b % a;
		b = a;
		a = t;
	}
	return b;
}

int main() {
	scanf("%d", &m);
	for (int q = 1; q <= m; q ++) {
		scanf("%lld%d%d", &n, &pd, &pg);
		if (pg == 100) {
			if (pd != 100) printf("Case #%d: Broken\n", q);
			else printf("Case #%d: Possible\n", q);
		} else if (pg == 0) {
			if (pd != 0) printf("Case #%d: Broken\n", q);
			else printf("Case #%d: Possible\n", q);
		} else {
			int k = gcd(pd, 100);
			long long b = 100 / k;
			if (b <= n) printf("Case #%d: Possible\n", q);
			else printf("Case #%d: Broken\n", q);
		}
	}
	return 0;
}
