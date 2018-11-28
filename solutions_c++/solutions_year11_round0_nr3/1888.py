#include<cstdio>
#include<algorithm>
using namespace std;
int candy[9999];
int main()
{
	int t,n;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++)scanf("%d",&candy[i]);
		int v=candy[0],sum=v;
		bool f=false;
		for(i=1;i<n-1;i++)
		{
			v=v^candy[i];
			sum+=candy[i];
		}
		v=v^candy[i];
		sum+=candy[i];
		sort(candy,candy+n);
		if(v==0)
		{
			printf("Case #%d: %d\n",test,sum-candy[0]);
		}
		else
		{
			printf("Case #%d: NO\n",test);
		}
	}
	return 0;
}
