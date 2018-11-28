#include <stdio.h>

#define MAX 1100

int main()
{
	int pg,pd;
	int t,ccnt;
	long long int n;

	scanf("%d",&t);

	for(ccnt=1;ccnt<=t;++ccnt)
	{
		scanf("%lld %d %d",&n,&pd,&pg);
		printf("Case #%d: ",ccnt);
		if((pg==0 && pd!=0) || (pg==100 && pd!=100) )
		{
			printf("Broken\n");
			continue;
		}
		if(n>=100)
		{
			printf("Possible\n");
			continue;
		}
		int d;

		for(d=1;d<=n;++d)
			if((pd*d)%100==0)
				break;
		if(d<=n)
			printf("Possible\n");
		else
			printf("Broken\n");
	}
	return 0;
}

