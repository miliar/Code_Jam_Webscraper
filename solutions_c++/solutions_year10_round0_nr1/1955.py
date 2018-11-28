#include <stdio.h>

int main()
{
	freopen("c:\\A-large.in" , "r" , stdin);
	freopen("c:\\a.out" , "w" , stdout);

	
	int t,n,k;
	int c = 1;

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		int ans = 1;

		for(int i = 0 ; i < n ; i++)
			ans*=2;

		//printf("%d %d\n",ans , k);

		printf("Case #%d: ",c);
		if((k + 1) % ans == 0)
		{
			printf("ON\n");
		} else printf("OFF\n");
		c++;
	}
}