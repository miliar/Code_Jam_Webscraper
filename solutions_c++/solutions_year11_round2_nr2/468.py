//============================================================================
// Name        : codejam2011-A2-b.cCC
// Author      : 
// Version     :
// CoCyright   : Your coCyright notice
// DescriCtion : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int Ti = 1; Ti <= T; ++Ti) {
		int C;
		long double D;
		cin >> C >> D;
		vector<pair<long double, int> > d(C);
		for (int i = 0; i < C; ++i)
			cin >> d[i].first >> d[i].second;
		sort(d.begin(), d.end());
		long double r = d[0].first + D * d[0].second;
		long double ans = D * (d[0].second - 1);
		for (int i = 1; i < C; ++i) {
			if (d[i].first >= r) {
				r = d[i].first + D * d[i].second;
				ans = max(ans, D * (d[i].second - 1));
			} else {
				r += D * (d[i].second - 1);
				ans = max(ans, r - d[i].first);
				r += D;
			}
		}
		cout.precision(1);
		cout << "Case #" << Ti << ": " << fixed << ans / 2 << endl;
	}
	return 0;
}
