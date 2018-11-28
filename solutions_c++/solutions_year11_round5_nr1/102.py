#include <iostream>
#include <set>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <sstream>
#include <assert.h>

using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)>(0)?(a):(-(a)))
#define mp make_pair
#define pnt pair<int,int>
#define MEMS(a,b) memset((a),(b),sizeof(a))
#define pb push_back
#define LL long long
#define U unsigned
vector<pnt > low;
vector<pnt > up;
vector<int> a1,a2,b1,b2,c1,c2;
double eps=1e-9;
double finds(double x1, double y1, double x2, double y2, double x3, double y3)
{
	double X1=x2-x1;
	double Y1=y2-y1;
	double X2=x3-x1;
	double Y2=y3-y1;
	return X1*Y2-X2*Y1;
}
double calcs(double x)
{
	vector<pair<double, double> > a,b;
	FOR(i,0,low.size())
		if (low[i].first-eps<=x)
			a.push_back(low[i]);
		else
		{
			double y;
			if (b1[i-1]==0)
				y=low[i-1].second;
			else
				y=(-a1[i-1]*x-c1[i-1])/(double)b1[i-1];
			a.push_back(mp(x,y));
		}
	FOR(i,0,up.size())
		if (up[i].first-eps<=x)
			b.push_back(up[i]);
		else
		{
			double y;
			if (b2[i-1]==0)
				y=up[i-1].second;
			else
				y=(-a2[i-1]*x-c2[i-1])/(double)b2[i-1];
			b.push_back(mp(x,y));
		}
		for (int i=(int) b.size()-1; i>=0; --i)
			a.push_back(b[i]);
		double res=0;
		FOR(i,0,a.size()-1)
			res+=finds(a[0].first,a[0].second,a[i].first,a[i].second,a[i+1].first,a[i+1].second);
		return ABS(res);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(test,1,t+1)
	{
		int w,lo,u,g;
		scanf("%d%d%d%d",&w,&lo,&u,&g);
		low.clear();
		a1.clear();
		a2.clear();
		b1.clear();
		b2.clear();
		c1.clear();
		c2.clear();
		up.clear();
		a1.resize(lo-1);
		b1.resize(lo-1);
		c1.resize(lo-1);
		a2.resize(u-1);
		b2.resize(u-1);
		c2.resize(u-1);
		low.resize(lo);
		FOR(i,0,lo)
			scanf("%d%d",&low[i].first,&low[i].second);
		up.resize(u);
		FOR(i,0,u)
			scanf("%d%d",&up[i].first,&up[i].second);
		FOR(i,0,low.size()-1)
		{
			a1[i]=low[i+1].second-low[i].second;
			b1[i]=low[i].first-low[i+1].first;
			c1[i]=-a1[i]*low[i].first-b1[i]*low[i].second;
		}
		FOR(i,0,up.size()-1)
		{
			a2[i]=up[i+1].second-up[i].second;
			b2[i]=up[i].first-up[i+1].first;
			c2[i]=-a2[i]*up[i].first-b2[i]*up[i].second;
		}
		double s=calcs(w);
		s/=g;
		double left=0;
		printf("Case #%d:\n",test);
		FOR(i,0,g-1)
		{
			double l=0,r=w;
			FOR(it,0,200)
			{
				double m=(l+r)/2;
				double c=calcs(m);
				if (c>(i+1)*s)
					r=m;
				else
					l=m;
			}
			double res=(l+r)/2.0;
			printf("%.10lf\n",res);
		}
	}
	return 0;
}