#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>

int x1, y1, x2, y2, n, m, s;

bool good(int x1, int y1, int x2, int y2) {
	if(y2 < 0 || y2 > m) return false;
	return abs(x1*y2-x2*y1) == s;
}

int main() {
	int t, tc;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		scanf("%d%d%d", &n, &m, &s);
		for(x1 = 0; x1 <= n; x1++)
			for(y1 = 0; y1 <= m; y1++)
				for(x2 = 0; x2 <= n; x2++) {
					y2 = x1 ? (s + x2*y1) / x1 : 0;
					if(good(x1, y1, x2, y2)) {
						printf("Case #%d: 0 0 %d %d %d %d\n", t, x1, y1, x2, y2);
						goto bugoga;
					}
					y2 = x1 ? (s - x2*y1) / x1 : 0;
					if(good(x1, y1, x2, y2)) {
						printf("Case #%d: 0 0 %d %d %d %d\n", t, x1, y1, x2, y2);
						goto bugoga;
					}
				}
		printf("Case #%d: IMPOSSIBLE\n", t);						
bugoga:
		;
	}
	return 0;
}
