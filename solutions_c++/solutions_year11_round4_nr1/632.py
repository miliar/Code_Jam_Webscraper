#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

struct Walkway {
	int b, e, s;
	bool operator < (const Walkway& rhs) const
	{
		return s < rhs.s;
	}
};

Walkway a[1024];
Walkway w[2048];

void solve(void)
{
	int X, s, r, tmax, nn;
	scanf("%d%d%d%d%d", &X, &s, &r, &tmax, &nn);
	for (int i = 0; i < nn; i++) {
		scanf("%d%d%d", &a[i].b, &a[i].e, &a[i].s);
	}
	int n = 3;
	w[0].b = 0;
	w[0].e = a[0].b;
	w[0].s = 0;
	w[1].b = a[nn-1].e;
	w[1].e = X;
	w[1].s = 0;
	w[2] = a[0];
	for (int i = 1; i < nn; i++) {
		w[n].b = a[i - 1].e;
		w[n].e = a[i].b;
		w[n].s = 0;
		n++;
		w[n++] = a[i];
	}
	sort(w, w + n);
	double t = 0;
	double tr = tmax;
	for (int i = 0; i < n; i++) {
		double y = w[i].e - w[i].b;
		if (y < tr * (r + w[i].s)) {
			double tt = y / (r + w[i].s);
			t += tt;
			tr -= tt;
		} else {
			y -= tr * (r + w[i].s);
			t += tr;
			tr = 0;
			if (y > 0) {
				double tt = y / (s + w[i].s);
				t += tt;
			}
		}
	}
	printf("%.7lf\n", t);
}


int main(void)
{
// 	freopen("a.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
