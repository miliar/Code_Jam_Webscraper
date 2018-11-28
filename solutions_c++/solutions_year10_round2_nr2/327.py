#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iterator>

using namespace std;

inline void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("D:/Download/B-large.in", "rt", stdin);
	freopen("D:/Download/B-large.out", "wt", stdout);
#endif
}

void solve();

int main() {
	openFiles();
	int t; std::cin >> t;
	while (t--) solve();
	return 0;
}

void solve() {
	int n, k, b, t; std::cin >> n >> k >> b >> t;
	std::vector<int> v(n), x(n);
	for (int i = 0; i < n; ++i) std::cin >> x[i];
	for (int i = 0; i < n; ++i) std::cin >> v[i];
	int sw = 0, cnt = 0, needspaw = 0;
	for (int i = n - 1; i >= 0; --i) {
		int dist = b - x[i];
		double needTime = dist / (double)v[i];
		if (needTime <= t) {
			sw += needspaw;
			if (++cnt == k) break;
		} else {
			++needspaw;
		}
	}
	static int ntest = 0;
	if (cnt < k) printf("Case #%d: %s\n", ++ntest, "IMPOSSIBLE");
	else printf("Case #%d: %d\n", ++ntest, sw);
	// solve here
}

