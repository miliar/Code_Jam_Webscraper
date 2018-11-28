#include <stdio.h>
#include <stdlib.h>

int main(void) {
	freopen("D:\\C_Prog\\Contest\\GCJ 2010\\A-large.in", "r", stdin);
	freopen("D:\\C_Prog\\Contest\\GCJ 2010\\A-large.out", "w", stdout);
	int t;\
	scanf("%d", &t);
	for (int z=1; z<=t; z++) {
		printf("Case #%d: ", z);
		int n, k, m;
		scanf("%d %d", &n, &k);
		m = k % (1 << n);
		if (m == (1 << n) - 1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
