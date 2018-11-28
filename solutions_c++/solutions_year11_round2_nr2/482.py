#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long lol;

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

const double eps = 1e-12;

int n, D;
int p[222], v[222];

double comp(double a, double b) {
	if (abs(a-b) < eps) return 0;
	if (a - b < -eps) return -1;
	return 1;
}

bool ok(double m) {
	double r = 0.0;
	for (int i = 0; i < n; ++i) {
		double x = p[i] - m;
		if (i > 0) x = max(p[i] - m, r + D);
		r = x + (v[i] - 1) * D;
		if (comp(r - p[i], m) > 0) return false;
	}
	return true;
}

void solve(int testcase)
{
	printf("Case #%d: ", testcase);
	scanf("%d%d", &n, &D);
	for (int i = 0; i < n; ++i) scanf("%d%d", &p[i], &v[i]);
	double l = 0.0, r = 1e19;
	for (int qqq = 100; qqq > 0; --qqq) {
		double m = (l+r) / 2;
		if (!ok(m)) l = m; else r = m;
	}
	printf("%.10lf\n", l);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) solve(i);
	return 0;
}
