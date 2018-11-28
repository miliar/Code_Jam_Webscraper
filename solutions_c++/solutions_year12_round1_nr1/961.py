#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAXN 1000000

double p[MAXN], f[MAXN], t[MAXN], as;

int main() {
	int test; scanf("%d", &test);
	for (int cas = 1; cas <= test; ++cas) {
		int a, b;
		scanf("%d%d", &a, &b);
		for (int i = 1; i <= a; ++i)
			scanf("%lf", p + i);
		t[0] = 1;
		for (int i = 1; i <= a; ++i)
			t[i] = t[i - 1] * p[i],
			f[a - i + 1] = (1 - p[i]) * t[i - 1];
		f[0] = t[a]; as = 0;
		for (int i = 0; i <= a; ++i)
			as += f[i] * (2 + 2 * b - a);
		double ans = 2 + b;
		for (int i = 0; i <= a; ++i) {
			//printf("%.6f\n", f[i]);
			double ta = 0;
			as += f[i] * ((1 + b - a) - (2 + 2 * b - a));
			ta = as + 2 * i;
			//for (int j = 0; j <= a; ++j)
		//		if (j <= i) {
		//			ta += f[j] * (1 + 2 * i + b - a);
					//printf("%d ", 1 + 2 * i + b - a);
		//		} else {
		//			ta += f[j] * (2 + 2 * i + 2 * b - a);
					//printf("%d ", 2 + 2 * i + 2 * b - a);
		//		}
			//puts("");
			ans = min(ans, ta);
		}
		printf("Case #%d: %.6f\n", cas, ans);
	}
	return 0;
}
