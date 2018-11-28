#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>

using namespace std;

void solve()
{
	double res=0.0;
	int x,s,r,n;
	double t;

	cin>>x>>s>>r>>t>>n;

	vector<double> v;
	for(int i=0;i<=x;i++)
	{
		v.push_back(s);
	}

	int b,e,w;
	for(int i=0;i<n;i++)
	{
		cin>>b>>e>>w;
		for(int k=b+1;k<=e;k++)
		{
			v[k]+=w;
		}
	}

	sort(v.begin()+1,v.end());

	//cout<<endl<<"V ";
	//for(int i=1;i<=x;i++)
	//	cout<<v[i]<<' ';
	//cout<<endl;

	for(int i=1;i<=x && t>0;i++)
	{
		if(1.0/(v[i]-s+r) <= t)
		{
			v[i]+=(r-s);
			t-=1.0/v[i];
		}
		else
		{
			v[i]=v[i]/(1-t*(r-s));
			t=0;
		}
	}

	for(int i=1;i<=x;i++)
	{
		res+=1.0/v[i];
	}
	cout<<res;
}

int main()
{
	cout.precision(10);
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);

	int t;
	cin>>t;

	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		solve();
		cout<<endl;
	}

	return 0;
}