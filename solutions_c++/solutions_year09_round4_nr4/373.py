#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <sstream>

#define int64 long long

using namespace std;

string taskname = "dd";

struct circle {
	double x, y, r;
	
	circle(double tx = 0, double ty = 0, double tr = 0) {
		x = tx;
		y = ty;
		r = tr;
	}

	void scan() {
		cin >> x >> y >> r;
	}
};

#define MAXN 10

circle a[MAXN];
int n;

double dist(circle c1, circle c2) {
	return hypot(c1.x - c2.x, c1.y - c2.y);
}

bool cover(circle c1, circle c2, double r) {
	return (dist(c1, c2) + c1.r + c2.r <= 2 * r);	
}

bool ok(double r) {
	if (n == 1) {
		return (a[0].r <= r);
	} else if (n == 2) {
		return (a[0].r <= r && a[1].r <= r);
	} else {
		int p[3];
		for (int i = 0; i < 3; i++) {
			p[i] = i;
		}
		do {
			if (a[p[0]].r <= r && cover(a[p[1]], a[p[2]], r)) {
				return true;
			}
		} while (next_permutation(p, p + 3));
		return false;
	}
}

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	for (int test = 0; test < tests; test++) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			a[i].scan();						
		}

		double l = 0, r = 10000;

		for (int i = 0; i < 200; i++) {
			double m = (l + r) / 2;
			if (ok(m)) {
				r = m;
			} else {
				l = m;
			}
		}

		cout << "Case #" << test + 1 << ": ";
		printf("%.14lf", l);
		cout << endl;
	}

	return 0;
}
