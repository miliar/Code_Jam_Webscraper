#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

void solve(int it) {
	int d, c;
	cin >> c >> d;
	vector<pair<int, int> > pts(c);
	for (int i = 0; i < c; i++) {
		cin >> pts[i].first >> pts[i].second;
	}
	double l = 0.0, r = 1e15;
	for (int i = 0; i < 100; i++) {
		double m = (l + r) / 2;
		bool ok = true;
		double last = -1e16;
		for (int j = 0; j < c; j++) {
			for (int k = 0; k < pts[j].second; k++) {
				last += d;
				double x1 = pts[j].first - m;
				double x2 = pts[j].first + m;
				if (x2 < last) {
					ok = false;
					break;
				}
				last = max(last, x1);
			}
			if (!ok) break;
		}
		if (ok) {
			r = m;
		}
		else {
			l = m;
		}
	}
	printf("%.20lf", (l + r) / 2);
}

int main() {
	int nt;
	scanf("%d", &nt);
	for (int it = 1; it <= nt; it++) {
		printf("Case #%d: ", it);
		solve(it);
		printf("\n");
	}
	return 0;
}
