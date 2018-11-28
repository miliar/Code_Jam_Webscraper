#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int tst, n, s, p, c1, c2, x;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &tst);
	for (int _ = 1; _ <= tst; _++){
		scanf("%d%d%d", &n, &s, &p);
		c1 = c2 = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &x);
			if (p + 2 * max(p - 1, 0) <=x)
				c1++;
			else if (p + 2 * max(p - 2, 0) <= x)
				c2++;
		}
		printf("Case #%d: %d\n", _, c1 + min(c2, s));
	}

	return 0;
}
