#include<stdio.h>

int main()
{
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	int n,k,t,cs;
	scanf("%d",&t);
	
	for(cs=0;cs<t;cs++)
	{
		scanf("%d%d",&n,&k);
		if((k & ((1<<n)-1))==((1<<n)-1))
			printf("Case #%d: ON\n",cs+1);
		else
			printf("Case #%d: OFF\n",cs+1);
	}
	return 0;
}