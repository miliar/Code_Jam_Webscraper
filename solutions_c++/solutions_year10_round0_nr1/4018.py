#include <stdio.h>

int main() {
	freopen("snapper.in", "r", stdin);
	freopen("snapper.out", "w", stdout);
	long long int t, n, k;
	long long int p[40];
	int flag = 0;
	scanf("%I64d", &t);
	for (int i=0; i<t; i++) {
		flag = 0;
		scanf("%I64d %I64d", &n, &k);
		if ((k+1)%(1<<n)==0) flag = 1;
		if (flag==1)
		printf("Case #%d: ON\n", i+1);
		else printf("Case #%d: OFF\n", i+1);
	}
	return 0;
}
