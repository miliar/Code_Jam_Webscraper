#include <iostream>
#include <set>
#include <map>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

#define N 15
#define inf 1000000

int i, j, t, T, r, mn, n, fr, k, x, sm, y;
int a[N], b[N], c[N];
int u[10005];

int uc[305];

char s[15];

map<string, int> m;


int miin(int x, int y) {
	return x < y ? x : y;
}


int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B1.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n;
		mn = inf;
		m.clear();
		fr = 0;
		for (i = 0; i < n; i++) {
			cin >> s;
			if (m.find(s) == m.end()) {
				m[s] = fr;
				fr ++;
			}
			c[i] = m[s];
			cin >> a[i] >> b[i];
		}
		memset(u, 0, sizeof(u));
		for (i = 1; i <(1 <<  n); i ++) {
			memset(u, 0, sizeof(u));
			memset(uc, 0, sizeof(uc));
			x = 0;
			y = 0;
			for (j = 0; j < n; j ++) {
				if (i & (1 << j)) {
					if (uc[c[j]] == 0) {
						y ++;
						uc[c[j]] = 1;
					}
					for (k = a[j]; k <= b[j]; k ++) {
						u[k] = 1;
					}
					x ++;
				}
			}
			sm = 0;
			for (j = 0; j <= 10000; j ++) {
				sm += u[j];
			}
			if (sm == 10000 && y <= 3) {
				mn = miin(mn, x);
			}
		}
		cout << "Case #" << t << ": ";
		if (mn == inf) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << mn << endl;
		}
	}
	return 0;
}






