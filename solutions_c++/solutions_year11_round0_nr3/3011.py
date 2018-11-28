#include <iostream>
#include <cstdio>

using namespace std;
int main()
{
	int t,n,x,i,sum,x1,mn;
	scanf("%d",&t);
	for(int tt=1; tt<=t; tt++)
	{
		scanf("%d",&n);
		x1=0,sum=0;
		mn=12345678;
		for(i=0; i<n; i++)
		{
			scanf("%d",&x);
			mn=min(mn,x);
			sum+=x;
			x1=x1^x;
		}
		printf("Case #%d: ",tt);
		if(x1)
			printf("NO\n");
		else
			printf("%d\n",sum-mn);
		
	}
	return 0;
}
