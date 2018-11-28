#include <stdio.h>
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int t=(1<<n);
		if(k%t==t-1)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}