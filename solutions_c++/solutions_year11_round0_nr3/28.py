#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int main()	{
	int T=0;
	scanf("%d",&T);
	for(int i=0; i!=T; ++i)	{
		int N=0, sum=0, xsum=0, min=10000000;
		scanf("%d",&N);
		for(int j=0; j!=N; ++j)	{
			int X=0;
			scanf("%d",&X);
			sum += X;
			xsum ^= X;
			if(X<min)	min=X;
		}
		printf("Case #%d: ",i+1);
		if(xsum)	printf("NO\n");
		else		printf("%d\n",sum-min);
	}
	return 0;
}

