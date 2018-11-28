#include <stdio.h>

long long GCD(long long a, long long b) {
	long long r;
	while (b > 0) { r = a % b; a = b; b = r; }
	return a;
}

int main()
{
	int kase, serial=1;
	long long n, pd, pg, gcd;

	bool conflict;

	scanf("%d", &kase);
	while (kase--) {
		// begin test case
		scanf("%lld %lld %lld", &n, &pd, &pg);

		conflict = false;
		if (pd == 0) {
			if (pg == 100) conflict = true;
		}
		else if (pd == 100) {
			if (pg == 0) conflict = true;
		}
		// then 0 < pd < 100
		else if (pg == 0 || pg == 100) {
			conflict = true;
		}
		else {
			gcd = GCD(pd, 100);
			if (n < 100 / gcd) conflict = true;
		}

		printf("Case #%d: ", serial++);
		if (conflict) puts("Broken");
		else puts("Possible");
		// end test case
	}
	return 0;
}
