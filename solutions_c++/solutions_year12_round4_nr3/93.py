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

#define N 2005
#define H 100000000
int a[N], u[N], h[N];

int i, j, k, n, m, x, y, z, t, f;
int tt, T;



int main() {
	freopen("small.in", "r", stdin);	freopen("small.out", "w", stdout);

	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%d", &n);
		for (i = 0; i + 1 < n; i ++) {
			scanf("%d", &a[i]);
			a[i] --;
		}
		for (i = 0; i < n; i ++) {
			u[i] = 0;
			h[i] = H;
		}
		f = 1;
		for (i = 0; i < n; i ++) {
			k = a[i];
			if (u[i] == 0) {
				h[i] = 1;
			}
			u[i] = 1;
			u[k] = 1;
			for (j = i + 1; j < n; j ++) {
				if (j == k) {
					continue;
				}
				t = h[i] + (h[k] - h[i]) * (j - i) / (k - i);
				z = (h[k] - h[i]) * (j - i) % (k - i);
				if (j < k && z == 0) {
					t --;
				}

				if (t < h[j]) {
					if (u[j] == 1) {
						f = 0;
						break;
					}
					h[j] = t;
				}
			}
			if (f == 0) {
				break;
			}
		}
		printf("Case #%d:", tt);
		if (f == 0) {
			printf(" Impossible\n");
			continue;
		}
		for (i = 0; i < n; i ++) {
			printf(" %d", h[i]);
		}
		printf("\n");
	}
	return 0;
}



