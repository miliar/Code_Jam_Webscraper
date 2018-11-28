#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;

namespace gcj {

	void solve() {
		int tc;
		scanf("%d", &tc);
		for (int ti = 1; ti <= tc; ti++) {
			int min = 2000000, m = 0, t = 0, n, k;
			scanf("%d", &n);
			for (int i = 0; i < n; i++) {
				scanf("%d", &k);
				min = std::min(min, k);
				m = m ^ k;
				t += k;
			}
			if (m) {
				printf("Case #%d: NO\n", ti);
			} else {
				printf("Case #%d: %d\n", ti, t - min);
			}
		}
 	}
}

int main() {

	gcj::solve();
	return 0;
}