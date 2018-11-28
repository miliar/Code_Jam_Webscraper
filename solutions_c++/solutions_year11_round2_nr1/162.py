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

double b[N], c[N], p[N], op[N], oop[N];

int i, j, k, n, m, tt, T;
double t, t1, res;
double x, y, z;


int main() {
	freopen("A-large.in", "r", stdin);	freopen("A-large.out", "w", stdout);
		
	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(c, 0, sizeof(c));
		memset(p, 0, sizeof(p));
		memset(op, 0, sizeof(op));
		memset(oop, 0, sizeof(oop));
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> a[i];
		}

		for (i = 0; i < n; i ++) {
			for (j = 0; j < n; j ++) {
				if (a[i][j] == '1') {
					b[i] += 1;
				}
				if (a[i][j] != '.') {
					c[i] += 1;
				}
			}
			p[i] = b[i] / c[i];
		}
		for (i = 0; i < n; i ++) {
			z = 0;
			t = 0;
			for (j = 0; j < n; j ++) {
				if (a[i][j] == '.') {
					continue;
				}
				x = b[j];
				y = c[j];
				if (a[j][i] == '1') {
					x -= 1;
				}
				y -= 1;
				t += x / y;
				z += 1;
			}
			op[i] = t / z;
		}
		for (i = 0; i < n; i ++) {
			x = y = 0;
			for (j = 0; j < n; j ++) {
				if (a[i][j] != '.') {
					x += op[j];
					y += 1;
				}
			}
			oop[i] = x / y;
		}
		printf("Case #%d:\n", tt);
		for (i = 0; i < n; i ++) {
			res = 0.25 * p[i] + 0.5 * op[i] + 0.25 * oop[i];
			printf("%.8lf\n", res);
		}
	}
	return 0;
}
			






