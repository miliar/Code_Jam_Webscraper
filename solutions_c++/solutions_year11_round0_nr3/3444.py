#include <cstdio>
#include <cstring>

#define long long long

long solve() {
	int n;
	scanf("%d", &n);
	long sum = 0;
	int min = 0x0fffffff, xsum = 0;
	for (int i = 0; i < n; ++i) {
		int candy;
		scanf("%d", &candy);
		if (candy < min) min = candy;
		sum += candy;
		xsum ^= candy;
	}
	if (xsum == 0) return sum-min;
	return -1LL;
}

int main() {
	int cc;
	scanf("%d", &cc);
	for (int i = 1; i <= cc; ++i) {
		long r = solve();
		printf("Case #%d: ", i);
		if (r == -1LL) printf("NO\n");
		else printf("%lld\n", r);
	}
}
