#include <set>
#include <cstdio>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
	int re, n, x1, y1, x2, y2, ans;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &n);
		set<pair<int, int> > s;
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = x1; i <= x2; ++i) {
				for (int j = y1; j <= y2; ++j) {
					s.insert(make_pair(i, j));
				}
			}
		}
		ans = 0;
		while (!s.empty()) {
			++ans;
			set<pair<int, int> > t;
			// printf("--- %d ---\n", ans);
			for (set<pair<int, int> >::const_iterator i = s.begin(); i != s.end(); ++i) {
				int x = i->first;
				int y = i->second;
				// printf("%d %d\n", x, y);
				if (s.count(make_pair(x - 1, y)) || s.count(make_pair(x, y - 1))) {
					t.insert(*i);
				}
				if (s.count(make_pair(x - 1, y + 1))) {
					t.insert(make_pair(x, y + 1));
				}
				if (s.count(make_pair(x + 1, y - 1))) {
					t.insert(make_pair(x + 1, y));
				}
			}
			s.swap(t);
		}

		printf("Case #%d: %d\n", ri, ans);
	}

	return 0;
}

