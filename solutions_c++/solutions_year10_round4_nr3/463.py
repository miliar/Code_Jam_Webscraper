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

bool hasElem(const std::vector<std::vector<int> >& v) {
	for (int i = 0; i < v.size(); ++i)
		for (int j = 0; j < v[i].size(); ++j)
			if (v[i][j]) return true;
	return false;
}

std::vector<std::vector<int> > proc(const std::vector<std::vector<int> >& v) {
	std::vector<std::vector<int> > ret(100, std::vector<int>(100));
	for (int i = 0; i < v.size(); ++i)
		for (int j = 0; j < v[i].size(); ++j)
			if (v[i][j] == 1) {
				bool add = false;
				if (i - 1 >= 0) add |= v[i - 1][j];
				if (j - 1 >= 0) add |= v[i][j - 1];
				if (add) ret[i][j] = 1;
			} else {
				bool add = true;
				add &= (i - 1) >=0 && v[i - 1][j];
				add &= (j - 1) >=0 && v[i][j - 1];
				if (add) ret[i][j] = 1;
			}
	return ret;
}

void solve() {
	std::vector<std::vector<int> > m(100, std::vector<int>(100));
	int n; std::cin >> n;
	for (int i = 0; i < n; ++i) {
		int x1, x2, y1, y2; std::cin >> x1 >> y1 >> x2 >> y2;
		for (int x = x1; x <= x2; ++x) for (int y = y1; y <= y2; ++y)
			m[y - 1][x - 1] = 1;
	}
	int ret = 0;
	while (hasElem(m)) {
		m = proc(m);
		++ret;
	}
	static int ntest = 0;
	printf("Case #%d: %d\n", ++ntest, ret);
}
