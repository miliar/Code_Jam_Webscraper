#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int casei, cases, n, m, area;

inline void init() {
	scanf("%d%d%d", &n, &m, &area);
}

inline void process() {
	printf("Case #%d: ", casei);
	for (int px1 = 0; px1 <= n; ++px1)
		for (int py1 = 0; py1 <= m; ++py1)
			for (int px2 = 0; px2 <= n; ++px2)
				for (int py2 = 0; py2 <= m; ++py2) if (abs(px1 * py2 - px2 * py1) == area) {
					printf("%d %d %d %d %d %d\n", 0, 0, px1, py1, px2, py2);
					return;
				}
	printf("IMPOSSIBLE\n");
}

int main() {
//	freopen("in.txt", "r", stdin); freopen("", "w", stdout);
	freopen("B-small-attempt0.in", "r", stdin); freopen("B-small.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
	}
}
