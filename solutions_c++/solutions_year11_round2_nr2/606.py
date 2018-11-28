#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <list>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <cassert>
#include <iomanip>

using namespace std;

#define vv vector
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define abs(x) ((x)<0?-(x):(x))
#define sqr(x) ((x)*(x))
#define in cin
#define out cout
#pragma warning(disable: 4996)

typedef long long ll;

int d;
vv<double> x;

bool good(double t) {
	vv<double> y(x.size());
	y[0] = x[0] - t;
	for (int i = 1; i < x.size(); ++i) {
		double border = y[i - 1] + d;
		if (x[i] - border >= 0) {
			y[i] = max(border, x[i] - t);
		} else {
			y[i] = min(border, x[i] + t);
		}
	}
	for (int i = 1; i < y.size(); ++i) {
		if (abs(y[i - 1] - y[i]) < d) {
			return false;
		}
	}
	return true;
}

double solve() {
	int n;
	in >> n >> d;
	x.clear();
	for (int i = 0; i < n; ++i) {
		int pt, ven;
		in >> pt >> ven;
		for (int j = 0; j < ven; ++j) {
			x.push_back(pt);
		}
	}
	if (x.size() < 2) {
		return 0;
	}
	//sort(x.begin(), x.end());
	double l = 0, r = 1e5;
	//while (l < r) {
	for (int steps = 0; steps < 500; ++steps) {
		double m = (l + r) / 2;
		if (good(m)) {
			r = m;
		} else {
			l = m;
		}
	}
	return l;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int test_cases;
	in >> test_cases;

	for (int test = 0; test < test_cases; ++test) {
		out << "Case #" << test + 1 << ": " << fixed << setprecision(7) << solve() << endl;
	}

	return 0;
}