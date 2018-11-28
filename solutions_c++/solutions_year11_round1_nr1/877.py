#include <stdio.h>
#include <math.h>

int gcd(int m, int n) {
	if (n == 0) {
		return m;
	}
	return gcd(n, m%n);
}

int lcm(int m, int n) {
	if (m > n) {
		return m / gcd(m, n);
	} else {
		return n / gcd(n, m);
	}
}

int main() {

	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		long long int N;
		scanf("%lld", &N);
		int pd, pg;
		scanf("%d %d", &pd, &pg);

		int md = 100 / gcd(pd, 100);
		int mg = 100 / gcd(pg, 100);

		bool possible = false;

		if (pg == 0 || pg == 100) {
			possible = (pg == pd);
		} else {
			int minG = md * pd / pg;
			if ((md * pd) % pg) {
				minG++;
			}
			int _minG = md * (100 - pd) / (100 - pg);
			if ((md * (100 - pd)) % (100 - pg)) {
				_minG++;
			}

			if (minG < _minG) {
				minG = _minG;
			}

			int g = minG / mg;
			if (minG % mg) {
				g++;
			}

			if (md <= N) {
				possible = true;
			}
		}
		
		printf("Case #%d: %s\n", t, possible ? "Possible" : "Broken");
	}

	return 0;
}
