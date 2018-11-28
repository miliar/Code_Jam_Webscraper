#include <stdio.h>

int main()
{
	freopen("small.in", "r", stdin);
	freopen("big.out", "w", stdout);
	int t, cas = 0, n, k;
	scanf("%d", &t);
	while(t --) {
		scanf("%d%d", &n, &k);
		n = 1<<n;
		printf("Case #%d: ", ++ cas);
		if(k % n == n - 1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
