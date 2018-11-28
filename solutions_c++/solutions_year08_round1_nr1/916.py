#include <stdio.h>
#include <algorithm>
using namespace std;

int a[1000],b[1000];

int main()
{
	int t,n,i,sum,k=1;

	for (scanf("%d",&t);t>0;t--)
	{
		sum=0;
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		for (i=0;i<n;i++)
		{
			scanf("%d",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		for (i=0;i<n;i++)
		{
			sum+=(a[i]*b[n-i-1]);
		}
		printf("Case #%d: %d\n",k,sum);
		k++;
	}
	return 0;
}
