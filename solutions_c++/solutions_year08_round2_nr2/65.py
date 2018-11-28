#include <iostream>
using namespace std;

#define N 1005
#define K 1005
int i, j, k, n, T, t, a ,b ,c, res, f, bg, l;

int p[N], pp[N], np;
int g[K], u[K];

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	for (i = 2; i< N; i ++) {
		if (pp[i] == 0) {
			for (j = i + i; j < N; j += i) {
				pp[j] = 1;
			}
		}
	}
	for (i = 2; i< N; i ++) {
		if (pp[i] == 0) {
			p[np++] = i;
		}
	}

	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> a >> b >> c;
		res = 0;
		for (i = a; i <= b; i ++) {
			g[i] = i;
		}
		memset(u, 0, sizeof(u));
		for (bg = 0; bg < np; bg ++) {
			if (p[bg] >= c) {
				break;
			}
		}
		
		f = 0;
		while (f == 0) {
			f = 1;
			for (i = a; i <= b; i ++) {
				for (j = i + 1; j <= b; j ++) {
					if (g[j] != g[i]) {
						for (k = bg; k < np; k ++) {
							if (i % p[k] == 0 && j % p[k] == 0) {
								for (l = a; l <= b; l ++) {
									if (g[l] == g[j]) {
										g[l] = g[i];
									}
								}
								f = 0;
								break;
							}
						}
					}
				}
			}
		}
		
		res = 0;
		for (i = a; i <= b; i ++) {
			if (u[g[i]] == 0) {
				res ++;
				u[g[i]] = 1;
			}
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
