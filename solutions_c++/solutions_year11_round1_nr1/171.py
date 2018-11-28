#include <cstdio>
#include <cstring>

long long n;
int T;
int pd, pg;

inline int gcd(int a, int b) {
	while (a != 0) {
		int t = b % a;
		b = a;
		a = t;
	}
	return b;
}

inline bool gao() {
	if (pg == 100) {
		return pd == 100;
	}
	if (pg == 0) {
		return pd == 0;
	}
	return 100 / gcd(pd, 100) <= n;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%lld%d%d", &n, &pd, &pg);
		printf("Case #%d: %s\n", caseNum, gao() ? "Possible" : "Broken");
	}
	return 0;
}
