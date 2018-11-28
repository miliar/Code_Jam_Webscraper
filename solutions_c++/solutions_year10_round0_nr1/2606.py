#include<stdio.h>

int main()
{
	int i,k,ncase,t1,n;
	scanf("%d",&ncase);
	for(i=1;i<=ncase;i++)
	{
		scanf("%d%d",&n,&k);
		t1=1<<n;
		printf("Case #%d: ",i);
		if(k%t1==t1-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
