#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int a[1000];

const int maxt = 1000000;
int f[maxt + 1];

void solve() {
	long long L;
	int n;
	cin >> L >> n;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	sort(a, a+n);
	memset(f, -1, sizeof(f));
	f[0] = 0;
	for (int i = 0; i < n; ++i) {
		int t = a[i];
		for (int j = t; j <= maxt; ++j)
			if (f[j-t] != -1) {
				int nt = f[j-t] + 1;
				if (f[j] == -1 || nt < f[j]) {
					f[j] = nt;
				}
			}
	}

	int mx = a[n-1];
	long long uu = (L - maxt) / mx + 1;
	long long t = uu * mx;
	long long ans = -1;
	while ( t <= L ) {
		if (f[L - t] != -1) {
			if (ans == -1) ans = uu + f[L-t];
			ans = min(ans, uu + f[L-t]);
		}
		++uu;
		t += mx;
	}
	if (ans == -1) cout << "IMPOSSIBLE" << endl;
	else cout << ans << endl;
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T -- >0) {
		cout << "Case #" << ++tc << ": ";
		solve();
		cerr << tc << endl;
	}
	return 0;
}