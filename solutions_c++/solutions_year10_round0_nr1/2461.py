#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int t,n,k;
	int num;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		num=1;
		printf("Case #%d: ",i);
		scanf("%d %d",&n,&k);
		while(n-->0)
			num*=2;
		k=k%num;
		if(k==num-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}