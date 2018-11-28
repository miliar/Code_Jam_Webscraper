#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int g[1024];
int f[1024];
long long c[1024];

int main() {
	freopen("park.in", "r", stdin);
	freopen("park.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T -- > 0) {
		int r, k, n;
		long long ans = 0;
		memset(f, 255, sizeof(f));
		memset(c, 0, sizeof(c));
		scanf("%d%d%d",&r,&k,&n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", g+i);
		}
		int pos = 0;
		int t = 0;
		while (1) {
			if (t >= r) break;
			if (f[pos] == -1) {
				int oldpos = pos;
				long long oldans = ans;
				int oldt = t ++;
				int remain = k;
				while (g[pos] <= remain) {
					remain -= g[pos];
					ans += g[pos];
					if (++pos == n) pos = 0;
					if (pos == oldpos) break;
				}
				f[oldpos] = oldt;
				c[oldpos] = oldans;
			} else {
				int cnt = (r - t) / (t - f[pos]);
				ans += (ans - c[pos]) * cnt;
				t   += (t - f[pos]) * cnt;
				memset(f, 255, sizeof(f));
				memset(c, 0, sizeof(c));
			}
		}

		cout << "Case #" << ++tc <<": " << ans << endl;
	}
	return 0;
}

