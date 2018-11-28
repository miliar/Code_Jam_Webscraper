#include <iostream>
#include <stdio.h>
using namespace std;

#define N 2005
typedef long long ll;

int i, j, k, n, m, x, y, tt, T, it;

int p[N];
ll dp[N];
ll t, t1, t2, res, z, d;
int a[N];

int main() {
	freopen("big.in", "r", stdin); freopen("big.out", "w", stdout);
	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		cin >> k >> m >> n;
		for (i = 0; i < n; i ++) {
			cin >> a[i];
		}
		for (i = 0; i < n; i ++) {
			p[i] = -1;
		}
		x = 0;
		p[x] = 0;
		it = 0;
		res = 0;
		while (it < k) {
			t = 0;
			for (i = 0; i < n; i ++) {
				t = t + a[x];
				if (t > m) {
					t -= a[x];
					break;
				}
				res += a[x];
				x = (x + 1) % n;
			}
			it ++;
			if (it >= k) {
				break;
			}
			if (p[x] != -1) {
				y = it - p[x];
				z = res - dp[x];
				d = (k - it) / y;
				res += d * z;
				it += d * y;
				break;
			} else {
				p[x] = it;
				dp[x] = res;
			}
		}
		while (it < k) {
			t = 0;
			for (i = 0; i < n; i ++) {
				t = t + a[x];
				if (t > m) {
					t -= a[x];
					break;
				}
				res += a[x];
				x = (x + 1) % n;
			}
			it ++;
		}

		cout << "Case #" << tt << ": " << res << endl;
	}
	return 0;
}




