#include <stdio.h>

void main()
{
	int t,k,n,i,j;

	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&t);

	for(i = 1; i<=t;i++)
	{
		scanf("%d %d",&n,&k);
		for(j=0;j<n;j++)
		{
			if(k&(1<<j))
			{
				continue;
			}
			goto off;
		}
		printf("Case #%d: ON\n",i);
		continue;
off:	printf("Case #%d: OFF\n",i);
	}
}