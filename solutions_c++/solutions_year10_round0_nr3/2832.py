#include <stdio.h>

int main()
{
	long long t,k,r,g[1001],tc,i,sum=0,j,tsum,n;
	scanf("%lld",&t);
	for(tc=1;tc<=t;tc++)
	{
		scanf("%lld%lld%lld",&r,&k,&n);
		tsum=0;
		for(i=0;i<n;i++)
		{
		  scanf("%lld",&g[i]);
		  tsum += g[i];
		}
		if(tsum <= k)
		  sum = r*tsum;
		else
		{
		sum = j = 0;
		while(r--)
		{
			tsum=0;
			while(tsum+g[j] <= k)
			{
				tsum += g[j];
				j = (j+1)%n;
			}
			sum += tsum;
		}
		}
		printf("Case #%lld: %lld\n",tc,sum);
	}
}
