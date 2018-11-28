#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;

ll sol[501][501];
ll comb[501][501];

ll gen(int depht, int n) {
	if (!depht) return 1;

	if (comb[depht][n] > -1) return comb[depht][n];

	ll r = 0;
	for (int i = 0; i < n; i++) {
		r += gen(depht - 1, n - i - 1);
		r %= 100003;
	}
		
	return comb[depht][n] = r;
}

ll get(ll vstavi, ll stevil) {
	return gen(stevil - vstavi, stevil);
}

inline void prp() {
	memset(comb, -1, sizeof comb);

	sol[2][1] = 1;
	for (ll i = 3; i <= 500; i++) {
		sol[i][1] = 1;
		for (ll j = i - 1, rng = 0; j >= 2; j--, rng++) {
			for (ll k = j - 1, vstv = 0; k >= j - 1 - rng; k--, vstv++) {
				sol[i][j] += (sol[j][k] * get(vstv, rng)) % 100003;
				sol[i][j] %= 100003;
			}
		}
	}
}

inline void task() {
	ll n;
	scanf("%lld", &n);
	
	ll r = 0;
	for (ll i = 1; i < n; i++) {
		r += sol[n][i];
		r %= 100003;
	}
		
	printf("%lld\n", r);
}

int main() {
	prp();
	//fprllf(stderr, "done\n");
	ll t;
	scanf("%lld", &t);
	for (ll i = 1; i <= t; i++) {
		printf("Case #%lld: ", i);
		task();
	}
}

