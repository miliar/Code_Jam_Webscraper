#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=1000+10;
int n,mark[maxn];
long long r,m,ans,a[maxn],d[maxn],tot,sum,p[maxn];
void init()
{
	cin >>r>>m>>n;
	for (int i=0;i<n;i++)
		cin >>a[i];
}
int getnext(int k)
{
	if (sum<=m)
	{
		d[tot++]=sum;
		return k;
	}
	int x=m;
	while (x>=a[k])
	{
		x-=a[k++];
		if (k==n)
			k=0;
	}
	d[tot++]=m-x;
	return k;
}
void solve()
{
	sum=0;
	for (int i=0;i<n;i++)
		sum+=a[i];
	tot=0;
	int i=0;
	memset(mark,-1,sizeof(mark));
	ans=mark[0]=0;
	while (r)
	{
		i=getnext(i);
		r--;
		ans+=d[tot-1];
		if (mark[i]>=0)
		{
			int t=0;
			for (int k=mark[i];k<tot;k++)
				p[t++]=d[k];
			for (int k=1;k<t;k++)
				p[k]+=p[k-1];
			ans+=p[t-1]*(r/t);
			if (r%t)
				ans+=p[r%t-1];
			return;
		}
		mark[i]=tot;
	}
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;
	cin >>t;
	for (int i=1;i<=t;i++)
	{
		init();
		solve();
		cout <<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
