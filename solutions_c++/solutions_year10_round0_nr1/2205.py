#include <stdio.h>
#include <string.h>
#define MAX 32
#define BIT(x) (1 << (x-1))
int main()
{
	unsigned long T,N,K;
	int i;
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	
	for (i=1; i<=T; ++i)
	{
		scanf("%ld%ld",&N,&K);
		if ((K & BIT(N)) == BIT(N))
		{
			if (((K+1) & BIT(N)) == 0)
				printf("Case #%d: ON\n",i);
			else
			{
				printf("Case #%d: OFF\n",i);
				continue;
			}
		}
		else printf("Case #%d: OFF\n",i);
	}

	return 0;
}