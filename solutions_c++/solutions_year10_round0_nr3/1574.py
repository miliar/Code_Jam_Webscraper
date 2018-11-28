#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

long long r,k,zz,n,g[1001],t[1001],sum,ans,p[1001],pp;

int main()
{
	freopen("gcj_rand0_c.in","r",stdin);
	freopen("gcj_rand0_c.out","w",stdout);
	scanf("%lld",&zz);
	for(long long z=1;z<=zz;++z)
	{
		memset(t,0,sizeof(t));
		ans=sum=pp=0;
		scanf("%lld %lld %lld",&r,&k,&n);
		for(long long i=1;i<=n;++i)
		{
			scanf("%lld",g+i);
			sum+=g[i];
		}
		long long u=1;
		for(long long i=1;i<=r;++i)
		{
		//	cout<<i<<' '<<u<<endl;
			if(t[u])
			{
				r-=i-1;
				ans+=(long long)(r/(i-t[u]))*sum*(pp-p[u]);
				r=r-(long long)(r/(i-t[u]))*(i-t[u]);
				for(long long i=1;i<=r;++i)
				{
					long long plus=0,j=u,f=0;
					for(;;++u)
					{
						if(u==n+1)
							u=1;
						if(plus+g[u]>k)
							break;
						if(j==u&&f)
							break;
						f=1;
						plus+=g[u];
					}
					ans+=plus;
					if(u==n+1)
						u=1;
				}
				break;
			}
			p[u]=pp;
			t[u]=i;
			long long plus=0,j=u,f=0;
			for(;;++u)
			{
				//cout<<u<<endl;
				if(u==n+1)
					u=1;
				if(plus+g[u]>k)
					break;
				if(u==j&&f)
					break;
				f=1;
				plus+=g[u];
			}
			//cout<<u<<' '<<j<<endl;
			ans+=plus;
			if(u<=j)
				++pp;
			if(u==n+1)
				u=1;
		}
		printf("Case #%lld: %lld\n",z,ans);
	}
	return 0;
}
