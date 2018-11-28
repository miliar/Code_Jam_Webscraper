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
	int a, b; std::cin >> a >> b;
	int n = (1 << a);
	int m = b % n;
	if (m == n - 1) printf("Case #%d: ON\n", nr);
	else printf("Case #%d: OFF\n", nr);
}
