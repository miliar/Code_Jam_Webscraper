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

void solve();

inline void openFiles() {
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
}

int main() {
#ifndef ONLINE_JUDGE
	openFiles();
#endif
	solve();
	return 0;
}

void solve() {
	int n; scanf("%d\n", &n);
	for (int i = 0; i < n; ++i) {
		int m; scanf("%d\n", &m);
		std::set<std::string> s;
		for (int j = 0; j < m; ++j) {
			char buf[1000];
			gets(buf);
			std::string str(buf); 
			s.insert(str);
		}
		scanf("%d\n", &m);
		int ret = 0;
		std::set<std::string> used;
		for (int j = 0; j < m; ++j) {
			char buf[1000];
			gets(buf);
			std::string str(buf); 
			if (s.find(str) != s.end()) {
				used.insert(str);
				if (used.size() == s.size()) {
					++ret;
					used.clear();
					used.insert(str);
				}
			}
		}
		printf("Case #%d: %d\n", i + 1, ret);
	}
}
