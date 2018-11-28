#include <iostream>
#include <cmath>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)

typedef long long ll;
int x[1010001], a[1000101];
int n, d;

ll abs(ll x) {
	return (x >= 0 ? x : -x);
}

bool can(ll m) {
	ll cur = -ll(1E17);
	forn(i, n)
		forn(j, a[i]) {
			ll ps = max(cur + d, x[i] - m);
			if (abs(ps - x[i]) > m) return false;
			cur = ps;
		}
	return true;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for (int tc = 1; tc <= tk; ++tc) {
    	
		cin >> n >> d;
		d *= 2;
		forn(i, n) {
			cin >> x[i] >> a[i];
			x[i] *= 2;
		}

		ll l = 0, r = ll(1E15);

		while (r != l) {
			ll m = (l + r) >> 1;

			if (can(m)) r = m;
			else l = m + 1;
		}

		long long ans = r;

		printf("Case #%d: ", tc);

		cout << ans / 2;
		if (ans % 2 != 0) printf(".5\n");
		else printf(".0\n");

    	fprintf(stderr, "Solved %d\n", tc);
    }
	
	return 0;
}