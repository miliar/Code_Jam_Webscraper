#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
#define N 5005

char a[N][20];
int b[30][30];

int i, j, k, n, m, l, t, r, T, x;
char c[N];
int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	cin >> l >> n >> m;
	for (i = 0; i < n; i ++) {
		cin >> a[i];
	}

	for (t = 1; t <= m; t ++) {
		cin >> c;
		memset(b, 0, sizeof(b));
		r = 0;
		k = 0;
		for (j = 0; c[j] != 0; j ++) {
			if (c[j] == '(') {
				j ++;
				while (c[j] != ')') {
					b[k][c[j] - 'a'] = 1;
					j ++;
				}
			} else {
				b[k][c[j]-'a'] = 1;
			}
			k ++;
		}
		for (j = 0; j < n; j ++) {
			for (k = 0; k < l; k ++) {
				x = a[j][k]-'a';
				if (b[k][x] == 0) {
					break;
				}
			}
			if (k == l) {
				r ++;
			}
		}
		printf("Case #%d: %d\n", t, r);
	}
	return 0;
}


