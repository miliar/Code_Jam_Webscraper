/*
 * C.cpp
 *
 *  Created on: 7 May 2011
 *      Author: Admin
 */

#include<cstdio>
#include<vector>
#include<algorithm>
#define min(A,B) ((A)<(B)?(A):(B))
#define max(A,B) ((A)<(B)?(B):(A))
#define abs(a) ((a)<0?(a)*-1:(a))
using namespace std;

int a[1001];

int main() {

		freopen("C-large.in", "rt", stdin);
		freopen("a.txt", "wt", stdout);

	int t, n, x, sum, mn;
	scanf("%d", &t);
	for (int K = 1; K <= t; ++K) {
		scanf("%d", &n);
		x = 0;
		sum = 0;
		mn = 1000000000;
		for (int i = 0; i < n; ++i) {
			scanf("%d", a + i);
			x ^= a[i];
			sum += a[i];
			mn = min(mn,a[i]);
		}
		sort(a, a + n);
		if (x == 0)
			printf("Case #%d: %d\n", K, sum - mn);
		else
			printf("Case #%d: NO\n", K);
	}

	return 0;
}
