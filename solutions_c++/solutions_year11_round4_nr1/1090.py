#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<cmath>
using namespace std;
int w[1001],b[1001],e[1001];
struct p
{
	bool u;
	double c,z;
};
bool operator<(const p&a,const p&b)
{
	return a.c/a.z<b.c/b.z;
}
int main()
{
	freopen("A-large(2).in","r",stdin);	
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for (int curt=1;curt<=test;curt++)
	{

		double x;
		cin>>x;
		double s,r;
		double t;
		cin>>s>>r>>t;
		int n;
		cin>>n;
		for (int i=0;i<n;i++)
			cin>>b[i]>>e[i]>>w[i];
		double curp=0;
		vector<pair<double,double > > sp;
		for (int i=0;i<n;i++)
		{
			double begin=b[i];
			double end=e[i];
			if (curp<begin)
			{
				sp.push_back(make_pair(s,begin-curp));
			}
			sp.push_back(make_pair(w[i]+s,end-begin));
			curp=end;
		}
		if (curp<x)
		{		
			sp.push_back(make_pair(s,x-curp));
		}
		
		double res=0.0;
		sort(sp.begin(),sp.end());
		int ind=0;
		while (ind<sp.size()&&t>0.0)
		{
			if (sp[ind].first==s)
			{
				if (sp[ind].second/r<t)
				{
					t-=sp[ind].second/r;
					sp[ind].first=r;
				}
				else
				{
					double dist=r*t;
					sp[ind].first=r;
					sp.push_back(make_pair(s,sp[ind].second-dist));
					sp[ind].second=dist;
					t=0;
				}
			}
			else
			{
				if (sp[ind].second/(sp[ind].first-s+r)<t)
				{
					t-=sp[ind].second/(sp[ind].first-s+r);
					sp[ind].first=(sp[ind].first-s+r);
				}
				else
				{
					double dist=(sp[ind].first-s+r)*t;	
					sp.push_back(make_pair(sp[ind].first,sp[ind].second-dist));
					sp[ind].first=(sp[ind].first-s+r);
					sp[ind].second=dist;
					t=0;
				}
			}
			ind++;
		}
		for (int i=0;i<sp.size();i++)
		{
			res+=sp[i].second/sp[i].first;
		}

		cout<<"Case #"<<curt<<": ";
		printf("%.8lf",res);
		cout<<endl;
	}


	return 0;
}