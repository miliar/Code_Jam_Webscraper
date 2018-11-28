#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

bool can(int a[], double m, int n, int d) {
	double last = -1e15;
	for (int i = 0; i < n; i++) {
		if (last + d > a[i] + m)
			return false;
		last = max(last + d, a[i] - m);
	}
	return true;
}

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		int n, d, sz = 0, a[1000005];
		scanf("%d %d", &n, &d);
		for (int i = 0; i < n; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			for (int j = 0; j < y; j++)
				a[sz++] = x;
		}
		sort(a, a + sz);
		double lo = 0, hi = 1e13;
		while (hi - lo > 1e-9) {
			double mid = (lo + hi) / 2.00;
			if (can(a, mid, sz, d))
				hi = mid;
			else
				lo = mid;
		}
		printf("Case #%d: %.9lf\n", t, lo);
	}
	return 0;
}

