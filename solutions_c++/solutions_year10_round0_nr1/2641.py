//GNU C++ 4.3.0
#include <stdio.h>
#include <math.h>
int t, n;
long long int k;
int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf(" %d", &t);
	for (int i = 1; i <= t; i++) {
		scanf(" %d %lld", &n, &k);
		printf("Case #%d: ", i);
		if ((k + 1) % (long long int)pow(2.0, n)) puts("OFF");
		else puts("ON");
	}
	return 0;
}