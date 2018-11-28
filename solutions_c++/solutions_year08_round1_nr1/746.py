#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int n,t,c,i,k,x[1000],y[1000];
	__int64 sum = 0;
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%d",&y[i]);
		sort(x,x+n);
		sort(y,y+n);
		for(i=sum=0;i<n;i++)
		{
			sum += x[i]*y[n-i-1];
		}
		printf("Case #%d: %I64d\n",c,sum);
	}
	return 0;
}