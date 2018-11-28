#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

#define MAXN 1001

int x,s,r,n;
int C;
struct Walkways
{
	int b,e,w;
};
vector<Walkways> ways;

double ans,t;

bool cmp(Walkways a,Walkways b)
{
	return a.w<b.w;
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("A-small-attempt1.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>C;
	for(int ca=1;ca<=C;++ca)
	{
		cin>>x>>s>>r>>t>>n;
		ways.clear();

		for(int i=0;i<n;++i)
		{
			int b,e,w;
			cin>>b>>e>>w;
			//if(w>=s)
			{
				Walkways ww;
				ww.b=b;
				ww.e=e;
				ww.w=w;
				ways.push_back(ww);
				x-=(e-b);
			}
		}
		Walkways ww;
		ww.b=-1;
		ww.e=x-1;
		ww.w=0;
		ways.push_back(ww);
		sort(ways.begin(),ways.end(),cmp);
		ans=0;
		for(int i=0;i<ways.size();++i)
		{
			int len=ways[i].e-ways[i].b;
			int sp;
			if(t>=0)
			{
				double run=t*(r+ways[i].w);
				if(run<len)
				{
					ans+=t;
					ans+=(double)(len-run)/(s+ways[i].w);
					t=0;
				}
				else
				{
					double tt=(double)len/(r+ways[i].w);
					t-=tt;
					ans+=tt;
				}
			}
			else
			{
				ans+=(double)len/(s+ways[i].w);
			}
		}

		printf("Case #%d: %.7lf\n",ca,ans);
	}
	return 0;
}
