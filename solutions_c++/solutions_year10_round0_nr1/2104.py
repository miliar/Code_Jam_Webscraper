#include <stdio.h>
int t,n,k;
int main()
{
	freopen("pb1.in","r",stdin);
	freopen("pb1.out","w",stdout);
	scanf("%d",&t);
	int i;
	for (i=1; i<=t; i++)
	{
		scanf("%d%d",&n,&k);
		if (k % (1<<n) == (1<<n)-1)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}
