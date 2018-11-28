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

int n;
vv<string> a;

double wp_without(int i, int team) {
	double win = 0, fail = 0;
	for (int j = 0; j < n; ++j) {
		if (j != team) {
			if (a[i][j] == '1') {
				++win;
			} else if (a[i][j] == '0') {
				++fail;
			}
		}
	}
	return win / (win + fail);
}

void solve() {
	in >> n;
	a.assign(n, "");
	vv<double> wp(n), owp(n, 0), oowp(n, 0);
	for (int i = 0; i < n; ++i) {
		in >> a[i];
	}
	for (int i = 0; i < n; ++i) {
		wp[i] = wp_without(i, -1);
	}
	for (int i = 0; i < n; ++i) {
		int games = 0;
		for (int j = 0; j < n; ++j) {
			if (a[i][j] != '.') {
				owp[i] += wp_without(j, i);
				++games;
			}
		}
		owp[i] /= games;
	}
	for (int i = 0; i < n; ++i) {
		int games = 0;
		for (int j = 0; j < n; ++j) {
			if (a[i][j] != '.') {
				oowp[i] += owp[j];
				++games;
			}
		}
		oowp[i] /= games;
	}
	for (int i = 0; i < n; ++i) {
		out << fixed << setprecision(7) << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int test_cases;
	in >> test_cases;

	for (int test = 0; test < test_cases; ++test) {
		out << "Case #" << test + 1 << ":" << endl;
		solve();
	}

	return 0;
}