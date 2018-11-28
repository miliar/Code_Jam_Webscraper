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

void solve() {
	int n; scanf("%d\n", &n);
	static int ntest= 0;
	double rr = 1000000000;
		if (n == 1) {
		int x, y, r;
		scanf("%d %d %d", &x, &y, &r);
		double rr = r;
		printf("Case #%d: %.6lf\n", ++ntest, rr);
	}
	if (n == 2) {
		int x, y, r;
		double rr = 0;
		scanf("%d %d %d", &x, &y, &r);
		rr = std::max(rr, (double)r);
		scanf("%d %d %d", &x, &y, &r);
		rr = std::max(rr, (double)r);
		printf("Case #%d: %.6lf\n", ++ntest, rr);
	}
	if (n == 3) {
		double rr = 1000000000;
		int x[3], y[3], r[3];
		scanf("%d %d %d", &x[0], &y[0], &r[0]);
		scanf("%d %d %d", &x[1], &y[1], &r[1]);
		scanf("%d %d %d", &x[2], &y[2], &r[2]);
		double r0 = sqrt((double)(x[0]-x[1])*(x[0]-x[1]) + (y[0]-y[1])*(y[0]-y[1])) + r[0] + r[1];
		r0 /= 2;
		rr = std::min(rr, std::max(r0, (double)r[2]));
		double r1 = sqrt((double)(x[0]-x[2])*(x[0]-x[2]) + (y[0]-y[2])*(y[0]-y[2])) + r[0] + r[2];
		r1 /= 2;
		rr = std::min(rr, std::max(r1, (double)r[1]));
		double r2 = sqrt((double)(x[2]-x[1])*(x[2]-x[1]) + (y[2]-y[1])*(y[2]-y[1])) + r[2] + r[1];
		r2 /= 2;
		rr = std::min(rr, std::max(r2, (double)r[0]));
		printf("Case #%d: %.6lf\n", ++ntest, rr);
	}
}
