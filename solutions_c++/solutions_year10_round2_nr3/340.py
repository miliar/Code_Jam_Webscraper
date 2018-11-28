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
	freopen("D:/Download/C-small-attempt0.in", "rt", stdin);
	freopen("D:/Download/C-small-attempt0.out", "wt", stdout);
#endif
}

void solve();

int main() {
	openFiles();
	int t; std::cin >> t;
	while (t--) solve();
	return 0;
}

int dp[1000][1000];

int func(int x, int y) {
	if (dp[x][y] == -1) {
		//dp[x][y] = func();
	}
	return dp[x][y];
}

bool test(const std::vector<int>& v, int n) {
	if (n == 1) return true;
	for (int i = 0; i < v.size(); ++i)
		if (v[i] == n)
			return test(v, i + 1);
	return false;
}

int rret[100];

void solve() {
	static int ntest = 0;
	int n; std::cin >> n;
	if (rret[n] != 0) {
		printf("Case #%d: %d\n", ++ntest, rret[n]);
		return;
	}
	std::vector<int> v; for (int i = 2; i < n; ++i) v.push_back(i);
	int ret = 0, to = 1 << (n - 2);
	for (int i = 1; i < to; ++i) {
 		std::vector<int> t;
		int tt = i, ind = 0;
		while (tt) {
			if ((tt & 1) > 0) t.push_back(v[ind]);
			tt = tt >> 1;
			++ind;
		}
		if (test(t, t.size() + 1)) ++ret;
	}
	rret[n] = (ret + 1) % 100003;
	printf("Case #%d: %d\n", ++ntest, (ret + 1) % 100003);
}

