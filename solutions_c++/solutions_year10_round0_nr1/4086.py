#include <stdio.h>


int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);
	int i, t;
	scanf("%d", &t);
	
	for(i = 1; i <= t; ++i)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		
		int nrmin = 1 << n;
		if((k + 1) % nrmin == 0) printf("Case #%d: ON\n", i);
		else printf("Case #%d: OFF\n", i);
	}
	
	return 0;
}