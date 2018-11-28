#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int len, ws, rs, rt, n;
		scanf("%d %d %d %d %d", &len, &ws, &rs, &rt, &n);

		vector<pair<int, pair<int, int> > > ww;

		for (int i = 0; i < n; ++i) {
			int a, b, s;
			scanf("%d %d %d", &a, &b, &s);
			ww.push_back(make_pair(s, make_pair(a, b)));
			len -= b-a;
		}
		ww.push_back(make_pair(0, make_pair(0, len)));

		sort(ww.begin(), ww.end());

		double run = rt;
		double totaltm = 0;

		for (int i = 0; i < ww.size(); ++i) {
			int s = ww[i].first;
			int a = ww[i].second.first;
			int b = ww[i].second.second;

			int dist = b-a;
			len -= dist;
			double tm = (double)dist/(rs+s);
			if (tm <= run) {
				totaltm += tm;
				run -= tm;
			} else {
				double rundist = run*(rs+s);
				double walkdist = dist-rundist;
				totaltm += run + walkdist/(ws+s);
				run = 0;
			}
		}

		printf("Case #%d: %.9lf\n", tt, totaltm);
	}
}
