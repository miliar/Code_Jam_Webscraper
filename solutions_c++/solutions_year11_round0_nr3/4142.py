#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
long long c[1000005];
int main()
{
	long long n,m,sum,ans;
	long long a,b,i,j;
	while(scanf("%lld",&n)!=EOF)
	{
		for(i=1;i<=n;i++)
		{
			scanf("%lld",&m);
			a=sum=0;
			for(j=1;j<=m;j++)
			{
				scanf("%lld",&c[j]);
				a=a^c[j];
				sum+=c[j];
			}
			sort(c+1,c+1+m);
			b=ans=0;
			for(j=1;ans<sum;j++)
			{
				b=b^c[j];
				a=a^c[j];
				ans+=c[j];
				sum=sum-c[j];
				if(b==a)
					break;
			}
			if(b==a)
				printf("Case #%lld: %lld\n",i,sum);
			else
				printf("Case #%d: NO\n",i);
		}
	}
	return 0;
}