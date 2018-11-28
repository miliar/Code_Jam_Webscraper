#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
	double t, tt, ans;
	int re, x, s, r, n, b, e, w;
	vector<pair<int, int> > v;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
		v.clear();
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &b, &e, &w);
			e -= b;
			x -= e;
			v.push_back(make_pair(w, e));
		}
		v.push_back(make_pair(0, x));
		sort(v.begin(), v.end());

		ans = 0;
		for (int i = 0; i < (int)v.size(); ++i) {
			w = v[i].first;
			e = v[i].second;
			tt = min(t, 1.0 * e / (w + r));
		//	printf("> %d %d %lf + %lf\n", w, e, tt, (e - tt * (w + r)) / (w + s));
			t -= tt;
			ans += tt + (e - tt * (w + r)) / (w + s);
		}
		printf("Case #%d: %.10lf\n", ri, ans);
	}

	return 0;
}

