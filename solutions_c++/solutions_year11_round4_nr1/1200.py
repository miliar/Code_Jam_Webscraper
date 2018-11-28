#define _CRT_SECURE_NO_DEPRECATE


#include<iostream>
#include <iomanip> 
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<set>
#include<list>
#include<limits>
#include<string.h>
#include<memory.h>
using namespace std;

#define SZ(x) ((long long)x.size())

ifstream inf("A-large.in");
//ofstream outf("out.txt");

#define cin inf

#define cout outf

struct node
{
	int b,e;
	int v;
	node(int _b,int _e,int _v)
	{
		b= _b;e=_e;v=_v;
	}
	bool operator<(const node& ot) const
	{
		return v < ot.v;
	}
};
struct ad
{
	int b,e,v;
	bool operator<(const ad& ot) const
	{
		return b < ot.b;
	}
} adx[1002];
void run(int tt)
{
	int x,s,r,t,n;
	cin>>x>>s>>r>>t>>n;
	int nd = 0;
	vector<node> dp;
	for(int i=0;i<n;i++)
		cin>>adx[i].b>>adx[i].e>>adx[i].v;

	sort(adx,adx+n);
	for(int i=0;i<n;i++)
	{
		int b = adx[i].b;
		int e = adx[i].e;
		int v = adx[i].v;
		if(nd < b)
		{
			dp.push_back(node(nd,b,s));
		}
		dp.push_back(node(b,e,v+s));
		nd = e;
	}
	if(nd < x)
		dp.push_back(node(nd,x,s));
	sort(dp.begin(),dp.end());

	r -= s;
	double ret = 0;
	double dt = t;
	for(int i=0;i<SZ(dp);i++)
	{
		double b = dp[i].b;
		double e = dp[i].e;
		double v = dp[i].v;
		double nt = (e-b)/(v+r);
		if(dt < 1e-9)
		{
			ret += (e-b)/v;
		}
		else if( nt < dt)
		{
			ret += nt;
			dt -= nt;
		}
		else
		{
			double ds = e-b - (v+r)*dt;
			double nnt = ds/v;
			ret += (dt+nnt);
			dt = 0;
		}
	}
	//cout<<"Case #"<<tt<<": "<<cin.precision()<<ret<<endl;
	printf("Case #%d: %.7f\n",tt,ret);
}
int main()
{
	int T;
	cin>>T;
	for(int t=1 ; t <= T ; t++)
		run(t);
} 
