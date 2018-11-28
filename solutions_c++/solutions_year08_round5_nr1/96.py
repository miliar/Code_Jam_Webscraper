#include <iostream>
#include <string>
#include <vector>

using namespace std;

char a[6002][6002];
const int inf = 100000;
const bool debug = false;

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int l, i, j, t, x = 3001, y = 3001, d = 1, dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1}, qmin, qmax, m, r = 0;
		string s;
		
		memset(a, 0, sizeof a);
		
		// uzzīmējam
		cin >> l;
		for (i = 0; i < l; i++) {
			cin >> s >> t;
			while (t--) {
				for (j = 0; j < s.size(); j++) {
					switch (s[j]) {
					case 'F':
						if (d == 0) {
							a[x][y] |= 1;
						} else if (d == 1) {
							a[x][y] |= 2;
						} else if (d == 2) {
							a[x - 1][y] |= 1;
						} else {
							a[x][y - 1] |= 2;
						}
						x += dx[d];
						y += dy[d];
						if (debug) cout << "(" << x - 3001 << "," << y - 3001 << ")\n";
						break;
					case 'L':
						d = (d + 1) & 3;
						break;
					case 'R':
						d = (d - 1 + 4) & 3;
						break;
					}
				}
			}
		}
		
		if (debug) for (y = 3010; y >= 3001; y--) {
			for (x = 3001; x <= 3010; x++) {
				cout << char(a[x][y] | '0');
			}
			cout << '\n';
		}
		
		// saskaitām
		for (y = 0; y < 6002; y++) {
			qmin = inf, qmax = -inf;
			for (x = 0; x < 6002; x++) {
				if (a[x][y] & 2) {
					qmin <?= x, qmax >?= x;
				}
			}
			m = 0;
			if (qmin != inf) for (x = 0; x < 6002; x++) {
				if (a[x][y] & 2) {
					m = !m;
				}
				if (x >= qmin && x < qmax && !m) {
					a[x][y] |= 4;
					r++;
					if (debug) cout << "h: " << x - 3001 << ' ' << y - 3001 << '\n';
				}
			}
		}
		for (x = 0; x < 6002; x++) {
			qmin = inf, qmax = -inf;
			for (y = 0; y < 6002; y++) {
				if (a[x][y] & 1) {
					qmin <?= y, qmax >?= y;
				}
			}
			if (debug) if (qmin != inf) cout << "x = " << x << ": qmin = " << qmin << ", qmax = " << qmax << '\n';
			m = 0;
			if (qmin != inf) for (y = 0; y < 6002; y++) {
				if (a[x][y] & 1) {
					m = !m;
				}
				if (y >= qmin && y < qmax && !m && !(a[x][y] & 4)) {
					a[x][y] |= 4;
					r++;
					if (debug) cout << "v: " << x - 3001 << ' ' << y - 3001 << '\n';
				}
			}
		}
		
		cout << "Case #" << it << ": " << r << '\n';
	}
	
	return 0;
}
