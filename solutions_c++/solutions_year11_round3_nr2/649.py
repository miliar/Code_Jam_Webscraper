#include<cstdio>
#include<algorithm>
using namespace std;
int nt,mt,i,j;
long long l,tt,n,c,f[1005];
long long cal(long long nt,long long tt,long long dis)
{
	if (nt>=tt) return dis*2;
	if (4*dis+nt<=tt) return dis*4;
	long long tmp=tt-nt;
	return 2*dis+(tt-nt)/2;
}
int main()
{
	freopen("B0.in","r",stdin);
	freopen("B0.out","w",stdout);
	scanf("%d",&nt);
	for(mt=1;mt<=nt;mt++)
	{
		scanf("%lld%lld%lld%lld",&l,&tt,&n,&c);
		for(i=0;i<c;i++) scanf("%lld",&f[i]);
		for(i=c;i<n;i++) f[i]=f[i%c];
		long long t=0,ans=100000000000000000LL;
		tt*=2;
		if(l==0)
		{
			for(j=0;j<n;j++) t+=f[j]*4;
			ans=min(ans,t);
		}
		if(l==1)
		{
			for(i=0;i<n;i++)
			{
				t=0;
				for(j=0;j<i;j++) t+=f[j]*4;
				t+=cal(t,tt,f[j]);
				for(j=i+1;j<n;j++) t+=f[j]*4;
				ans=min(t,ans);
			}
		}
		if(l==2)
		{
			
			for(int i1=0;i1<n;i1++)
			for(int i2=i1+1;i2<n;i2++)
			{
				t=0;
				for(j=0;j<i1;j++) t+=f[j]*4;
				t+=cal(t,tt,f[j]);
				for(j=i1+1;j<i2;j++) t+=f[j]*4;
				t+=cal(t,tt,f[j]);
				for(j=i2+1;j<n;j++) t+=f[j]*4;
				ans=min(t,ans);
			}
		}
		printf("Case #%d: %lld\n",mt,ans/2);
	}
}
