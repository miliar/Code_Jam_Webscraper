//google code jam 2010 qualification round a

#include <stdio.h>

int main()
{
	int t,n,cas,i;
	long k;
	bool ans;

	scanf("%d", &t);
	for (cas=1; cas<=t; cas++)
	{
		scanf("%d%ld", &n, &k);
		ans=true;
		for (i=1; ans && i<=n; i++)
		{
			if (k%2==0) ans=false;
			k/=2;
		}
		printf("Case #%d: ", cas);
		if (ans) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}