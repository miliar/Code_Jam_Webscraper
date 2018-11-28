#include <cstdio>
using namespace std;

typedef long long ll;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int tt = 1; tt <= tc; ++tt) {
		ll n, req, end, time, dist[55], spd[55];
		scanf("%lld %lld %lld %lld", &n, &req, &end, &time);
		for (int i = 0; i < n; ++i) {
			scanf("%lld", &dist[i]);
		}
		for (int i = 0; i < n; ++i) {
			scanf("%lld", &spd[i]);
		}

		ll done = 0, swap = 0, pos = n-1, slows = 0;

		while (pos >= 0 && done < req) {
			// can this chick finish (if unblocked)?
			if (spd[pos]*time >= end-dist[pos]) {
				swap += slows;
				++done;
			} else {
				++slows;
			}
			--pos;
		}

		if (done >= req) {
			printf("Case #%d: %lld\n", tt, swap);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}
	}
}
