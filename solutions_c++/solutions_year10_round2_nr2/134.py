#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, k, b, tt;
		scanf("%d%d%d%d", &n, &k, &b, &tt);
		vector<int> x(n), v(n);
		vector<pair<int, double> > time(n);
		for (int i = 0; i < n; i++) scanf("%d", &x[i]);
		for (int i = 0; i < n; i++) scanf("%d", &v[i]);

		for (int i = 0; i < n; i++) {
			double ti = 1.0 * (b - x[i]) / v[i];
			time[i] = make_pair(i, ti);
		}

		int res = 0;
		int poss = 0;
		sort(time.rbegin(), time.rend());
		for (int i = 0; i < n; i++) {
			if (time[i].second <= tt) {
				poss++;
				for (int j = 0; j < n; j++) {
					if (time[i].first < time[j].first && time[j].second > tt) res++;
				}
				if (poss >= k) break;
			}
		}
		if (poss >= k) printf("Case #%d: %d\n", t, res);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}