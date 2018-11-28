#include <stdio.h>
const int MAXN = 200;

#define ABS(x) ((x) < 0 ? -(x) : (x))
#define MAX(x, y) ((x) > (y) ? (x) : (y))

int n;
char rbt[MAXN];
int btn[MAXN];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int k = 0; k < cases; ++k) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf(" %c %d", &rbt[i], &btn[i]);
		}
		int ans = 0;
		int p0 = 1, p1 = 1;
		int t0 = 0, t1 = 0;
		for (int i = 0; i < n; ++i) {
			if (rbt[i] == 'O') {
				if (ABS(btn[i] - p0) + 1 > MAX(t0, t1) - t0) 
					t0 += ABS(btn[i] - p0) + 1;
				else 
					t0 = t1 + 1;
				p0 = btn[i];
			} else {
				if (ABS(btn[i] - p1) + 1 > MAX(t0, t1) - t1)
					t1 += ABS(btn[i] - p1) + 1;
				else
					t1 = t0 + 1;
				p1 = btn[i];
			}
//			printf("%d %d\n", t0, t1);
		}
		ans = MAX(t0, t1);
		printf("Case #%d: %d\n", k + 1, ans);
	}
	return 0;
}
