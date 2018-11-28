#include <stdio.h>
#include <algorithm>
using namespace std;

int i, j, k, n, t, tt, p;
int m[1024];
int a[10][512];

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		scanf("%d", &p);
		for (i = 0; i < (1 << p); i++) {
			scanf("%d", &m[i]);
		}
		for (i = p - 1; i >= 0; i--) {
			for (j = 0; j < (1 << i); j++) scanf("%d", &a[i][j]);
		}

		int cnt = 0;
		for (i = 0; i < p; i++) {
			for (j = 0; j < (1 << i); j++) {
				for (k = 0; k < (1 << (p - i)); k++) {
					if (m[k + j * (1 << (p - i))] < p) break;
				}
				if (k != (1 << (p - i))) {
					cnt++;
					for (k = 0; k < (1 << (p - i)); k++) {
						m[k + j * (1 << (p - i))]++;
					}
				}
			}
		}

		printf("%d\n", cnt);
	}
	return 0;
}

