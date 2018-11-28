#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define sz(a) ((int)((a).size()))
typedef pair<int, int> ii;
typedef long long LL;

int a[120][30];
int f[120][120];
bool d[1<<20];
int ans[1<<20];

int main() {
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);
	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
fprintf(stderr, "%d\n", test);
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		int Ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				int Less = 0, Greater = 0;
				f[i][j] = f[j][i] = 0;
				for (int k = 0; k < m; k++) {
					if (a[i][k] < a[j][k]) Less++;
					else if (a[i][k] > a[j][k]) Greater++;
					else if (a[i][k] == a[j][k]) { Less = Greater = 1; break; }
				}
				if (Less && Greater) continue;
				f[i][j] = f[j][i] = 1;
			}
		}
		
		for (int i = 0; i < n; i++) d[1 << i] = 1;
		int nn = 1 << n;
		for (int k = 3; k < nn; k++) {
			if (!(k & (k - 1))) continue;
			int mj = -1;
			for (int j = 0; j < n; j++) if (k & (1 << j)) { mj = j; break; }
			d[k] = 0;
			if (!d[k ^ (1 << mj)]) continue;
			bool shit = false;
			for (int j = 0; j < n; j++) if (j != mj && (k & (1 << j))) {
				if (!f[j][mj]) {
					shit = true;
					break;
				}
			}
			if (shit) continue;
			d[k] = 1;
		}
		for (int k = 1; k < nn; k++) {
			if (d[k]) {
				ans[k] = 1;
				continue;
			}
			ans[k] = 120;
			for (int t = (k - 1) & k; t > 0; t = (t - 1) & k) {
				if (d[t]) {
					int rrr = ans[k ^ t] + 1;
					ans[k] = min(ans[k], rrr);
				}
			}
		}
		
		
		printf("Case #%d: %d\n", test, ans[nn-1]);
	}
	return 0;
}
