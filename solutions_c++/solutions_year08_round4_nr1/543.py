#include <iostream>
#include <algorithm>

using namespace std;

int g[10001], c[10001], d[10001][2];
int m, v;
const int inf = 1000000000;

int dp(int in, int v) {
	int &d = ::d[in][v];
	
//	cout << in << ' ' << v << ' ' << m << '\n';
	if (d != -1) return d;
	d = inf;
	if (in > (m - 1) / 2) {
		// lapa
//		cout << "lapa\n";
		if (v == g[in]) d = 0;
	} else if (g[in] == 0) {
		// or
//		cout << "or\n";
		if (v == 1) {
			d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 1));
			d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 0));
			d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 1));
			if (c[in]) {
				// nevajag nemaz
				d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 1) + 1);
			}
		} else {
			d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 0));
			if (c[in]) {
				d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 1) + 1);
				d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 0) + 1);
				d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 0) + 1);
			}
		}
	} else {
		// and
//		cout << "and\n";
		if (v == 1) {
			d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 1));
			if (c[in]) {
				d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 1) + 1);
				d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 0) + 1);
				d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 1) + 1);
			}
		} else {
			d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 1));
			d = min(d, dp(in * 2, 1) + dp(in * 2 + 1, 0));
			d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 0));
			if (c[in]) {
				d = min(d, dp(in * 2, 0) + dp(in * 2 + 1, 0) + 1);
			}
		}
	}
	
//	cout << "d[" << in << "][" << v << "] = " << d << '\n';
	return d;
}

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int i;
		
		cin >> m >> v;
//		fill(d, d + m, -1);
		memset(d, -1, sizeof d);
		for (i = 1; i <= m; i++) {
			cin >> g[i];
			if (i <= (m - 1) / 2) cin >> c[i];
		}
		
		int r = dp(1, v);
		
		cout << "Case #" << it << ": "/* << m << ' ' << v << ' '*/;
		if (r < inf) {
			cout << r << '\n';
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}
	
	return 0;
}
