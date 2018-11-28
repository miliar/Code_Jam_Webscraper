#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

__int64 a[1000],b[1000],sum;

int main()
{
	int t,n,i,k=1;

	for (scanf("%d",&t);t>0;t--)
	{
		sum=0;
		cin>>n;
		for (i=0;i<n;i++)
		{
			scanf("%I64d",&a[i]);
		}
		for (i=0;i<n;i++)
		{
			scanf("%I64d",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		for (i=0;i<n;i++)
		{
			sum+=(a[i]*b[n-i-1]);
		}
		printf("Case #%d: %I64d\n",k,sum);
		k++;
	}
	return 0;
}
