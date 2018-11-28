/*
 * wl.cpp
 *
 *  Created on: 2011-4-20
 *      Author: Administrator
 */
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t,b,a[1001],i,n,l=1;
	long long sum;
	freopen("C.txt","w",stdout);
	scanf("%lld",&t);
	while(t--)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		b=a[0];
		sum=a[0];
		for(i=1;i<n;i++)
		{
			b=b^a[i];
			sum+=a[i];
		}
		if(b!=0)
		{
			printf("Case #%d: NO\n",l++);
			continue;
		}
		else
		{
			sort(a,a+n);
			printf("Case #%d: %lld\n",l++,sum-a[0]);
		}
	}
	return 0;
}


