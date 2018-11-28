#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;

LL n, pd, qd, pg, qg;


int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		printf("Case #%d: ", ++cas);
		qd = qg = 100;
		scanf("%lld%lld%lld", &n, &pd, &pg);
		if (pd < 100 && pg == 100 || pd > 0 && pg == 0) {
			puts("Broken");
			continue;
		}
		LL d = __gcd(pd, qd);
		pd /= d; qd /= d;
		d = __gcd(pg, qg);
		pg /= d; qg /= d;
		if (qd > n) {
			puts("Broken");
			continue;
		} else {
			puts("Possible");
		}
	}
	return 0;
}
