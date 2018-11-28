#include<iostream>
using namespace std;
typedef long long ll;

ll g[1005];
int start[1005];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t,r,n;
	ll k;
	int cas=1;
	cin>>t;
	while(t--)
	{
		cin>>r>>k>>n;
		for(int i=0;i<n;i++)
			cin>>g[i];
		for(int i=0;i<n;i++)
			start[i]=0;

		int s=0;
		int tm=0;
		ll tot=0;
		while(start[s]==0)
		{
			start[s]=1;
			tm++;
			ll tmp=0;
			int ss=s;
			while(tmp+g[ss]<=k)
			{
				tmp+=g[ss];
				ss=(ss+1)%n;
				if(ss==s) break;
			}
			s=ss;
			tot+=tmp;
		}

		int begin=s;
		s=0;
		ll tot2=0;
		int tm2=0;
		while(s!=begin&&r--)
		{
			tm2++;
			ll tmp=0;
			int ss=s;
			while(tmp+g[ss]<=k)
			{
				tmp+=g[ss];
				ss=(ss+1)%n;
				if(ss==s) break;
			}
			s=ss;
			tot2+=tmp;
		}

		if(r==0) {cout<<"Case #"<<cas++<<": "<<tot2<<'\n';continue;}

		tot-=tot2;
		tm-=tm2;

		ll res=tot2;
		res+=tot*(r/tm);
		r%=tm;
		
		s=begin;
		while(r--)
		{
			ll tmp=0;
			int ss=s;
			while(tmp+g[ss]<=k)
			{
				tmp+=g[ss];
				ss=(ss+1)%n;
				if(ss==s) break;
			}
			s=ss;
			res+=tmp;
		}

		cout<<"Case #"<<cas++<<": "<<res<<'\n';

	}

	return 0;
}