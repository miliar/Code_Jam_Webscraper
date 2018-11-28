#include <stdio.h>
#include <set>

using namespace std;

typedef long long ll;

set<ll> m[2];

inline bool outbound(ll v) {
	return (v > 1048577000000 || (v & 1048575) > 1000000);
}

ll xy(int x, int y) {
	return x * (ll)1048576 + y;
}

int main(int argc, char const* argv[])
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 0; ti < tc; ti++) {
		int live = 0;
		m[0].clear();
		{
		int r;
		scanf("%d", &r);
		for (int i = 0; i < r; i++) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x++) {
				ll xb = x * (ll)1048576;
				for (int y = y1; y <= y2; y++) {
					if (m[0].count(xb + y) == 0) {
						m[0].insert(xb + y);
						live++;
					}
				}
			}
		}
		}

		int um = 0, tm = 1;
		long long r = 0;
		while(m[um].size() > 0) {
			m[tm].clear();
			for (set<ll>::iterator it = m[um].begin(); it != m[um].end(); ++it) {
				// check dead
				if (m[um].count(*it - 1048576) || m[um].count(*it - 1)) {
					// still alive
					m[tm].insert(*it);
				} else {
					// dead
					//live--;
				}
				// check new, this as left, match top
				if (m[um].count(*it + 1048576 - 1) > 0 && !outbound(*it + 1048576)
					&& m[um].count(*it + 1048576) == 0) {
					m[tm].insert(*it + 1048576);
					//live++;
				}
			}
			um = 1 - um;
			tm = 1 - tm;
			r ++;
			// printf("%d %lld %d\n", live, r, m[um].size());
		}
		printf("Case #%d: %lld\n", ti + 1, r);
	}
	return 0;
}
