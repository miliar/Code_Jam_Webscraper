#include<iostream>
#include<cstdio>
#include<algorithm>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int ii,tt,n,m,t;
int d[2010],p[2010];
long long s[2010],cost[2010];
bool v[2010];

int main()
{
	freopen("cl.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>tt;
	fo(ii,1,tt)
	{
		cin>>t>>m>>n;
		fo(i,1,n)
			cin>>d[i];
		fo(i,1,n)d[i+n]=d[i];
		s[0]=0;
		fo(i,1,n+n)
			s[i]=s[i-1]+d[i];
		fo(i,1,n)
		{
			int ss=0;
			fo(j,i,i+n-1)
				if (ss+d[j]<=m)
				{
					ss+=d[j];
					p[i]=j%n+1;	
					cost[i]=s[j]-s[i-1];
				}
				else
					break;
		}
		fo(i,1,n)v[i]=false;
		int k=0,i;
		long long sum=0,ans=0,ss=0;
		for(i=1;!v[i];i=p[i])
		{
			sum+=cost[i];
			k++;
			v[i]=true;
		}
		int cir=0,st=i;
		for(i=st;p[i]!=st;i=p[i])
		{
			cir++;
			ss+=cost[i];
		}
		cir++;ss+=cost[i];
		k-=cir;
		int l=t;
		i=1;
		if (t>k+cir)
		{
			ans=(ss)*((t-k)/cir)+sum-ss;
			i=st;
			l=(t-k)%cir;
		}
		fo(j,1,l)
		{
			ans+=cost[i];
			i=p[i];
		}
		cout<<"Case #"<<ii<<": "<<ans<<endl;
	}
	return 0;
}
				
		
	
	
