#include <stdio.h>



int main()
{
	int T;

	scanf("%d", &T);

	for(int t=1; t<=T; t++)
	{
		int pd, pg, N;

		scanf("%d %d %d", &N, &pd, &pg);

		if(pd && !pg)
		{
			printf("Case #%d: Broken\n", t);
			continue;
		}

		if(pd!=100 && pg==100)
		{
			printf("Case #%d: Broken\n", t);
			continue;
		}

		if(pd==100)
		{
			printf("Case #%d: Possible\n", t);
			continue;
		}

		if(!pd)
		{
			printf("Case #%d: Possible\n", t);
			continue;
		}

		int c2 = 2, c5 = 2;

		if(pd%25==0)c5=0;
		else if(pd%5==0)c5=1;

		if(pd%4==0)c2=0;
		else if(pd%2==0)c2=1;

		int nn = 1;

		for(int i=0; i<c5; i++)nn*=5;
		for(int i=0; i<c2; i++)nn*=2;

		if(nn<=N)printf("Case #%d: Possible\n", t);
		else printf("Case #%d: Broken\n", t);
	}

	return 0;
}