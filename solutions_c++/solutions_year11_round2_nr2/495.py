// MS Visual C++ 2008
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdlib.h>

using namespace std;

const long double EPS = 1e-4;

long long x[1000000];
long double y[1000000];

inline long double llfabs(const long double x)
{
	return (x < 0) ? -x : x;
}

int check(long double m, int k, long double d)
{
	long double lp = x[0] - m;
	for (int i = 1; i < k; i++) {
		if (lp + d > x[i] + m) return 0;
		else if (lp + d < x[i] - m) lp = x[i] - m;
		else lp = lp + d;
	}
	return 1;
}

long double tm_(long double w, int k, long long d)
{
	long double res = 0, t;
	for (int i = 0; i < k; i++) {
		if ((t = llfabs(x[i] - d * i - w)) > res) res = t;
	}
	return res;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int tk = 1; tk <= T; tk++) {
		int c;
		long long d;
		cin >> c >> d;
		int k = 0, p, v;
		for (int i = 0; i < c; i++) {
			cin >> p >> v;
			while (v--) x[k++] = p;
		}

		long double l = 0, r = 1e17;
		while (r - l > EPS) {
			long double m = (l + r) / 2;
//			if (m - l < EPS || r - m < EPS) break;
			if (check(m, k, d)) r = m;
			else l = m;
		}
		printf("Case #%d: %.1llf\n", tk, l);
	}

	return 0;
}