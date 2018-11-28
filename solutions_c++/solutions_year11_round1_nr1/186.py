#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long lint;

lint gcd(lint a, lint b) {
	if (b == 0)
		return a;
	return gcd(b, a % b);
}

int main() {
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		lint n; int pd, pg;
		scanf("%lld %d %d", &n, &pd, &pg);

		bool ok = true;
		if (100 / gcd(100, pd) > n)
			ok = false;
		else if (pg == 100 && pd != 100)
			ok = false;
		else if (pg == 0 && pd != 0)
			ok = false;

		printf("Case #%d: ", test);
		if (ok)
			printf("Possible\n");
		else
			printf("Broken\n");
	}

	return 0;
}
