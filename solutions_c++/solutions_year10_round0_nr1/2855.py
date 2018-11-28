#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	long long int n;
	scanf("%lld ", &n);
	for (int i = 0; i < n; i++) {
		long long int b, s;
		scanf("%lld %lld ", &b, &s);
		printf("Case #%d: ", i+1);
		if (!s) {
			printf("OFF");
			if (i == n - 1) break;
				printf("\n");
			continue;
		}
		long long int x = 1 << b;
		if (s%x == x - 1) printf("ON");
		else printf("OFF");
		if (i == n - 1) break;
		printf("\n");
	}
	return 0;
}