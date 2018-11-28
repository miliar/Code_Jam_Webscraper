#include <stdio.h>

main() 
{
	int t,n,k;

	//freopen("a.in", "r", stdin);
	
	scanf("%d", &t);
	
	for (int i = 0; i < t; ++i)
	{
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", i+1);
		
		k = k + 1;
		int c = 0; 
		while ( (k>1) && (k%2==0))
		{
			k = k / 2;
			c++;
		}
		if (c >= n) printf("ON\n");
		else printf("OFF\n");
	}
	
	return 0;
}
