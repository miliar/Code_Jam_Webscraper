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
#define eps 0.1

struct st {
	double r;
	int k;
};

st a[N];
double rx[N], ry[N];
int pr(st a, st b) {
	return a.r > b.r;
}

int i, j, k, n, m;
double t, r, x, y, z, dx, yy;
double mx, my;

int tt, T;


int main() {
	freopen("large.in", "r", stdin);	freopen("large.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%d%lf%lf", &n, &mx, &my);
		for (i = 0; i < n; i ++) {
			scanf("%lf", &a[i].r);
			a[i].k = i;
		}
		sort(a, a + n, pr);
		x = 0;
		y = 0;
		k = 0;
		dx = a[0].r;
		while (k < n) {
			if (y > my - eps) {
				x += dx + a[k].r + eps;
				dx = a[k].r;
				y = 0;
			}
			rx[a[k].k] = x;
			ry[a[k].k] = y;
			y += a[k].r + a[k+1].r + eps;
			k ++;
		}

		printf("Case #%d:", tt);
		for (i = 0; i < n; i ++) {
			printf(" %.4lf %.4lf", rx[i], ry[i]);
		}
		printf("\n");
	}
	return 0;
}



/*
50

2 6 6

1 1

3 320 2

2 4 3 

*/


	


