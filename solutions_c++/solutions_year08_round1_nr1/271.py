#include "stdio.h"
#include <algorithm>
using namespace std;
int x[1005],y[1005];
int main()
{
	__int64 k,j;
	int kase,n,i,to;
	scanf("%d",&kase);
	for(to=1;to<=kase;to++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%d",&y[i]);
		sort(x,x+n);
		sort(y,y+n);
		k=0;
		for(i=0;i<n;i++)
		{
			j=x[i];
			j*=y[n-i-1];
			k+=j;
		}
		printf("Case #%d: %I64d\n",to,k);
	}
	return 0;
}