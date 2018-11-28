#include <cstdio>
using namespace std;
int gcd(int a, int b) {
	return (a == 0 ? b : gcd(b % a, a));
}
int main() {
	int cas, cs = 1;
	scanf("%d", &cas);
	while(cas--) {
		long long n;
		int pd, pg;
		scanf("%lld%d%d", &n, &pd, &pg);
		int a = pd, b = 100;
		int g = gcd(a, b);
		if(b / g <= n && (pg == 0 && pd == 0 || pg == 100 && pd == 100 || pg != 0 && pg != 100)) {
			printf("Case #%d: Possible\n", cs);
		}
		else
			printf("Case #%d: Broken\n", cs);
		++cs;
	}
	return 0;
}
