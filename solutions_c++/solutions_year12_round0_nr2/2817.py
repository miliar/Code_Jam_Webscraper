#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const N = 100;
int n, s, p;
int t[N];
bool readin() {
	if (scanf("%d%d%d", &n, &s, &p) == EOF) {
		return false;
	}
	for (int i = 0; i < n; ++i) {
		scanf("%d", &t[i]);
	}
	return true;
}
int solve() {
	int ret = 0;
	int cnt = 0;
	for (int i = 0; i < n; ++i) {
		int mp;
		mp = (t[i] % 3 != 0 ? t[i] / 3 + 1 : t[i] / 3);
		if (mp >= p) {
			++ret;
			continue;
		}
		mp = (t[i] + 4) / 3;
		if (t[i] >= 2 && mp >= p && cnt < s) {
			++ret;
			++cnt;
		}
	}
	return ret;
}
int main() {
	int tc;
	int cc = 0;
	scanf("%d", &tc);
	while (tc--) {
		readin();
		printf("Case #%d: %d\n", ++cc, solve());
	}
	return 0;
}
