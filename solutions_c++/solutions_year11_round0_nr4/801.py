#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int vals[2000], vis[2000];

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		int n;
		cin >> n;
		for (int i=0;i<n;++i) {
			int v;
			cin >> v;
			--v;
			vals[i] = v;
			vis[i] = 0;
		}

		double ans = 0.0;
		for (int i=0;i<n;++i) if (!vis[i]) {
			int at = i, len = 0;
			while (!vis[at]) {
				vis[at] = 1;
				at = vals[at];
				++len;
			}
			ans += (len == 1 ? 0 : len);
		}
		printf("Case #%d: %.8lf\n", z, ans);
	}
}
