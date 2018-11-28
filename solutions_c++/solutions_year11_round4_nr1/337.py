#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <functional>
using namespace std;

struct Walkway {
	double len;
	double v;
	void read() {
		double s,e;
		scanf("%lf%lf%lf", &s, &e, &v);
		len = e-s;
	}
	bool operator<(const Walkway &b) const {
		return v < b.v;
	}
}w[1024];

int main() {
	int T;
	int var = 0;

	scanf("%d", &T);
	while( T -- ) {
		double x, s, r, t;
		int n;
		scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
		for (int i = 0 ; i < n ; i ++ ) {
			w[i].read();
			x -= w[i].len;
		}
		w[n].v = 0;
		w[n].len = x;
		n ++;
		sort(w, w+n);
		double ans = 0;
		for (int i = 0 ; i < n ; i ++ ) {
			if (fabs(t) > 0) {
				if (t * (r + w[i].v) <= w[i].len) {
					ans += t;
					ans += (w[i].len - t * (r + w[i].v)) / (s + w[i].v);
					t = 0;
				} else {
					ans += w[i].len / (w[i].v + r);
					t -= w[i].len / (w[i].v + r);
				}
			} else {
				ans += w[i].len / (w[i].v + s);
			}
		}
		printf("Case #%d: %.7f\n", ++var, ans);
	}
	return 0;
}
