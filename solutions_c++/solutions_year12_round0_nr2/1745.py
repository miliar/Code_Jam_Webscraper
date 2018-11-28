#include <cstdio>
#define min(a,b) (a<b)?(a):(b)
int main() {
	int t, n, s, p, m, r, c;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		scanf("%d%d%d", &n, &s, &p);
		r = c = 0;
		for (int j = 0; j != n; ++j) {
			scanf("%d", &m);
			if (m >= p*3-2) {
				++r;
			} else if (m >= p && m >= p*3-4) {
				++c;
			}
		}
		r += min(s, c);
		printf("Case #%d: %d\n", i, r);
	}
	return 0;
}