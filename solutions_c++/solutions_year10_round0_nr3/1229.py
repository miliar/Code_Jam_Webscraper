#include<iostream>
using namespace std;
long long ans;
long long s[5000],g[5000];
long a[5000],p[5000],next[5000],m,n,k;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	long testcase;
	scanf("%ld",&testcase);
	for (int cc=1;cc<=testcase;cc++)
	{
		scanf("%ld%ld%ld",&m,&k,&n);
		for (int i=0;i<n;i++) scanf("%ld",&a[i]);
		for (int i=n;i<n+n;i++) a[i]=a[i-n];
		g[0]=0; next[0]=0;
		for (int i=0;i<n;i++)
		{
			g[0]+=a[i];
			if (g[0]>k) { next[0]=i; g[0]-=a[i]; break; }
		}
		for (int i=1;i<n;i++)
		{
			g[i]=g[i-1]-a[i-1]; next[i]=next[i-1]; if (next[i]<i) next[i]+=n;
			for (int j=next[i];j<i+n;j++)
			{
				g[i]+=a[j];
				if (g[i]>k) { next[i]=j; g[i]-=a[j]; break; }
			}
			if (next[i]>=n) next[i]-=n;
		}
		for (int i=0;i<n;i++) p[i]=-1;
		long now=0,l=-1,r;
		for (int i=0;i<m;i++)
		{
			p[now]=i;
			s[i]=g[now];
			if (i>0) s[i]+=s[i-1];
			ans=s[i];
			now=next[now];
			if (p[now]>=0) { l=p[now]; r=i; break; }
		}
		if (l>=0)
		{
			long long sr;
			if (l>0) sr=s[r]-s[l-1]; else sr=s[r];
			ans+=(m-r-1)/(r-l+1)*sr;
			long y=(m-r-1)%(r-l+1);
			if (y>0) 
			{
				if (l>0) ans+=s[l+y-1]-s[l-1];
				else ans+=s[l+y-1];
			}
		}
		printf("Case #%ld: %I64d\n",cc,ans);
	}
}