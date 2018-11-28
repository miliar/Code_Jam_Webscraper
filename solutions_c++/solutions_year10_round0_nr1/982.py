#include<stdio.h>
int main()
{
	int cas,f[35],i,n,k,ii;
	//freopen("1.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	f[0]=1;
	for(i=1;i<=30;i++)
		f[i]=f[i-1]*2;
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d%d",&n,&k);
		if((k+1)%f[n]==0)
			printf("Case #%d: ON\n",ii);
		else
			printf("Case #%d: OFF\n",ii);
	}
	return 0;
}