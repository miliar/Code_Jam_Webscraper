#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

int go() {
	int r;
	scanf("%d", &r);
	set<pair<int,int> > s, ns;
	for (int i=  0;i < r; ++i) {
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		if (x1 > x2) swap(x1, x2);
		if (y1 > y2) swap(y1, y2);
		for (int i = x1-1; i < x2; ++i)
			for (int j = y1-1; j < y2; ++j) {
				s.insert(make_pair(i, j));
			}
	}
	for (int r = 0; ;++r) {
		if (s.size() == 0) return r;
		for (auto it = s.begin(); it != s.end(); ++it) {
			if (s.count(make_pair(it->first - 1, it->second)) || s.count(make_pair(it->first, it->second - 1)))
				ns.insert(*it);
			if (s.count(make_pair(it->first + 1, it->second - 1)))
				ns.insert(make_pair(it->first + 1, it->second));
		}
		ns.swap(s);
		ns.clear();
	}
}

int main() {
	freopen("C-small-attempt0 (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int c;
	scanf("%d", &c);
	for (int i = 0; i < c; ++i) {
		fprintf(stderr, "%d\n", i);
		printf("Case #%d: %d\n", i+1, go());
	}
}