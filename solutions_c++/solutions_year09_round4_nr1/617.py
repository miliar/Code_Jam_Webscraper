#include <vector>
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
#include <iostream>
#include <iomanip>
#include <iterator>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <sstream>
#include <cassert>

using namespace std;

inline void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
#endif
}

void solve();

int main() {
	openFiles();
	int t; scanf("%d\n", &t);
	while (t--) solve();
	return 0;
}

int ff(std::vector<std::string>& vs, int pos) {
	int n = vs.size();
	for (int i = pos; i < n; ++i) {
		bool good = true;
		for (int j = 0; j < n; ++j) 
			if (j > pos && vs[i][j] == '1') {
				good = false;
				break;
			}
		if (good) return i;
	}
}

void solve() {
	int n; scanf("%d\n", &n);
	std::vector<std::string> vs;
	for (int i = 0; i < n; ++i) {
		char buf[1024]; gets(buf);
		vs.push_back(buf);
	}
	int swap = 0;
	for (int i = 0; i < n; ++i) {
		int ind = ff(vs, i);
		swap += ind - i;
		std::string ss = vs[ind];
		vs.erase(vs.begin() + ind);
		vs.insert(vs.begin() + i, ss);
	}
	static int ntest = 0;
	printf("Case #%d: %d\n", ++ntest, swap);
}
