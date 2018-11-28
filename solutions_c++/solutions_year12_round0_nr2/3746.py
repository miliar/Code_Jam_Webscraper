#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	long long int t,n,s,p,a[1000],minsum,sum,ans,count1,count2;
	scanf("%lld",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%lld%lld%lld",&n,&s,&p);
		for(int j=0;j<n;j++)
			scanf("%d",&a[j]);
		if(p==1)
			minsum=1;
		else if(p==0)
			minsum=0;
		else
			minsum=p+p-2+p-2;
		if(p==0)
			sum=0;
		else
			sum=p+p-1+p-1;
		count1=count2=ans=0;
		for(int j=0;j<n;j++)
		{
			if(a[j]>=minsum&&a[j]<sum)
				count1++;
			else if(a[j]>=sum)
				count2++;
		}
		if(count1<=s)
			ans+=count1;
		else
			ans+=s;
		ans+=count2;
		printf("Case #%d: %d\n",(i+1),ans);
	}
	return 0;
}