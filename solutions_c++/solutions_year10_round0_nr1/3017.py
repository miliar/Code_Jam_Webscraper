
#include <stdio.h>

void main()
{
	int T, N, K;
	scanf("%d",&T);
	int i, flag;
	for(i=0;i<T;i++)
	{
		scanf("%d %d",&N,&K);
		flag=~0;
		flag<<=N;
		flag=flag|K;
		if(~flag)
		{
			printf("Case #%d: OFF\n",i+1);
		}
		else
		{
			printf("Case #%d: ON\n",i+1);
		}
	}	
}