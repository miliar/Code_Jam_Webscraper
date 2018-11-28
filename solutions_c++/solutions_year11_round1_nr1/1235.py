#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("Aout.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		double p1,p2;
		long long n;
		scanf("%lld%lf%lf",&n,&p1,&p2);
		if((p2==100&&p1!=100)||(p2==0&&p1!=0))
		{
			printf("Case #%d: Broken\n",cas);
			continue;
		}
		else 
		{
			if(n>=100)
				printf("Case #%d: Possible\n",cas);
			else
			{
				int i,j,flag=0;
				for(i=1;!flag&&i<=n;i++)
					for(j=0;!flag&&j<=i;j++)
					{
						double tmp=(double)j/(double)i;
						tmp*=100.0;
						if(tmp==p1)
							flag=1;
					}
				if(flag)
					printf("Case #%d: Possible\n",cas);
				else
					printf("Case #%d: Broken\n",cas);
			}
		}
	}
	return 0;
}
