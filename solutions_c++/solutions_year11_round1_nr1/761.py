#include <iostream>

using namespace std;

long long gcd(long long a, long long b) {
	if (b == 0) {
		return a;
	} else {
		return gcd(b, a % b);
	}
}

int main() {

	int Tc;
	
	freopen("A-large.in", "r", stdin);
	freopen("r1a-large.out", "w", stdout);

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {
		long long n;
		int pd, pg;
		scanf("%I64d%d%d", &n, &pd, &pg);

		bool result = true;

		if (0 == pd && pg == 100) {
			result = false;
		} else if (0 == pd && pg < 100) {
			result = true;
		} else if (100 == pd && pg == 0) {
			result = false;
		} else if (100 == pd && pg > 0) {
			result = true;
		} else if (100 == pg && pd < 100) {
			result = false;
		} else if (0 == pg && pd > 0) {
			result = false;
		} else {
			result = false;
			for (int i = 1; i <= n && i <= 100; ++i) {
				if ((i * pd) % 100 == 0) {
					result = true;
				}
			}
		}

		if (true == result) {
			printf("Case #%d: Possible\n", tc);
		} else {
			printf("Case #%d: Broken\n", tc);
		}
	}

	return 0;
}

