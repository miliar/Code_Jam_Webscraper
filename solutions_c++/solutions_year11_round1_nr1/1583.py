#include <cstdio>
#include <algorithm>

namespace gcj {
	void print(int t, char* str) {
		printf("Case #%d: %s\n", t, str);
	}

	void solve() {
		int t, n, pd, pg, d, g, l, r;
		scanf("%d", &t);
		for (int i = 0; i < t; i++) {
			scanf("%d %d %d", &n, &pd, &pg);
			for (d = 1; pd && d <= n && d * pd % 100 !=0 ; d ++);
			if (d > n) {
				print(i + 1, "Broken");
				continue;
			}
			if ((pd < 100 && pg == 100)
				|| pd > 0 && pg == 0)
				print(i + 1, "Broken");
			else
				print(i + 1, "Possible");
		}
	}
}

int main () {

	freopen("d:/GCJ/Round1/A-small-attempt1.in", "r", stdin);
	freopen("d:/GCJ/Round1/A-small-attempt1.out", "w", stdout);

	gcj::solve();
	return 0;
}