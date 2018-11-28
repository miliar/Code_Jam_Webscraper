#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 1 << 10;

int n, W, L;

int r[nmax];
pair<int, int> c[nmax];
int p[nmax];

void readTest() {

	scanf("%d", &n);
	scanf("%d%d", &W, &L);
	for(int i = 0; i < n; ++i) {
		scanf("%d", &r[i]);
	}

}

bool crossX(int x1, int y1, int r1, int x2, int y2, int r2) {
	return	abs(x1 - x2) < r1 + r2;
}

bool crossY(int x1, int y1, int r1, int x2, int y2, int r2) {
	return	abs(y1 - y2) < r1 + r2;
}

bool check(int x, int y, int k) {

	for(int i = 0; i < k; ++i) {

		if (abs(c[p[i]].first - x) >= r[p[i]] + r[p[k]]) {
			continue;
		}
		if (abs(c[p[i]].second - y) >= r[p[i]] + r[p[k]]) {
			continue;
		}
		return false;

	}

	return true;
}

bool succeed() {

	c[p[0]] = make_pair(0, 0);

	for(int i = 1; i < n; ++i) {

		c[p[i]] = make_pair(INF, INF);

		for(int j = 0; j < i; ++j) {
			
			int x, y;

			x = c[p[j]].first + r[p[j]] + r[p[i]];
			y = 0;

			for(int k = 0; k < i; ++k) {

				if (crossX(x, y, r[p[i]], c[p[k]].first, c[p[k]].second, r[p[k]])) {
					y = max(y, c[p[k]].second + r[p[k]]);
				}

			}

			if (y) {
				y += r[p[i]];
			}

			if (x <= W && y <= L) {
				c[p[i]] = min(c[p[i]], make_pair(x, y));
			}

			x = 0;
			y = c[p[j]].second + r[p[j]] + r[p[i]];

			for(int k = 0; k < i; ++k) {

				if (crossY(x, y, r[p[i]], c[p[k]].first, c[p[k]].second, r[p[k]])) {
					x = max(x, c[p[k]].first + r[p[k]]);
				}

			}

			if (x) {
				x += r[p[i]];
			}

			if (x <= W && y <= L) {
				c[p[i]] = min(c[p[i]], make_pair(x, y));
			}


		}

		if (c[p[i]].first == INF) {
			return false;
		}

	}

	return true;

}

void solveTest() {

	for(int i = 0; i < n; ++i) {
		p[i] = i;
	}

	while(true) {
		random_shuffle(p, p + n);

		if (succeed()) {
			break;
		}

	}

	for(int i = 0; i < n; ++i) {
		if (!check(c[p[i]].first, c[p[i]].second, i)) {
			throw -1;
		}
	}

	for(int i = 0; i < n; ++i) {
		printf(" %d %d", c[i].first, c[i].second);
	}
	puts("");

}

int main()
{
	freopen("B.in", "rt", stdin);

	bool submit = true;

	if (submit) {
		freopen("BL.out", "wt", stdout);
	}

	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt) {
		readTest();
		printf("Case #%d:", tt + 1);
		solveTest();
		if (submit) {
			cerr << "Case " << tt + 1 << " done\n";
		}
	}
	return 0;
}