#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

const double EPS = 1e-10;
const int ITERS = 100;

int n, w, l;
double res;
vector<pair<int, int> > r;
vector<pair<int, int> > ans;

void solve() {
	scanf("%d%d%d", &n, &w, &l);
	r.resize(n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &r[i].first);
		r[i].second = i;
	}
	ans.assign(n, make_pair(-1, -1));
	random_shuffle(r.begin(), r.end());
	int curx = -r[0].first, cury = 0;
	int maxr = 0;
	bool firstline = true;
	for (int i = 0; i < n; ++i) {
		if (curx + r[i].first > w) {
			curx = -r[i].first;
			cury += 2 * maxr;
			firstline = false;
		}
		ans[r[i].second] = make_pair(curx + r[i].first, firstline ? 0 : cury + r[i].first);
		//fprintf(stderr, "%d %d\n", ans[r[i].second].first, ans[r[i].second].second);
		assert(ans[r[i].second].first <= w && ans[r[i].second].second <= l);
		maxr = max(maxr, r[i].first);
		curx += 2 * r[i].first;
	}
	for (int i = 0; i < n; ++i) {
		printf("%d %d ", ans[i].first, ans[i].second);
	}
	printf("\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	srand(time(NULL));
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		fprintf(stderr, "Case #%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
