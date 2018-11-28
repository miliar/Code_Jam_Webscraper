#include <stdio.h>
int main()
{
	int T,N,C;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int flag=0,sum=0,min=999999;
		scanf("%d",&N);
		for(int j=0;j<N;j++)
		{
			scanf("%d",&C);
			flag^=C;
			sum+=C;
			if(min>C)
				min=C;
		}
		if(flag)
			printf("Case #%d: NO\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,sum-min);
	}
	return 0;
}
