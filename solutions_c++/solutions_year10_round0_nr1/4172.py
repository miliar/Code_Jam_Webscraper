#include <cstdio>

int main()
{
	int nt, n, k;
	
	scanf("%d", &nt);
	
	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d %d", &n, &k);
		
		n = (1 << n);
		
		k = k % n;
			
		if (k + 1 == n) puts("ON"); else puts("OFF");
	}
	
	return 0;
}
