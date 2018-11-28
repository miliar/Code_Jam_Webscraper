#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>
#include<cstdio>
#include<queue>
using namespace std;
const long long inf=100000000000ll;
struct po
{
	long long wl[12];
	long long v;
}dd[2050];
long long n;
void wll(long long a,long long b)
{
	long long i,j;
	if(b==n)
	{
		for(i=0;i<12;i++)
			dd[a].wl[i]=inf;
		dd[a].wl[n-dd[a].v]=0;
		return;
	}
	wll(a*2+1,b+1);
	wll(a*2,b+1);
	for(i=0;i<12;i++)
	{
		if(i>b)
			dd[a].wl[i]=inf;
		long long c=inf,d=inf,e=inf;
		for(j=i+1;j>=0;j--)
		{
			c=min(c,dd[a*2].wl[j]);
			d=min(d,dd[a*2+1].wl[j]);
		}
		e=c+d+dd[a].v;
		c=d=inf;
		for(j=i;j>=0;j--)
		{
			c=min(c,dd[a*2].wl[j]);
			d=min(d,dd[a*2+1].wl[j]);
		}
		e=min(e,c+d);
		dd[a].wl[i]=e;
	}
	return ;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("bl.out","w",stdout);
	long long i,j,k,l,m,o,y,z;
	scanf("%I64d",&z);
	for (y=1;y<=100;y++);
	for(y=1;y<=z;y++)
	{
		scanf("%I64d",&n);
		m=1<<n;
		for(j=n;j>=0;j--)
		{
			for(i=0;i<(1<<j);i++)
				scanf("%I64d",&dd[i+(1<<j)].v);
		}
		wll(1,0);
		printf("Case #%I64d: %I64d\n",y,dd[i].wl[0]);
	}
	return 0;
}
