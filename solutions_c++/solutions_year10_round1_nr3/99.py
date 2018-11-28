
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

long long a[3000100];
long long b[3000100];
long long sjr(long long aa,long long bb)
{
	long long ret=0;
	if(bb>=aa)
	{
		ret+=aa-1-b[aa];
		if(bb>=a[aa])
			ret+=a[aa]-aa+1;
		else
			ret+=bb-aa+1;
		return ret;
	}
	if(bb<=b[aa])
		return 0;
	return bb-b[aa];
}
int main()
{
	freopen("c1.txt","r",stdin);
	freopen("oc1.txt","w",stdout);
	long long i,j,a1,a2,b1,b2;
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
	a[1]=1;
	a[2]=3;
	b[2]=b[3]=1;
	a[3]=4;
	b[4]=2;
	j=5;
	for(i=4;i<=1000010;i++)
	{
		a[i]=b[i]+i;
		for(;j<=a[i];j++)
			b[j]=i-1;
	}
	long long y,z;
	scanf("%I64d",&z);
	for(y=1;y<=z;y++)
	{
		scanf("%I64d%I64d%I64d%I64d",&a1,&a2,&b1,&b2);
		long long ans=0;
		for(i=a1;i<=a2;i++)
		{
			if(b1!=1)
				ans+=sjr(i,b2)-sjr(i,b1-1);
			else
				ans+=sjr(i,b2);
		}
		printf("Case #%I64d: %I64d\n",y,(a2-a1+1)*(b2-b1+1)-ans);
	}
	return 0;
}
