#include <cstdio>
#include <algorithm>

using namespace std;

int n, s, p, x;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		scanf("%d%d%d", &n, &s, &p);
		int q = 0, w = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &x);
			int c = x / 3 + (x % 3 > 0);
			if (c >= p)
				q ++;
			if (c == p-1 && x % 3 != 1 && x >= p)
				w ++;
		}
		q += min(s, w);
		printf("Case #%d: %d\n", test+1, q);
	}
	return 0;
}