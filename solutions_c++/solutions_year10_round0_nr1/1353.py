#include <stdio.h>

int main()
{
	int T,t,n,k;
	freopen("a.in","r",stdin);	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&k);
		if((k+1)%(1<<n)==0)
			printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);
	}
	return 0;
}