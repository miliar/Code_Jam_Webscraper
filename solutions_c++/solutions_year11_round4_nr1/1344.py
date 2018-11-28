#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

double aabs(double a,double b)
{
	return a>b?a-b:b-a;
}

struct node
{
	double dis,w;
	double tm;
	bool operator<(const node& rhs)const
	{
		return w<rhs.w;
	}
}walk[2000];

int T;
double x,s,r,t;
int n;
int b,e;
double remain;
double ans;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin>>x>>s>>r>>t>>n;
		remain=x;
		for(int i=0;i<n;i++)
		{
			cin>>b>>e>>walk[i].w;
			walk[i].dis=e-b;
			walk[i].tm=walk[i].dis/(s+walk[i].w);
			remain-=walk[i].dis;
		}
		walk[n].dis=remain;
		walk[n].w=0;
		walk[n].tm=walk[n].dis/(s+walk[n].w);
		n++;
		sort(walk,walk+n);
		ans=0;
		/*if(remain>r*t)
		{
			ans+=t;
			remain-=r*t;
			ans+=remain/s;
			for(int i=0;i<n;i++)
				ans+=walk[i].tm;
		}
		else
		{
			ans+=(remain/r);
			t-=(remain/r);*/
		for(int i=0;i<n;i++)
		{
			//cout<<t<<endl;
			//cout<<walk[i].tm<<' '<<walk[i].dis<<' '<<walk[i].w<<endl;
			if(t>0)
			{
				if(walk[i].dis > t*(walk[i].w+r))
				{
					ans+=t;
					walk[i].dis-=t*(walk[i].w+r);
					ans+=walk[i].dis/(walk[i].w+s);
					t=0;
				}
				else
				{
					ans+=walk[i].dis/(walk[i].w+r);
					t-=walk[i].dis/(walk[i].w+r);
				}

			}
			else
				ans+=walk[i].tm;
			//cout<<ans<<endl;
		}
		ans+=1e-8;
		/*}*/
		cout<<"Case #"<<cnt<<": ";
		printf("%.7f\n",ans);
	}
	return 0;
}
