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

#define N 1005
#define inf 1000000000

int a[N][N];

int ab(int x) {
	return x >= 0 ? x : -x;
}

int maax(int x, int y) {
	return x > y ? x : y;
}
int f1(int n, int i) {
	if (i < n) {
		return n - 1 - i;
	} else {
		return n - 1 - (2*n-2-i);
	}
}
int f2(int n, int i) {
	if (i < n) {
		return n - 1 + i;
	} else {
		return n - 1 + (2*n-2-i);
	}
}
int s(int x) {
	return x*x;
}

int test(int x, int y, int n) {
	int i, j, xx, yy;
	for ( i= 0;i < n; i ++) {
		for (j = 0; j < n; j ++) {
			if (x + x - i >= 0) {
				if (a[i][j] != a[x + x-i][j] && a[i][j] != -1 && a[x+x-i][j] != -1) {
					return 0;
				}
			}
			if (y + y - j >= 0) {
				if (a[i][j] != a[i][y + y - j] && a[i][j] != -1 && a[i][y+y-j] != -1) {
					return 0;
				}
			}
		}
	}
	return 1;
}

int i, j, k, n, m, x, y, z, t, T, tt, res;

int main() {
	freopen("large.in", "r", stdin);	freopen("large.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		for (i = 0; i < N; i ++) {
			for (j = 0; j < N; j ++) {
				a[i][j] = -1;
			}
		}
		scanf("%d", &n);
		for (i = 0; i < 2*n-1; i ++) {
			m = f1(n, i);
			k = f2(n, i);
			for (j = m; j <= k; j += 2) {
				scanf("%d", &a[i][j]);
			}
		}
		res = inf;
		for (i = 0; i <= 2*n; i ++) {
			for (j = 0; j <= 2 * n; j ++) {
				t = test(i, j, 2*n + 2);
				if (t == 1) {
					z = s(n + ab(i-(n-1)) + ab(j-(n-1))) - s(n);
					if (z < res) {
						res = z;
					}
				}
			}
		}



		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}

/*

1
2
 1
2 3
 4
 
 
*/