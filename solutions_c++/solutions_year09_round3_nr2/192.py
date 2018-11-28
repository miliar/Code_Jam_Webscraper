#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;
#define EPS 1e-8
#define llong long long

int main(int argc, char* argv[]) {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int cas;
	for (cas = 1; cas <= T; ++cas) {
		int n;
		scanf("%d", &n);
		llong a = 0;
		llong b = 0;
		llong c = 0;
		llong d = 0;
		llong e = 0;
		llong f = 0;
		int i;
		for (i = 0; i < n; ++i) {
			int aa, bb, cc, dd, ee, ff;
			scanf("%d%d%d%d%d%d", &bb, &dd, &ff, &aa, &cc, &ee);
			a += aa;
			b += bb;
			c += cc;
			d += dd;
			e += ee;
			f += ff;
		}
	//	printf("%I64d %I64d %I64d %I64d %I64d %I64d\n", a, b, c, d, e, f);
		llong af = a * a + c * c + e * e;
		llong bf = 2 * (a * b + c * d + e * f);
		llong cf = b * b + d * d + f * f;
		//printf("%I64d %I64d %I64d", af, bf, cf);
		double rt = 0;
		double rd = 0;
		if (af != 0) {
		rt = -1.0 * bf / (2 * af);
		if (rt < 0 + EPS)
			rt = 0;
		if (rt == 0)
			rd = sqrt(cf) / n;
		else
			rd = sqrt((4.0 * af * cf - bf * bf) / (4.0 * af)) / n;
		} else {
			rt = 0;
			rd = sqrt(cf) / n;	
		}
		printf("Case #%d: %.10lf %.10lf\n", cas, rd, rt);
	}
	return EXIT_SUCCESS;
}
