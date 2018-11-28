#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

#define SIZE(X) (int)X.size()
#define ALL(X) X.begin(), X.end()

inline int nextInt() 
{
	register int ans = 0, sgn = 1;
	register char ch;
	while ((ch = getchar()) < '0') if (ch == '-') sgn = -1;
	do {
		ans *= 10;
		ans += (ch - '0');
	} while ((ch = getchar()) >= '0');
	return sgn * ans;
}

double x[10], y[10], r[10];

inline double dist(int a, int b) {
	return sqrt( (x[a] - x[b]) * (x[a] - x[b]) + (y[a] - y[b]) * (y[a] - y[b]) ); 
}

int n, i;

int main(void) 
{
	int t = nextInt();
	for (int tt = 1; tt <= t; ++tt) {
		n = nextInt();
		for (i = 1; i <= n; ++i) {
			scanf("%lf %lf %lf", x + i, y + i, r + i);
		}

		if (n == 1) {
			printf("Case #%d: %lf\n", tt, r[1]);
			continue;
		}

		if (n == 2) {
			double ret = max(r[1], r[2]);
			printf("Case #%d: %lf\n", tt, ret);
			continue;
		}

		double ret1 = max((dist(1, 2) + r[1] + r[2]) / 2.0, r[3]);
		double ret2 = max((dist(2, 3) + r[2] + r[3]) / 2.0, r[1]);
		double ret3 = max((dist(1, 3) + r[1] + r[3]) / 2.0, r[2]);

		double ret = min(ret1, ret2);
		ret = min(ret, ret3);

		printf("Case #%d: %lf\n", tt, ret);
	}
	return 0;
}