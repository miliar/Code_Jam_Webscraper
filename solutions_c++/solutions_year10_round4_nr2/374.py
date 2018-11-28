#include<iostream>
#include<string.h>
#include<cstdio>
#include<map>
#include<stdio.h>
#include<queue>
using namespace std;
const long long inf=100000000000ll;
struct po
{
	long long js[12];
	long long v;
}data[2050];
long long n;
void sjr(long long a,long long b)
{
	long long i,j;
	if(b==n)
	{
		for(i=0;i<12;i++)
			data[a].js[i]=inf;
		data[a].js[n-data[a].v]=0;
		return;
	}
	sjr(a*2+1,b+1);
	sjr(a*2,b+1);
	for(i=0;i<12;i++)
	{
		if(i>b)
			data[a].js[i]=inf;
		long long c=inf,d=inf,e=inf;
		for(j=i+1;j>=0;j--)
		{
			c=min(c,data[a*2].js[j]);
			d=min(d,data[a*2+1].js[j]);
		}
		e=c+d+data[a].v;
		c=d=inf;
		for(j=i;j>=0;j--)
		{
			c=min(c,data[a*2].js[j]);
			d=min(d,data[a*2+1].js[j]);
		}
		e=min(e,c+d);
		data[a].js[i]=e;
	}
	return ;
}
int main()
{
	freopen("e:\\b2.in","r",stdin);
	freopen("e:\\b2.out","w",stdout);
	long long i,j,k,l,m,o,y,z;
	scanf("%I64d",&z);
	for(y=1;y<=z;y++)
	{
		scanf("%I64d",&n);
		m=1<<n;
		for(j=n;j>=0;j--)
		{
			for(i=0;i<(1<<j);i++)
				scanf("%I64d",&data[i+(1<<j)].v);
		}
		sjr(1,0);
		printf("Case #%I64d: %I64d\n",y,data[i].js[0]);
	}
	///for(;;);
	return 0;
}
