#include <cstdio>

long long gcd(long long a, long long b) {
	if (a < b) {
		a ^= b ^= a ^= b;
	}
	if (b) {
		return gcd(b, a % b);
	} else {
		return a;
	}
}

bool proc() {
	long long n, pd, pg;
	scanf("%lld %lld %lld ", &n, &pd, &pg);

	if (pg == 0) {
		if (pd != 0) {
			return 0;
		} else {
			return 1;
		}
	}
	if (pd == 0) {
		if (pg == 100) {
			return 0;
		} else {
			return 1;
		}
	} else {
		long long g = gcd(100, pd);
		g = 100 / g;
		if (g > n) {
			return 0;
		} else {
			if (pg == 100) {
				if (pd == 100) {
					return 1;
				} else {
					return 0;
				}
			} else {
				return 1;
			}
		}
	}
}

int main() {
	int cases;
	scanf("%d ", &cases);
	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		if (proc()) {
			printf("Possible");
		} else {
			printf("Broken");
		}
		printf("\n");
	}

	return 0;
}
