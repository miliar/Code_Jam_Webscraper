#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
typedef pair<int,int> PII;
typedef pair<int,PII> PIPII;
typedef vector<PIPII> VPIPII;
double solve()
{
	int x,s,r,t,n;
	scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
	VPIPII list;
	for(int i=0;i<n;i++)
	{
		int a,b,w;
		scanf("%d%d%d",&a,&b,&w);
		list.push_back(make_pair(w,make_pair(a,b)));
	}
	if(list[0].second.first>0)
	{
		list.push_back(make_pair(0,make_pair(0,list[0].second.first)));
	}
	if(list[n-1].second.second<x)
	{
		list.push_back(make_pair(0,make_pair(list[n-1].second.second,x)));
	}
	for(int i=1;i<n;i++)
	{
		if(list[i].second.first!=list[i-1].second.second)
		{
			list.push_back(make_pair(0,make_pair(list[i-1].second.second,list[i].second.first)));
		}
	}
	sort(list.begin(),list.end());
	double tt=t;
	double ans=0.0;
	n=list.size();
	for(int i=0;i<n;i++)
	{
		double t1=(double)(list[i].second.second-list[i].second.first)/(double)(list[i].first+r);
		//printf("%d: %lf %lf\n",i,t1,tt);
		if(tt>=t1)
		{
			tt-=t1;
			ans+=t1;
		}
		else
		{
			ans+=(double)(list[i].second.second-list[i].second.first+tt*(s-r))/(double)(list[i].first+s);
			tt=0.0;
		}
	}
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		printf("Case #%d: %.10lf\n",cs,solve());
	}
	return 0;
}
