#include <cstdio>
#include <algorithm>
using namespace std;

int C, D;
int p[205], v[205];

bool f(double mi) {
	double pt = 0;
	for (int i = 0; i < C; ++i) {
		for (int j = 0; j < v[i]; ++j) {
			if (!i && !j) pt = p[i] - mi;
			else {
				if ((p[i] + mi) - pt < D) return 0;
				pt = max(p[i] - mi, pt + D);
			}
			//printf("%.1f ", pt);
		}
	}
	return 1;
}

double bsearch() {
	int lo = 0, hi = 1<<30, mi;
	while (lo + 1 < hi) {
		mi = (hi - lo) / 2 + lo;
		//printf("%d\n", mi);
		if (f(mi)) hi = mi; else lo = mi;
		//puts("");
	}
	//printf ("%d %d", lo, hi);
	if (f(lo)) printf("%d\n", lo);
	else if (f(lo + 0.5)) printf("%.1f\n", lo + 0.5);
	else if (f(lo + 1)) printf("%d\n", lo + 1 );
}

int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		printf("Case #%d: ", ++cas);
		scanf("%d%d", &C, &D);
		for (int i = 0; i < C; ++i) {
			scanf("%d%d", &p[i], &v[i]);
		}
		bsearch();
	}
	return 0;
}
