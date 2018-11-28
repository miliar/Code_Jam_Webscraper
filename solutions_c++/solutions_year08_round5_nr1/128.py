#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define S 150
#define N 6010
#define K 8192

int i, j;

int t, T, n, k, m, x, y, l, x2, y2, p, mnx, mxx, mny, mxy;
int res;
char a[50];
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

class sum {
public:
	short a[K+K];
	void clear() {
		int i;
		for (i = 0; i < K + K; i++) {
			a[i] = 0;
		}
	}
	void set(int x, int y) {
		x += K;
		a[x] = 1;
		x >>= 1;
		while (x > 0) {
			a[x] = a[x+x] + a[x+x+1];
			x >>= 1;
		}
	}
	int get(int x, int y) {
		int r = 0;
		x += K;
		y += K;
		while (x < y) {
			if (x % 2 == 1) {
				r += a[x];
				x ++;
			} else if (y % 2 == 0) {
				r += a[y];
				y --;
			} else {
				x >>= 1;
				y >>= 1;
			}
		}
		r += a[x];
		return r;
	}
};

sum h[N], v[N];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large2.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n;
		for (i = 0; i < N; i ++) {
			h[i].clear();
			v[i].clear();
		}
		x = N / 2;
		y = N / 2;
		p = 0;
		mnx = x;
		mny = y;
		mxx = x;
		mxy = y;
		for (i = 0; i < n; i ++) {
			memset(a, 0, sizeof(a));
			cin >> a >> m;
			l = strlen(a);
			for (j = 0; j < m; j ++) {
				for (k = 0; k < l; k ++) {
					if (a[k] == 'R') {
						p = (p + 3) % 4;
					} else if (a[k] == 'L') {
						p = (p + 1) % 4;
					} else {
						if (p == 0) {
							v[x].set(y, 1);
						} else if (p == 1) {
							h[y].set(x, 1);
						} else if (p == 2) {
							v[x-1].set(y,1);
						} else if (p == 3) {
							h[y-1].set(x, 1);
						}
						x += dx[p];
						y += dy[p];
						if (x > mxx) {
							mxx = x;
						} 
						if (x < mnx) {
							mnx = x;
						}
						if (y > mxy) {
							mxy = y;
						} 
						if (y < mny) {
							mny = y;
						}
					}
				}
			}
		}

		res = 0;
		for (i = mnx; i <= mxx; i ++) {
			for (j = mny; j < mxy; j ++) {
				x = h[j].get(0, i);
				y = h[j].get(i + 1, N);
				if (x % 2 == 0 && x > 0 && y > 0) {
					res ++;
					continue;
				}
				x = v[i].get(0, j);
				y = v[i].get(j + 1, N);
				if (x % 2 == 0 && x > 0 && y > 0) {
					res ++;
					continue;
				}
			}
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}




	