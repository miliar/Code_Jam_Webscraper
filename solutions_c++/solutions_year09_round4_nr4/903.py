#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define MN		64
#define SQ(x)	((x)*(x))

struct Circle {
	int x, y;
	int r;
};

Circle C[MN];
int T, N;

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	//freopen("D.in", "r", stdin);

	scanf("%d", &T);
	for (int t=0; t<T; ++t) {
		scanf("%d", &N);
		for (int i=0; i<N; ++i) {
			scanf("%d%d%d", &C[i].x, &C[i].y, &C[i].r);
		}

		double ans = 0;

		if (N<=2) {
			ans = 0;
			for (int i=0; i<N; ++i) {
				ans = max(ans, (double)C[i].r);
			}
		} else if (N==3) {
			ans = 100000000;
			for (int i=0; i<N; ++i) {
				for (int j=0; j<N; ++j) if (i!=j) {
					double v1 = C[3-i-j].r;
					double v2 = (sqrt((double)SQ(C[i].x-C[j].x)+SQ(C[i].y-C[j].y))+C[i].r+C[j].r) / 2.0;
					ans = min(ans, max(v1, v2));
				}
			}
		}

		printf("Case #%d: %.6lf\n", t+1, ans);
	}

	return 0;
}