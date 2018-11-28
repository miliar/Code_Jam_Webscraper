#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

#define maxn (1 << 10)
#define eps 1e-9

#define rabs(x) fabsl(x)
typedef long double real;

int x[maxn], y[maxn], z[maxn], p[maxn], n;

real r[3];

//inline real rabs(real x) { return x < 0.0 ? -x : x; }

inline real dist(real x1, real y1, real z1, real x2, real y2, real z2) {
	return rabs(x1-x2) + rabs(y1-y2) + rabs(z1-z2);
}

real find(int lv) {
	int i;
	if(lv == 3) {
		real ans = 0.0;
		for(i = 0; i < n; i++)
			ans = std::max(ans, dist(r[0], r[1], r[2], x[i], y[i], z[i]) / p[i]);
		return ans;
	}
	real ll = 0.0, rr = 1e6;
	while(rr-ll > eps) {
		real v1 = (3.0*ll+rr) * 0.25; r[lv] = v1;
		real f1 = find(lv+1);
		real v2 = (rr+ll) * 0.5; r[lv] = v2;
		real f2 = find(lv+1);
		real v3 = (ll+rr*3.0) * 0.25; r[lv] = v3;
		real f3 = find(lv+1);
		if(f1 < f3 && f1 <= f2) rr = v2;
		else if(f3 < f1 && f3 <= f2) ll = v2;
		else {
			ll = v1;
			rr = v3;
		}
	}
	r[lv] = (ll+rr)*0.5;
	return find(lv+1);
}

int main() {
	int t, tc;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		int i, j;
		scanf("%d", &n);
		for(i = 0; i < n; i++) scanf("%d%d%d%d", x+i, y+i, z+i, p+i);
		printf("Case #%d: %.8Lf\n", t, find(0));
	}
	return 0;
}
