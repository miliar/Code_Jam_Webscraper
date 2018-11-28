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
	for (int i = 0; i < t; ++i)
		solve();
	return 0;
}

const std::string wtcj = "welcome to code jam";
int dp[510][100];
std::vector<std::vector<int>> trans;

int f(int x, int y) {
	if (y == 0) return 1;
	if (dp[x][y] == -1) {
		int ret = 0;
		char nextChar = wtcj[y-1];
		for (int i = 0; i < trans[nextChar].size(); ++i) {
			if (trans[nextChar][i] >= x) break;
			ret = (ret + f(trans[nextChar][i], y - 1)) % 10000;
		}
		dp[x][y] = ret;
	}
	return dp[x][y];
}

void solve() {
	trans.assign(256, std::vector<int>());
	memset(dp, 0xFF, sizeof(dp));
	char buf[1024]; gets(buf);
	std::string str = buf;
	for (int i = 0; i < str.size(); ++i)
		trans[str[i]].push_back(i);
	int ret = f(str.size(), wtcj.size());
	static int ntest = 0;
	printf("Case #%d: %.4d\n", ++ntest, ret);
}
