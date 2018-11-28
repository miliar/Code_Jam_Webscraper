#include<stdio.h>
#include<string.h>
int main()
{
	int t,n,k;
	scanf("%d",&t);
	for(int q=1;q<=t;q++)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",q);
                if((k+1)%(1<<n)==0)printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
