#include <stdio.h>
#include <string.h>
#include <Stdlib.h>

void main(void)
{
	FILE *f;
	f=fopen("A-large.in","r");

	int T;
	fscanf(f,"%d\n",&T);

	for(int t=0;t<T;t++)
	{

		int N,pd,pg;
		char numbuf[1024];
		fscanf(f,"%s %d %d\n",&numbuf,&pd,&pg);

        if (strlen(numbuf)>4) N = 200;
		else
		{
			N = atoi(numbuf);
		};

		bool passed=false;

		if (N>=100)
		{
			passed = true;
		}
		else
		{
			for(int i=1;i<=N;i++)
			{
				if (   (i*pd) % 100 == 0)
				{
					passed=1;
//					printf("%d,",i);
				};
			};
		};

		if (passed)
		{
            if (pg==100 && pd<100) passed = false;
			if (pg==0 && pd!=0) passed = false;
		};

		printf("Case #%d: %s\n",t+1,passed?"Possible":"Broken");

	};
};