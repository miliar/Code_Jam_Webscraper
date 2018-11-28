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
	solve();
	return 0;
}

void solve() {
	int n, m, k; scanf("%d %d %d\n", &n, &m, &k);
	std::vector<std::string> word;
	for (int i = 0; i < m; ++i) {
		char buf[1024]; scanf("%s\n", buf);
		word.push_back(buf);
	}
	for (int i = 0; i < k; ++i) {
		char buf[1024]; scanf("%s\n", buf);
		std::vector<std::set<char> > vs;
		std::string str(buf);
		for (int j = 0; j < str.size(); ++j) {
			vs.push_back(std::set<char>());
			if (str[j] == '(') {
				while (str[++j] != ')') {
					vs.back().insert(str[j]);
				}
			} else {
				vs.back().insert(str[j]);
			}
		}
		int num = 0;
		for (int j = 0; j < word.size(); ++j) {
			bool fail = false;
			assert(word[j].size() == vs.size());
			for (int l = 0; l < word[j].size(); ++l) {
				char c = word[j][l];
				if (vs[l].find(c) == vs[l].end()) {
					fail = true;
				}
			}
			if (!fail) ++num;
		}
		printf("Case #%d: %d\n", i + 1, num);
	}
}
