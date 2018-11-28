#include<stdio.h>

int n,K;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,t;
	scanf("%d",&t);
	for(k=0;k<t;k++)
	{
		printf("Case #%d: ",k+1);
		scanf("%d%d",&n,&K);
		K=K%(1<<n);
		if(K==(1<<n)-1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}