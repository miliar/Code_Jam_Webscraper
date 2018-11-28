#include <cstdio>
#include <algorithm>
using namespace std;
struct Person{
	int r;
	int x, y;
} p[1000];
int ptt[10]; // ...
int main() {
	int t, n, W, L;
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ++ti) {
		scanf("%d%d%d", &n, &W, &L);
		for (int i = 0; i != n; ++i) {
			scanf("%d", &(p[i].r));
		}
		for (int i = 0; i < n; ++i) ptt[i] = i;
		int x = 0, y = 0, yn = 0;
		do {
			bool ok = true;
			for (int i = 0; i != n; ++i) {
				int ii = ptt[i];
				if (x != 0) x += p[ii].r;
				if (x > W) { // cannot put the current
					x = 0;
					y = yn;
					if (y > L) {
						ok = false;
						break;
					}
				}
				p[ii].x = x;
				p[ii].y = y;
				if (y != 0) p[ii].y += p[ii].r;
				if (p[ii].y > L) { // cannot put anymore
					ok = false;
					break;
				}
				x = p[ii].x + p[ii].r;
				yn = max(yn, p[ii].y + p[ii].r);
			}
			if (ok) {
				printf("Case #%d:", ti);
				for (int i = 0; i != n; ++i) {
					printf(" %d %d", p[i].x, p[i].y);
				}
				putchar('\n');
				break;
			}
		} while (next_permutation(ptt, ptt + n));
	}
	return 0;
}