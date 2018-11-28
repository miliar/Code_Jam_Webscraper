#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct st {
	double d, s;
	st(double d, double s) :
		d(d), s(s) {

	}
};

bool operator <(st a, st b) {
	return a.s < b.s;
}

int main() {
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		double X, S, R, t;
		int n;
		scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t, &n);
		vector<st> V;
		double lasten;
		for (int i = 0; i < n; ++i) {
			double be, en, sp;
			scanf("%lf %lf %lf", &be, &en, &sp);
			if (i == 0 && be > 0.5) {
				V.push_back(st(be, S));
			} else if (i > 0 && be > lasten + 0.5) {
				V.push_back(st(be - lasten, S));
			}
			V.push_back(st(en - be, S + sp));
			lasten = en;
		}
		if (lasten < X - 0.5) {
			V.push_back(st(X - lasten, S));
		}
		double ans = 0;
		double runTime = 0;
		sort(V.begin(), V.end());
		for (int i = 0; i < V.size(); ++i) {
			double rt = 0;
			if (runTime < t) {
				rt = min(t - runTime, V[i].d / (V[i].s + R - S));
			}
			ans += rt + (V[i].d - rt * (V[i].s + R - S)) / V[i].s;
			runTime += rt;
		}
		printf("Case #%d: %.10lf\n", test, ans);
	}
	return 0;
}
