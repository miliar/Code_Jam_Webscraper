#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

long long gcd(long long a,long long b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

long long sum[10005];
long long max_gcd[10005];



long long minx(long long a,long long b)
{
	if(a==-1) return b;
	else return a<b?a:b;
}


int main()
{
	int cas=1;
	freopen("C-small-attempt3.in","r",stdin);
	freopen("outC.txt","w",stdout);
	int T;scanf("%d",&T);
	while(T--)
	{
		int i,j;
		int n;
		/*if(cas==18)
		{
			cout<<endl;
		}*/
		long long l,h;
		scanf("%d%lld%lld",&n,&l,&h);
		for(i=0;i<n;++i)
			scanf("%lld",&sum[i]);
		sort(sum,sum+n);
		max_gcd[n-1]=sum[n-1];
		for(i=n-2;i>=0;--i)
		{
			max_gcd[i]=gcd(max_gcd[i+1],sum[i]);
		}
		printf("Case #%d: ",cas++);
		long long po=-1;
		for(i=l;i<=h;++i)
		{
			for(j=0;j<n;++j)
			{
				if(i%sum[j]==0||sum[j]%i==0) continue;
				break;
			}
			if(j==n)
			{
				po=i;
				break;
			}
		}
		long long lcm=1;
		double lcn=1.0;
		long long ans=-1;
		for(i=0;i<n;++i)
		{
			long long d=gcd(lcm,sum[i]);
			lcn=lcn*sum[i]/d;
			if(lcn-h>1e-9)
				break;
			lcm=lcm/d*sum[i];
			lcn=lcm;
			if(i!=n-1)
			{
				long long b=max_gcd[i+1];
				if(b%lcm==0) 
				{
					long long aa=h/lcm,bb=l/lcm;
					long long kk=b/lcm;
					if((aa>bb||(l%lcm==0&&aa>=bb)))
					{
						if(l%lcm!=0) bb++;
						if(bb<=kk)
							ans=minx(ans,lcm*bb);
					}
				}
			}
		}
		if(i==n)
		{
			long long aa=h/lcm,bb=l/lcm;
			if(aa>bb||(l%lcm==0&&aa>=bb))
			{
				if(l%lcm!=0) bb++;
				ans=minx(ans,lcm*bb);
			}
		}
		long long kl=max_gcd[0];
		long long kk=sqrt((double)kl)+1e-10;
		for(i=1;i<kk+2;++i)
		{
			if(kl%i==0)
			{
				if(i<=h&&i>=l)
					ans=minx(ans,i);
				if(kl/i<=h&&kl/i>=l)
					ans=minx(ans,kl/i);
			}
		}
//		cout<<ans<<' '<<po<<' '<<endl;
		if(po==-1)
			printf("NO\n");
		else
		printf("%lld\n",po);
	}
}