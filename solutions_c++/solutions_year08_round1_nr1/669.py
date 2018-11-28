#include <stdio.h>
#include <algorithm>
using namespace std;

int x[800],y[800];

int main()
{
	int t,n;
	int i,j,k;
	__int64 r;

	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",x+i);
		}
		for(i=0;i<n;i++)
		{
			scanf("%d",y+i);
		}

		sort(x,x+n);
		sort(y,y+n);

		r=0;
		for(i=0;i<n;i++)
		{
			r+=(__int64)x[i]*y[n-i-1];
		}
	
		printf("Case #%d: %I64d\n",k,r);
	}

	return 0;
}