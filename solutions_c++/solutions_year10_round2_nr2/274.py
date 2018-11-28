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

#define N 55

int a[N], v[N], u[N], b[N], nb;
int i, j, k, n, m, x, y, z, t, tt, T, d, tm, res;


int main() {
	freopen("large.in", "r", stdin);	freopen("large.out", "w", stdout);

	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		cin >> n >> m >> d >> tm;
		for (i = 0; i < n; i ++) {
			cin >> a[i];
		}
		for (i = 0; i < n; i ++) {
			cin >> v[i];
		}
		res = 0;

		for (i = 0; i < n; i ++) {
			if ( (d - a[i]) <= tm*v[i]) {
				u[i] = 1;
			} else {
				u[i] = 0;
			}
		}
		k = 0;
		for (i = n - 1; i >= 0; i --) {
			for (j = i + 1; j < n; j ++) {
				if (a[j] - a[i] < tm * (v[i] - v[j])) {
					if (u[i] == 1 && u[j] == 0) {
						res ++;
					}
				}
			}
			if (u[i] == 1) {
				k ++;
			}
			if (k >= m) {
				break;
			}
		}
		printf("Case #%d: ", tt);
		if (k >= m) {
			printf("%d\n", res);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
					




	