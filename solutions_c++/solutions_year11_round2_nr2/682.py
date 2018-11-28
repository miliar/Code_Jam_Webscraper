#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(

const int MAXN = 201;
int cases, n, d;
struct interval {
	int p, v;
}a[MAXN];

bool cmp(const interval& a, const interval& b) {
	return a.p < b.p;
}

bool check(double x) {
	double pos = a[0].p - x + d * (a[0].v - 1);
	if (pos - a[0].p > x) return 0;
	for (int i = 1; i < n; i++) {
		if (a[i].p - x - pos >= d) {
			if (-x + d * (a[i].v - 1) <= x) {
				pos = a[i].p - x + d * (a[i].v - 1);
			} else {
				return 0;
			}
		} else {
			if (pos + d - a[i].p > x) return 0;
			if (pos + d + d * (a[i].v - 1) - a[i].p <= x) {
				pos = pos + d + d * (a[i].v - 1);
			} else {
				return 0;
			}
		}
		
	}
	return 1;
}

int main() {
	freopen("B-small-attempt0 (2).in", "r", stdin);
	freopen("B-small-attempt0 (2).out", "w", stdout);
	scanf("%d", &cases);
	for (int cas = 1; cas <= cases; cas++) {
		scanf("%d%d", &n, &d);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &a[i].p, &a[i].v);
		}
		sort(a, a + n, cmp);
		double l = 0, r = 1e11;
		while (fabs(r - l) > 1e-4) {
			double x = (l + r) / 2;
			if (check(x)) {
				r = x;
			} else {
				l = x;
			}
		}
		printf("Case #%d: %.3lf\n", cas, l);
	}
}
