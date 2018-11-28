#include <cstdio>
#include <vector>
#include <algorithm>

const int MAX_ITER = 400;

int T;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++) {
		int C, D;
		scanf("%d %d", &C, &D);
		std :: vector<std :: pair<int, int> > cnt(C);
		for (int i = 0; i < C; i ++) {
			scanf("%d %d", &cnt[i].first, &cnt[i].second);
		}
		double l = 0, r = 1e30;
		for (int iter = 0; iter < MAX_ITER; iter ++) {
			double m = (l + r) * .5;
			double pos = cnt[C - 1].first + m;
			bool ok = true;
 			for (int i = C - 1; i >= 0; i --) {
				pos = std :: min(pos, cnt[i].first + m);
				double next = pos - (cnt[i].second - 1.0) * (double)D;
				if (fabs(next - cnt[i].first) > m + 1e-9) {
					ok = false;
					break;
				}
				pos = next - D;
			}
			if (ok) {
				r = m;
			} else {
				l = m;
			}
		}
		printf("Case #%d: %.10lf\n", t, l);
	}
}