#include <cstdio>
#include <algorithm>
using namespace std;

int k, tests, t[210][210];

int ile(int n) {
	int ans = 0;
	for (int i = 1; i <= n; i++)
		ans += 2 * i - 1;
	return ans;
}

int main() {
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		scanf("%d", &k);
		memset(t, -1, sizeof(t));
		for (int i = 1; i <= 2 * k - 1; i++) {
			if (i <= k) {
				int j = k - i;
				for (int l = 0; l < i; l++)
					scanf("%d", &t[i - 1][j + 2 * l]);
			} else {
				int j = i - k;
				for (int l = 0; l < 2 * k - i; l++)
					scanf("%d", &t[i - 1][j + 2 * l]);
			}
		}
		int x = (2 * k - 1) / 2, y = (2 * k - 1) / 2;
		int best_odl = 1000000;
		for (int i = 0; i < 2 * k - 1; i++)
			for (int j = 0; j < 2 * k - 1; j++) {
				int akt_odl = abs(i - x) + abs(j - y);
				bool ok = true;
				for (int i2 = 0; i2 < 2 * k - 1; i2++)
					for (int j2 = 0; j2 < 2 * k - 1; j2++) {
						int i3 = i - (i2 - i), j3 = j2;
						if (i3 >= 0 && i3 < 2 * k - 1 && j3 >= 0 && j3 < 2 * k - 1) {
							if (t[i2][j2] != -1 && t[i3][j3] != -1 && t[i2][j2] != t[i3][j3])
								ok = false;
						}
						i3 = i2, j3 = j - (j2 - j);
						if (i3 >= 0 && i3 < 2 * k - 1 && j3 >= 0 && j3 < 2 * k - 1) {
							if (t[i2][j2] != -1 && t[i3][j3] != -1 && t[i2][j2] != t[i3][j3])
								ok = false;
						}
					}
				if (ok) best_odl = min(best_odl, akt_odl);
			}
		printf("Case #%d: %d\n", tc, ile(k + best_odl) - ile(k));
	}
	return 0;
}