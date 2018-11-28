#include<stdio.h>

int cas, t, n, k, mask;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
	for (cas = 1; cas <= t; cas++){
		scanf("%d%d",&n,&k);
		mask = (1 << n) - 1;
		if ( ( k & mask ) == mask ) 
			printf("Case #%d: ON\n", cas);
		else printf("Case #%d: OFF\n", cas);
	}
	return 0;
}