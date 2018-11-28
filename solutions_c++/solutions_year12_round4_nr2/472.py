#pragma comment(linker, "/stack:64000000")

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()

typedef long long llong;

void solve() {
	int n, w, h;
	scanf("%d %d %d", &n, &w, &h);
	vector <pair <int, int> > r(n);
	REP(i, n) {
		scanf("%d", &r[i].first);
		r[i].second = i;
	}
	vector <int> resx(n), resy(n);
	for(int iter = 0; iter < 10000; iter++) {
		random_shuffle(all(r));
		int x = 0, y = 0, mx = 0;
		bool OK = true;
		REP(i, n) {
			if (y + r[i].first > h) {
				x = mx;
				y = 0;				
				if (x > w) {
					OK = false;
					break;
				}
			}
			resx[r[i].second] = (x == 0? 0: x + r[i].first);
			resy[r[i].second] = (y == 0? 0: y + r[i].first);
			if (y == 0) {
				y = r[i].first;
			} else {
				y += 2 * r[i].first;
			}
			if (x == 0) {
				mx = max(mx, r[i].first);
			} else {
				mx = max(mx, x + 2 * r[i].first);
			}			
		}
		if (OK) {
			break;
		}
	}
	REP(i, n) {
		printf("%d %d ", resx[i], resy[i]);
	}
}

int main() {
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
	freopen("B-output.out", "w", stdout);
#endif	
	srand(time(NULL));
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		printf("Case #%d: ", test);
		solve();
		printf("\n");
		cerr << test << endl;
	}
	return 0;
}