#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 1005

char c[100];
int i, j, k, n, m, x, y, z, T, l, t;
long long res;

int u[300], a[300], fr;
int main() {
	freopen("large.in", "r", stdin);	
	freopen("large.out", "w", stdout);

	cin >> T;
	t = 0;
	while (T--) {
		t ++;
		memset(u, 0, sizeof(u));
		memset(c, 0, sizeof(c));
		memset(a, -1, sizeof(a));
		fr = 0;
		cin >> c;
		fr = 0;
		l = strlen(c);
		for (i = 0; i< l; i ++) {
			if (a[c[i]] == -1) {
				if (fr == 0) {
					a[c[i]] = 1;
					fr ++;
				} else if (fr == 1) {
					a[c[i]] = 0;
					fr ++;
				} else {
					a[c[i]] = fr++;
				}
			}
		}
		if (fr < 2) {
			fr = 2;
		}
		res = 0;
		for (i = 0; i < l; i ++) {
			x = a[c[i]];
			res = res * fr + x;
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}

