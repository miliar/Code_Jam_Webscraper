#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

int main()
{
	int T;	
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		double x,s,r,t;
		int n;
		cin>>x>>s>>r>>t>>n;
		vector<double> b(n+1),e(n+1);
		vector<pair<double,double> > v(n+1);
		double wd=x;
		for(int i=1;i<=n;i++)
		{
			cin>>b[i]>>e[i]>>v[i].first;
			v[i].second=e[i]-b[i];
			wd-=v[i].second;
		}
		//cout<<wd<<endl;
		v[0]=make_pair(0,wd);
		sort(v.begin(),v.end());
		//reverse(v[i].begin(),v[i].end());
		double tim=0.0,rt=0.0;
		
		for(int i=0;i<v.size();i++)
		{
			if(rt + v[i].second/(v[i].first+r)<=t)
			{
				tim+=v[i].second/(v[i].first+r);
				rt+=v[i].second/(v[i].first+r);
			}
			else
			{
				double tr=t-rt;
				rt=t;
				double distrun=tr*(v[i].first+r);
				double res=v[i].second-distrun;
				tim+=(tr+res/(v[i].first+s));
			}
		}
		//cout<<tim<<endl;
		printf("Case #%d: %lf\n",k,tim);
		
		

	}	
	return 0;
}
