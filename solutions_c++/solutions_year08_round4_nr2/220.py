#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <string>

using namespace std;

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n, m, a;
		scanf("%d %d %d", &n, &m, &a);
		printf("Case #%d: ", tt + 1);
		bool f = false;
		for (int x1 = 0; x1 <= n; ++x1) {
			for (int y1 = 0; y1 <= m; ++y1) if (x1 || y1) {
				for (int x2 = 0; x2 <= n; ++x2) {
					for (int y2 = 0; y2 <= m; ++y2) if ((x2 || y2) && ((x2 != x1) || (y2 != y1))) {
						int s = (x1 * y2 - x2 * y1);
						if (s < 0) s = -s;
						if (s == a) {
							printf("%d %d %d %d %d %d\n", 0, 0, x1, y1, x2, y2);
							f = true;
							break;
						}
					}
					if (f) break;
				}
				if (f) break;
			}
			if (f) break;
		}
		if (!f) printf("IMPOSSIBLE\n");
	}
	return 0;
}
