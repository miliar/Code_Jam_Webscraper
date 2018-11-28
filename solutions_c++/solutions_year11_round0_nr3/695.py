#include <cstdio>
#include <cstring>

using namespace std;

#define max(x, y) ((x) > (y) ? (x) : (y))

int a[10000];
int d[2][1 << 20];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n;
		scanf("%d", &n);
		int s = 0;
		int S = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			s ^= a[i];
			S += a[i];
		}
		int result = -1;
		if (s == 0) {
			for (int i = 0; i < 1 << 20; ++i) {
				d[0][i] = -1;
				d[1][i] = -1;
			}
			d[0][0] = 0;
			for (int i = 0; i < n; ++i) {
				int i1 = i & 1;
				int i2 = (i + 1) & 1;
				memcpy(d[i2], d[i1], sizeof(d[i1]));
				for (int j = (1 << 20) - 1; j >= 0; --j) {
					if (d[i1][j] >= 0) {
						d[i2][j ^ a[i]] = max(d[i2][j ^ a[i]], d[i1][j] + a[i]);
						if (d[i2][j ^ a[i]] > result && d[i2][j ^ a[i]] < S && d[i2][j ^ a[i]] > 0) result = d[i2][j ^ a[i]];
					}
				}
			}
		}
		if (result == -1) printf("Case #%d: NO\n", tt + 1);
		else printf("Case #%d: %d\n", tt + 1, result);
	}
	return 0;
}
