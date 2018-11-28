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
	freopen("D:/Download/test.out", "wt", stdout);
#endif
}

void solve();

int main() {
	openFiles();
	int t; scanf("%d\n", &t);
	while (t--) solve();
	return 0;
}

struct State {
	int g, d, m;
	bool operator<(const State& s) const {
		if (g != s.g) return g < s.g;
		if (d != s.d) return d < s.d;
		if (m != s.m) return m < s.m;
		return false;
	};
};

int p, n;
std::vector<int> maxmiss, cost;
std::map<State, long long> dp;

long long func(int game, int dep, int miss) {
	State ss = { game, dep, miss };
	if (dp.find(ss) == dp.end()) {
		//if (miss < 0) return 100000 * 1100LL;
		if (dep == 0) {
			if (miss > maxmiss[game]) return 100000 * 1100LL;
			return 0;
		}
		int ind = 0; for (int i = 1; i < dep; ++i) ind += n / (1 << (i));
		long long c = cost[ind + game];
		long long r1 = func(game * 2, dep - 1, miss) + func(game * 2 + 1, dep - 1, miss) + c;
		long long r2 = func(game * 2, dep - 1, miss + 1) + func(game * 2 + 1, dep - 1, miss + 1);
		dp[ss] = std::min(r1, r2);
	}
	return dp[ss];
}

void solve() {
	dp.clear();
	std::cin >> p;
	n = 1 << p;
	maxmiss.assign(n, 0);
	cost.assign(n - 1, 0);
	for (int i = 0; i < n; ++i) std::cin >> maxmiss[i];
	for (int i = 0; i < n - 1; ++i) {
		std::cin >> cost[i];
	}
	long long ret = func(0, p, 0);
	static int ntest = 0;
	printf("Case #%d: %lld\n", ++ntest, ret);
}
