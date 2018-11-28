#include <iostream>
using namespace std;

int tcase, pd, pg;
long long n; 

int gcd(int small, int big) {
	if (small > big) swap(small, big);
	while (small) {
		big %= small;
		swap(small, big);
	}
	return big;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int k = 1; k <= tcase; ++k) {
		scanf("%lld%d%d", &n, &pd, &pg);
		printf("Case #%d: ", k);
		if (pg == 100 || pg == 0) {
			puts(pd == pg ? "Possible" : "Broken");
			continue;
		}
		if (pd == 0) {
			puts("Possible");
			continue;
		}
		if (100 / gcd(pd, 100) <= n) puts("Possible");
		else puts("Broken");
	}
	return 0;
}
