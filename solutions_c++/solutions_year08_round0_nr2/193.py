#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int k, n, m; scanf("%d %d %d", &k, &n, &m);
		vector<pair<pair<int, int>, int> > v;
		for (int i = 0; i < n; ++i) {
			int sh, sm, th, tm;
			scanf("%d:%d %d:%d", &sh, &sm, &th, &tm);
			v.push_back(make_pair(make_pair(sh * 60 + sm, th * 60 + tm), 1));
		}
		for (int i = 0; i < m; ++i) {
			int sh, sm, th, tm;
			scanf("%d:%d %d:%d", &sh, &sm, &th, &tm);
			v.push_back(make_pair(make_pair(sh * 60 + sm, th * 60 + tm), 2));
		}
		sort(v.begin(), v.end());
		int a = 0, b = 0;
		for (int i = 0; i < n + m; ++i) if (v[i].second) {
			if (v[i].second == 1) ++a;
			else ++b;
			int x = i, y = v[i].second;
			for (int j = i + 1; j < n + m; ++j) if (v[j].second && (v[j].second != y)) {
				if (v[j].first.first >= v[x].first.second + k) {
					x = j;
					y = v[j].second;
					v[j].second = 0;
				}
			}
		}
		printf("Case #%d: %d %d\n", t + 1, a, b);
	}
	return 0;
}
