/*
 * A.cpp
 *
 *  Created on: 2010-5-8
 *      Author: aaahexing
 */

#include <set>
#include <map>
#include <cctype>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 101;

int s, p, q, n, k, cas, v[MAXN];

inline bool ok(int n) {
	for (int i = 1; i <= n; i ++)
		if (! v[i])
			return false;
	return true;
}

inline bool gao(int n, int k) {
//	for (int i = 1; i <= n; i ++)
//		v[i] = 0;
//	v[0] = 1;
//	for (p = 0; ! ok(n); p ++) {
////		for (int i = 1; i <= n; i ++)
////			printf("%d ", v[i]);
////		puts("");
//
//		for (s = 0; s <= n && v[s]; s ++);
//		for (int i = 1; i <= s; i ++)
//			v[i] = !v[i];
//	}
////	printf("p = %d, k = %d\n", p, k);
	p = (1 << n) - 1;
	return (k >= p) && ((k-p)%(p+1) == 0);
}

int main() {
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
//	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

	setbuf(stdout, NULL);

	scanf("%d", &cas);
	for (int c = 1; c <= cas; c ++) {
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", c, gao(n, k) ? "ON" : "OFF");
	}

	return 0;
}
