#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n;
		scanf("%d", &n);
		int val[n];
		for (int i = 0; i < n; ++i) scanf("%d", &val[i]);
		int best = -1;
		for (int i = 0; i < (1<<n); ++i) {
			int a = 0, b = 0, aa = 0;
			bool aok = false, bok = false;
			for (int j = 0; j < n; ++j) {
				if (i&(1<<j)) {
					a ^= val[j];
					aa += val[j];
					aok = true;
				} else {
					b ^= val[j];
					bok = true;
				}
			}
			if (aok && bok && a == b) {
				best = max(best, aa);
			}
		}
		printf("Case #%d: ", tt);
		if (best == -1) printf("NO\n");
		else printf("%d\n", best);
	}
}
