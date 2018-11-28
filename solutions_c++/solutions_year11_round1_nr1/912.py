#include <stdio.h>

long long n;
int pd, pg;

int gcd(int a, int b) {
	int m;
	while (a % b ){
		m=a%b;
		a=b;
		b=m;
	}
	return b;
}

void solve() {
	int i, m;
	scanf("%lld%d%d", &n, &pd, &pg);

	if (pd > 0 && pg == 0 || pd < 100 && pg ==100) {
		goto broken;	
	} if (pd == 100 || pd == 0) {
		goto possible;
	}

	m=gcd(pd, 100);

	if (n / (100 / m) > 0) {
		goto possible;
	}

broken:
	printf("Broken\n");
	return;
possible:
	printf("Possible\n");
}

int main() {
	int t, i;
	scanf("%d",&t);
	for (i=1;i<=t;i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
