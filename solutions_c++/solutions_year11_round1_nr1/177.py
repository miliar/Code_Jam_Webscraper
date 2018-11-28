#include <cstdio>
#include <cstring>

typedef long long LL;

LL N, PD, PG;

LL gcd(LL a, LL b) {
	if (a < b) return gcd(b, a);
	if (b == 0) return a;
	if (a % b == 0) return b;
	return gcd(b, a % b);
}

int main() {
	int test;
	scanf("%d", &test);
	for (int i = 0; i < test; i++) {
		printf("Case #%d: ", i + 1);
		scanf("%lld%lld%lld", &N, &PD, &PG);
		if (100 / gcd(PD, 100) > N) {
			puts("Broken");
			continue;
		}
		if (PG == 100 && PD != 100) {
			puts("Broken");
			continue;
		}
		if (PG == 0 && PD != 0) {
			puts("Broken");
			continue;
		}
		puts("Possible");
	}
	return 0;
}
