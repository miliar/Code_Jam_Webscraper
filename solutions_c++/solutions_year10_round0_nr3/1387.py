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
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
#endif
}

void solve(int);

int main() {
	openFiles();
	int t; std::cin >> t;
	for (int i = 0; i < t; ++i)
		solve(i + 1);
	return 0;
}

void solve(int nr) {
	struct State { int money; int turn; };
	std::deque<int> d;
	int R, k, n; std::cin >> R >> k >> n;
	for (int i = 0; i < n; ++i) {
		int t; std::cin >> t;
		d.push_back(t);
	}
	std::map<int, State> vis; 
	int currPos = 0, earn = 0, circLen = 0, turns = 0;
	while (R > 0 && vis.find(currPos) == vis.end()) {
		State s = { earn, circLen++ };
		vis[currPos] = s;
		int left = k;
		std::vector<int> taken;
		while (!d.empty() && d.front() <= left) {
			int t = d.front(); d.pop_front();
			left -= t; earn += t;
			taken.push_back(t);
			currPos = (currPos + 1) % n;
		}
		d.insert(d.end(), taken.begin(), taken.end());
		--R; ++turns;
	}
	State s = vis[currPos];
	int len = turns - s.turn;
	int cost = earn - s.money;
	earn += cost * (R / len); R %= len;
	while (R > 0) {
		int left = k;
		std::vector<int> taken;
		while (!d.empty() && d.front() <= left) {
			int t = d.front(); d.pop_front();
			left -= t; earn += t;
			taken.push_back(t);
		}
		d.insert(d.end(), taken.begin(), taken.end());
		--R;
	}
	printf("Case #%d: %d\n", nr, earn);
}
