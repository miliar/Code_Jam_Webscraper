


/*
	Prob: (Google code jam 2011 - Qualification Round - C)
	Author: peanut
	Time: 07/05/11 20:05
	Description: ^_^ - xor
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int T, N, c, s, v, minV;

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++ cs) {
		scanf("%d", &N);
		c = s = 0;
		minV = 0x7fffffff;
		for (int k = 1; k <= N; ++ k) {
			scanf("%d", &v);
			c ^= v; s += v; minV <?= v;
		}
		if (c) printf("Case #%d: NO\n", cs);
		else printf("Case #%d: %d\n", cs, s - minV);
	}
	
	return 0;
}
