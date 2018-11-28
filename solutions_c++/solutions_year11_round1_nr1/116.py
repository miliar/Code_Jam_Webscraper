#include <cstdio>

int gcd(int a, int b) {
	int t;
	while (a) {
		t = b%a;
		b = a;
		a = t;
	}
	return b;
}

int T, pd, pg;
long long n;

int main() {
	scanf("%d", &T);
	for (int r = 0; r < T; ) {
		printf("Case #%d: ", ++r);
		scanf("%lld%d%d", &n, &pd, &pg);
		if (pg == 100)
			if (pd == 100)
				puts("Possible");
			else
				puts("Broken");
		else if (pg == 0)
			if (pd == 0)
				puts("Possible");
			else
				puts("Broken");
		else if (n >= 100/gcd(pd, 100))
			puts("Possible");
		else
			puts("Broken");
	}
	return 0;
}
