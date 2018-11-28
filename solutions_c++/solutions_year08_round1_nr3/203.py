#include <cstdio>
#include <cmath>
#include <string>

int main() {
	int a[31] = {2, 6};
	for (int i = 2; i <= 30; ++i) {
		a[i] = (6*a[i-1]+1000)%1000-(4*a[i-2]+1000)%1000;
		a[i] = (a[i]+1000)%1000;
	}
	int T, idx = 0; scanf("%d", &T);
	while (T--) {
		int x; scanf("%d", &x);
		printf("Case #%d: %03d\n", ++idx, a[x]-1);
	}
	return 0;
}
