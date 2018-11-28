#include <string>
#include <cstdio>
using namespace std;

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t, T, n, i, c, total, min, x;
	for (t = 1, scanf("%d", &T); t <= T; t++) {
		scanf("%d", &n);
		min = 9999999;
		total = 0;
		x = 0;
		for (i = 0; i < n; i++) {
			scanf("%d", &c);
			if (c < min) min = c;
			total += c;
			x ^= c;
		}
		printf("Case #%d: ", t);
		if (x == 0) {
			printf("%d\n", total - min);
		} else {
			printf("NO\n");
		}
	}
	fclose(stdout);
	return 0;
}
