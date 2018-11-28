#include <cstdio>
long long ton(int n) {
	if (n == 0) return 1;
	if (n % 2) return 2*ton(n/2)*ton(n/2);
	else return ton(n/2)*ton(n/2);
}
int main() {
	int t, n, k; scanf("%d", &t);
	for(int i = 1; i <= t; i++)  {
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", i);
		while ((k > 0) && (n > 1)) {
			if (k % 2) { k /= 2; n--; }
			else break;
		}
		if (k % 2) printf("ON\n");
		else printf("OFF\n");
	}
	
}
