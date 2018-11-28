#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define sz(v) (int)(v).size()

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int test = 1; test <= tst; test++) {
		int n, s, p, t = 0;
		cin >> n >> s >> p;
		//vector <int> v(n);
		int res = 0;
		REP(i, n) {
			int x;
			cin >> x;
			if ((x + 2) / 3 >= p) {
				++res;
			} else if (2 <= x && x <= 28 && s > 0 && (x + 1) / 3 + 1 >= p) {
				--s;
				++res;
			}
		}
		printf("Case #%d: %d\n", test, res);
		//vector <pair <int, int> > a(n);
		//REP(i, n) cin >> v[i];
		//REP(i, n) a[i] = make_pair(1000, i);
		//REP(i, n) {
		//	int t = v[i];
		//	int m = t % 3;
		//	if (m == 2 && t >= 2 || m == 0 && t >= 3 || m == 1 && t >= 4) {
		//		if (m == 0) t -= 3;
		//		else if (m == 1) t -= 4;
		//		else t -= 2;
		//		t /= 3;
		//		t += 2;
		//		if (0 <= t && t <= 10) {
		//			a[i].first = t;
		//		}
		//	}
		//}
		//sort(a.rbegin(), a.rend());
		//REP(i, n) cout << a[i].first << " " << a[i].second << endl;
		//int res = 0;
		//REP(i, s) {
		//	assert(a[i].first != -1);
		//	v[a[i].second] = -100;
		//	if (a[i].first >= p) {
		//		++res;
		//	}
		//}
		//REP(i, n) {
		//	int t = v[i] / 3;
		//	if (v[i] % 3 != 0) ++t;
		//	if (t >= p) {
		//		++res;
		//	}
		//}
	}
	return 0;
}