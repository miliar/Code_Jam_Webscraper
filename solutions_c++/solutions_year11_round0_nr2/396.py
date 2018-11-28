#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 105
char a[N][N];
char b[N][N];
char res[N];

char c[N];
int nr;
int u[N];

int i, j, k, n, m, x, y, z, t, T, tt;



int main() {
	freopen("b-large.in", "r", stdin);	freopen("b-large.out", "w", stdout);

	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		memset(a, -1, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(u, 0, sizeof(u));
		cin >> n;
		for (j = 0; j < n; j++) {
			cin >> c;
			x = c[0] - 'A';
			y = c[1] - 'A';
			z = c[2] - 'A';
			a[x][y] = a[y][x] = z;
		}

		cin >> n;
		for (j = 0; j < n; j++) {
			cin >> c;
			x = c[0] - 'A';
			y = c[1] - 'A';
			b[x][y] = b[y][x] = 1;
		}
		cin >> n >> c;
		nr = 0;
		for ( i= 0; i < n; i++) {
			c[i] -= 'A';
		}
		for (i = 0; i < n; i ++) {
			if (nr == 0) {
				res[nr++] = c[i];
				continue;
			}
			x = res[nr-1];
			y = c[i];
			if (a[x][y] != -1) {
				res[nr-1] = a[x][y];
				continue;
			}
			x = c[i];
			for (j = 0; j < nr; j ++) {
				y = res[j];
				if (b[x][y] == 1) {
					nr = 0;
					break;
				}
			}
			if (nr != 0) {
				res[nr++] = c[i];
			}
		}
		printf("Case #%d: [", tt);
		for (i = 0; i < nr; i ++) {
			if (i > 0) {
				printf(", ");
			}
			printf("%c", (char)(res[i]+'A'));
			
		}
		printf("]\n");
	}
	return 0;
}

