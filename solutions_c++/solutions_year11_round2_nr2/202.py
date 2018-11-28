#include <stdio.h>
#include <algorithm>
using namespace std;
int pos[1000010];
int N;
int main() {
	int T;
	scanf("%d", &T);
	for (int _ = 0; _ < T; _++) {
		printf("Case #%d: ", _+1);
		int D, C;
		scanf("%d %d", &C, &D);
		N = 0;
		for (int i = 0; i < C; i++) {
			int a,b;
			scanf("%d %d", &a, &b);
			for (int j = 0; j < b; j++)
				pos[N++] = a;
		}
		sort(pos, pos+N);
		long double tmin = 0.;
		long double tmax = 1.e12L;
		while (tmax - tmin > 1.e-7L ) {
			long double t = (tmin+tmax)/2L;
			long double p = pos[0] - t;
			bool can = true;
			for (int i = 1; i < N; i++) {
				long double p2 = max(p+D, pos[i]-t);
				if (p2 > pos[i]+t) {
					can = false;
					break;
				}
				p = p2;
			}
			if (!can) tmin = t;
			else tmax = t;
		}
		printf("%.7Lf\n", (tmax+tmin)/2.L);
	}
	return 0;
}
