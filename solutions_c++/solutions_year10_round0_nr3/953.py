#include <iostream>
using namespace std;

const int maxn=1000+10;
long long a[maxn],d[maxn],n,r,k,p,q,tot;
long long ans,v[maxn];

void init()
{
	scanf("%I64d%I64d%I64d",&r,&k,&n);
	for (int i=0;i<n;++i)
		scanf("%I64d",&a[i]);
	memset(v,0,sizeof(v));
	memset(d,0,sizeof(d));
	ans=0;
}

void work()
{
	int h=0;
	for (int i=1;i<=n+1;++i)
	{
		int x=a[h],t=(h+1)%n;
		while (x+a[t]<=k && h!=t)
		{	x+=a[t];t=(t+1)%n;}
		v[i]=v[i-1]+x;d[h]=i;
		h=t;
		if (d[h]>0)
		{
			ans+=v[d[h]-1];
			p=i-d[h]+1;
			q=v[i]-v[d[h]-1];
			break;
		}
	}
	int w=r-d[h]+1;
	ans+=(w/p)*q;
	for (int i=1;i<=w%p;++i)
	{
		int x=a[h],t=(h+1)%n;
		while (x+a[t]<=k && h!=t)
		{	x+=a[t];t=(t+1)%n;}
		h=t;ans+=x;
	}
}

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%I64d",&tot);
	for (int tc=1;tc<=tot;++tc)
	{
		init();
		work();
		printf("Case #%d: %I64d\n",tc,ans);
	}
    return 0;
}
