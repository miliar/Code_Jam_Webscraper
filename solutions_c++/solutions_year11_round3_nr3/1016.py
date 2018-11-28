
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;

ll mdc(ll a, ll b) {
	if (b == 0) return a;
	return mdc(b, a%b);
}
#define NN 11000
ll v[NN];

int main() {
	int T;
	scanf("%d", &T);
	for (int ct = 1; ct <= T; ct++) {
		int n, l, h; scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; i++)
			scanf("%lld", &v[i]);

		int i, ok;
		for (i = l; i <= h; i++) {
			ok = 1;
			for (int j = 0; j < n; j++)
				if (i % v[j] != 0 && v[j] % i != 0) {
					ok = 0; break;
				}
			if (ok) break;
		}

		if (!ok) printf("Case #%d: NO\n", ct);
		else printf("Case #%d: %lld\n", ct, i);
	}
	return 0;
}
