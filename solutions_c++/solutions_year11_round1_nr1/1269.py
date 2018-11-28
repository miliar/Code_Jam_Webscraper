//A

#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	//files
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	//vars
	int T,t;
	int n,pd,pg;
	int d,g,wd,wg;
	bool good;
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//input
			scanf("%d%d%d",&n,&pd,&pg);
			//special cases
			good=0;
				if (pd==0)
				{
						if (pg!=100)
							good=1;
					goto done;
				}
				if (pg==0)
					goto done;
				if (pd==100)
				{
					good=1;
					goto done;
				}
				if (pg==100)
					goto done;
			//brute force
				for (d=1; d<=n; d++)
				{
					wd=int(double(pd*d)/100+0.5);
						if (((wd*100)%d==0) && ((wd*100)/d==pd))
						{
							good=1;
							goto done;
						}
				}
			//output
done:
			printf("Case #%d: ",t);
				if (good)
					printf("Possible\n");
				else
					printf("Broken\n");
		}
	return(0);
}