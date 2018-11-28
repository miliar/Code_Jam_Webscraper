//C

#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	//files
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	//vars
	int T,t;
	int n,a,b,i,x;
	int freq[105];
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//input
			scanf("%d%d%d",&n,&a,&b);
				for (i=0; i<n; i++)
					scanf("%d",&freq[i]);
			//brute force
			printf("Case #%d: ",t);
				for (x=a; x<=b; x++)
				{
					for (i=0; i<n; i++)
						if (freq[i]>=x)
						{
							if (freq[i]%x)
								break;
						}
						else
							if (x%freq[i])
								break;
					if (i==n)
					{
						printf("%d\n",x);
						break;
					}
				}
				if (x>b)
					printf("NO\n");
		}
	return(0);
}