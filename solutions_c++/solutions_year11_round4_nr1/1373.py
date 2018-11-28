#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main()
{
	//freopen("1.txt","rt",stdin);
	//freopen("A-small-attempt0.in","rt",stdin);
	//freopen("A-smallOUT.txt","wt",stdout);
	freopen("A-large.in","rt",stdin);
	freopen("A-largeOUT.txt","wt",stdout);
	int T;
	cin>>T;
for(int j=1;j<=T;j++)
{
	int x,s,r,n;
	double t;
	cin>>x>>s>>r>>t>>n;
	vector<pair<pair<int,int>,int>> w(n);
	for(int i=0;i<n;i++)
		cin>>w[i].first.first>>w[i].first.second>>w[i].second;
	sort(w.begin(),w.end());
	vector<int> wi(101,0);
	int en=0;
	for(int i=0;i<n;i++)
	{
		wi[0]+=w[i].first.first-en;
		en=w[i].first.second;
		wi[w[i].second]+=w[i].first.second-w[i].first.first;

	}
	wi[0]+=x-w[n-1].first.second;
	double ti=t,time=0;
	for(int i=0;i<=100;i++)
	{
		if(t>0) 
		{
			if(double(wi[i])/((double)r+i)<=t)
				t-=(double(wi[i]))/((double)r+i);
			else
			{
				
				time+=((double)wi[i]-t*(r+i))/((double)s+i);
				t=0;
			}
		}
		else
			time+=((double)wi[i])/((double)s+i);
	}
	time+=(ti-t);
	printf("Case #%d: %.10lf\n",j,time);
}

fclose(stdout);
}


