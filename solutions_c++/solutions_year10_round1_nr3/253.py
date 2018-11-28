#include<iostream>
#include<cmath>
const double Q=(sqrt(5.0)-1)/2;
int main()
{
	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);
	int rep,cas;
	scanf("%d",&rep);
	for(cas=1;cas<=rep;cas++)
	{
		int i,j,a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		long long ans=0;
		for(i=a1;i<=a2;i++)
		{
			double low=i*Q,high=i/Q;
			if (b2 < low)
				ans += (b2-b1+1);
			else if (b1 > high)
				ans += (b2-b1+1);
			else if (b1 > low && b2 < high)
				;
			else if (b1 < low && b2 < high)
				ans += int(low) - b1 + 1;
			else if (b1 > low && b2 > high)
				ans += b2 - int(high);
			else
				ans += b2 - int(high) + int(low) - b1 + 1;
		}printf("Case #%d: %lld\n",cas,ans);
	}
}