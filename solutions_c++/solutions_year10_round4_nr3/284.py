#include <cstdio>
#include <iostream>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;
#include <vector>


set<pair<int, int> > live;
vector<pair<int, int> > born, die;

bool step() {
//	cerr << live.size() << endl;
	born.clear();
	die.clear();
	for (set<pair<int, int> >::iterator w = live.begin(); w != live.end(); ++w) {
		int i = w->first;
		int j = w->second;
		if ((live.count(make_pair(i - 1, j)) == 0) && (live.count(make_pair(i, j - 1)) == 0))
			die.push_back(make_pair(i, j));
		if ((live.count(make_pair(i - 1, j + 1)) == 1) && (live.count(make_pair(i, j + 1)) == 0))
			born.push_back(make_pair(i, j + 1));
	}
	for (int i = 0; i < born.size(); ++i)
		live.insert(born[i]);
	for (int i = 0; i < die.size(); ++i)
		live.erase(die[i]);
	return (live.size() != 0);
}

void solve() {
	int n;
	scanf("%d", &n);
	live.clear();
	born.clear();
	die.clear();
	for (int w = 0; w < n; ++w) {
		int x1, x2, y1, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		if (x1 > x2) swap(x1, x2);
		if (y1 > y2) swap(y1, y2);
		for (int i = x1; i <= x2; ++i)
			for (int j = y1; j <= y2; ++j)
				if (live.count(make_pair(i, j)) == 0)
					live.insert(make_pair(i, j));
	}
	int T = 1;
	while (true) {
		if (step()) ++T; else break;
	}
	printf("%d\n", T);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		cerr << i << endl;
		printf("Case #%d: ", i);
		solve();
	}
}
