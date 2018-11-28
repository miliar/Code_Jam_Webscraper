#include <stdio.h>
#include <string.h>
int main()
{
	int n,k,t,i,cas;
	unsigned int pow2[32];
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	pow2[0]=1;
	for (i=1; i<32; i++) pow2[i]=pow2[i-1]*2;
	scanf("%d",&t);
	for (cas=1; cas<=t; cas++)
	{
		scanf("%d%d",&n,&k);
		i=k%pow2[n];	
		if (i==pow2[n]-1) printf("Case #%d: ON\n",cas);
		else printf("Case #%d: OFF\n",cas);
	}
	return 0;
}

