#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int i, j, k, n, t, tt, R, T,x1,y1,x2,y2;
char b[105][105], a[105][105];

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		scanf("%d", &R);
		memset(a, '0', sizeof(a));
		for (i = 0; i < R; i++) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (j = y1; j <= y2; j++) {
				for (k = x1; k <= x2; k++) {
					a[j][k] = '1';
				}
			}
		}
		T = 0;
		bool dead = true;
		do {
			dead = true;
			T++;
			memset(b, '0', sizeof(b));
			for (i = 1; i <= 100; i++) {
				for (j = 1; j <= 100; j++) {
					if (a[i][j] == '1' && a[i-1][j] == '0' && a[i][j-1] == '0') b[i][j] = '0';
					else if (a[i][j] == '0' && a[i-1][j] == '1' && a[i][j-1] == '1') b[i][j] = '1';
					else b[i][j] = a[i][j];
					if (b[i][j] == '1') dead = false;
				}
			}
			for (i = 1; i <= 100; i++) {
				for (j = 1; j <= 100; j++) {
					a[i][j] = b[i][j];
				}
			}
		} while(!dead);
		printf("%d\n", T);
	}
	return 0;
}
