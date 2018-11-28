#include <stdio.h>
#include <math.h>
int abs(int i) {
	return (i < 0 ? -i : i);
}

int main() {
	int tc;
	scanf("%d", &tc);
	int i, j, k, m, r;
	char c[10];
	int poso, posb;
	for (i = 0; i < tc; i++) {
		poso = posb = 1;
		scanf("%d", &j);
		m = 0;
		int res = 0;
		while (j--) {
			scanf("%s %d", c, &k);
			//printf("O=%d, B=%d, m=%d, (%c=>%d)", poso, posb, m, c[0], k);
			if (c[0] == 'O') {
				r = abs(poso-k);
				if (m < 0) {
					m -= r+1;
					res += r+1;
				} else if (m < r) {
					m = m - r - 1;
					res -= m;
				} else {
					m = -1;
					res -= m;
				}
				poso = k;
			} else {
				//int n = -m;
				r = abs(posb-k);
				if (m > 0) {
					m += r+1;
					res += r+1; 
				} else if (-m < r) {
					m = r + m + 1;
					res += m;
				} else {
					m = 1;
					res += m;
				}

				posb = k;
			}
			//printf(", total = %d\n", res);
		}
		printf("Case #%d: %d\n", i+1, res);
	}
}

