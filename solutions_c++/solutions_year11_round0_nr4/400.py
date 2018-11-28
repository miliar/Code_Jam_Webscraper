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
#define inf 1e10
int dp[N];

int a[N];
int u[N];
double res, t;
int i, j, k, n, x, y, z, T, tt;

int main() {
	freopen("d-large.in", "r", stdin);	freopen("d-large.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%d", &n);
		for (i=  0; i <n ; i++) {
			scanf("%d", &a[i]);
			a[i] --;
			u[i] = 0;
		}
		res = 0;
		for (i = 0; i < n; i ++) {
			if (u[i] == 0) {
				x = 0;
				y = i;
				while (u[y] == 0) {
					x ++;
					u[y] = 1;
					y = a[y];
				}
				if (x > 1) {
					res += x;
				}
			}
		}
		printf("Case #%d: %.6lf\n", tt, res);
	}
	return 0;
}
