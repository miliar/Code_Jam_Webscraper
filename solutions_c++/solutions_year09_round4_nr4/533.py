#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <memory>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define s(c) ((int)((c).size()))
#define all(c) (c).begin(),(c).end()
#define mset(a, v) memset(a, v, sizeof(a))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)
#define rf(i, hi, lo) for (int i = (hi), Min = (lo); i >= Min; --i)
#define c(i, c) f(i, 0, s(c) - 1)
#define rc(i, c) rf(i, s(c) - 1, 0)
#define it(type, it, c) for (type::iterator it = (c).begin(); it != (c).end(); ++it)
#define rit(type, it, c) for (type::reverse_iterator it = (c).rbegin(); it != (c).rend(); ++it)
typedef vector<int> vint;
typedef long long lint;

int n;
int x[42], y[42], r[42];

#define sqr(a) ((double)(a)*(double)(a))

void solve(int t) {
	printf("Case #%d: ", t);
	scanf("%d", &n);
	f(i, 1, n) {
		scanf("%d%d%d", x + i, y + i, r + i);
	}
	if (n == 1) {
		printf("%.6lf\n", (double)r[1]);
		return;
	}
	if (n == 2) {
		printf("%.6lf\n", (double)max(r[1], r[2]));
		return;
	}
	double d1 = sqrt(sqr(x[1] - x[2]) + sqr(y[1] - y[2]));
	double d2 = sqrt(sqr(x[1] - x[3]) + sqr(y[1] - y[3]));
	double d3 = sqrt(sqr(x[3] - x[2]) + sqr(y[3] - y[2]));
	d1 += r[1] + r[2];
	d2 += r[1] + r[3];
	d3 += r[3] + r[2];
	d1 /= 2;
	d2 /= 2;
	d3 /= 2;
	double a1 = max(d1, (double)r[3]);
	double a2 = max(d2, (double)r[2]);
	double a3 = max(d3, (double)r[1]);
	printf("%.6lf\n", min(a1, min(a2, a3)));
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	f(i, 1, t)
	solve(i);
	return 0;
}
