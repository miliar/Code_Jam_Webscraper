#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

const int maxn = 10000 + 10;
struct node
{
	int r, id;
} c[maxn];
int n, W, L;
int x[maxn], y[maxn];

bool cmp(node A, node B)
{
	return A.r > B.r;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("BL.out", "w", stdout);
	int TextN, TT = 0;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%d%d%d", &n, &W, &L);
		for (int i = 1; i <= n; i++) {
			scanf("%d", &c[i].r);
			c[i].id = i;
		}
		sort(c+1, c+1+n, cmp);

		if (W <= L) {
			int ox = 0, oy = 0, C = c[1].r;
			for (int k = 1; k <= n; k++) {
				x[c[k].id] = ox, y[c[k].id] = oy;
				if (k == n) break;
				ox += c[k].r + c[k+1].r;
				if (ox > W) {
					ox = 0;
					oy += C + c[k+1].r;
					C = c[k+1].r;
				}
			}
		} else {
			int ox = 0, oy = 0, C = c[1].r;
			for (int k = 1; k <= n; k++) {
				x[c[k].id] = ox, y[c[k].id] = oy;
				if (k == n) break;
				oy += c[k].r + c[k+1].r;
				if (oy > L) {
					oy = 0;
					ox += C + c[k+1].r;
					C = c[k+1].r;
				}
			}
		}
		printf("Case #%d:", ++TT);
		for (int i = 1; i <= n; i++) {
			printf(" %d %d", x[i], y[i]);
		}
		printf("\n");
	}
	return 0;
}
