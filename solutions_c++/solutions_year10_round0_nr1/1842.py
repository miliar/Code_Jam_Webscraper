#include <cstdio>
int main()
{
	int t,i,n,k,val;
	freopen("snapper.in","r",stdin);
	freopen("snapper.out","w",stdout);
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		val=1<<n;
		k%=val;
		if (k==val-1)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}
