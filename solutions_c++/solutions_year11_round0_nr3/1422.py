#include<cstdio>
using namespace std;

int main()
{
	int n,t,sum,xsum,r,a;
	scanf("%d",&t);
	for (int tt=1; tt<=t; tt++)
	{
		scanf("%d",&n);
		r = 10000000;
		sum = xsum = 0;
		for (int i=0; i<n; i++)
		{
			scanf("%d",&a);
			sum += a;
			xsum ^= a;
			if (a < r)
				r = a;
		}
		if (xsum != 0)
			printf("Case #%d: NO\n",tt);
		else
			printf("Case #%d: %d\n",tt,sum-r);
	}
}
