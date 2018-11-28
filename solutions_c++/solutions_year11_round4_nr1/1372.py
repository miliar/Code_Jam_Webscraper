#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<map>
#include<cmath>
using namespace std;
#define mp make_pair
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
struct ss{
	int b,e,v;
}
hash[1009];
bool cmp(ss a,ss b)
{
	if(a.v < b.v)return true;
	return false;
}
int main()
{
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++)
	{
		int x,s,r,t1,n;
		int bi,ei,vi;
		double ans=0.0;
		scanf("%d%d%d%d%d",&x,&s,&r,&t1,&n);
		
		memset(hash,0,sizeof(hash));
		for(int i=0;i<n;i++)
		{
			scanf("%d%d%d",&bi,&ei,&vi);
			hash[i].b=bi,hash[i].e=ei,hash[i].v=vi;
		}
		sort(hash,hash+n,cmp);
		
		double i=0.0,t=(double)t1;
		double y=(double)x;
		for(int ii=0;ii<n;ii++)
		{
			y=y-(hash[ii].e-hash[ii].b);
		}
		//cout<<y<<"\n";
		double tt=(double)y/(r);
		int flag=((int)floor(tt-t) >=0);
		//cout<<flag<<"\n";
		if(flag)
		{
			ans+=t;
			y=y-(t*r);
			t=0.0;
		}
		else
		{
			t-=tt;
			ans+=tt;
			y=0.0;
		}
		//printf("Case #%d: %.10lf\n",tc,ans);
		//cout<<t<<"\n";
		ans=ans+y/(double)s;
		//cout<<ans<<"\n";
		double dist=0.0;

		for(int ii=0;ii<n;ii++)
		{
				double tt=(double)(hash[ii].e-hash[ii].b)/(r+hash[ii].v);
					int flag=((int)floor(tt-t) >=0);
				if(flag)
				{
					ans+=t;
					dist=(hash[ii].e-hash[ii].b);
					dist=dist-(t*(r+hash[ii].v));
					ans+=dist/(hash[ii].v+s);
					t=0.0;
					//cout<<ans<<" "<<dist<<"\n";
				}
				else
				{
					t-=tt;
					ans+=tt;
				}
				
			
		}
		//if(tc==29)cout<<x<<" "<<s<<" "<<r<<" "<<t<<" "<<n<<"\n";
		printf("Case #%d: %.10lf\n",tc,ans);
	}
	return 0;
}
