#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;
typedef unsigned long long LLU;
typedef long long LL;
typedef pair<double,double> pdd;
#define mp make_pair
#define pb push_back
const int INF=99999999;
const double PI=3.1415926535897932384626;
const double EPS=1E-11;
vector<pdd> low,up;
double geta(vector<pdd>& poly)
{
//	printf("poly\n");
	double s=0;
	for(int i=0;i<poly.size();i++)
	{
//		printf(": %lf %lf\n",poly[i].first,poly[i].second);
		s+=poly[i].first*poly[(i+1)%poly.size()].second;
		s-=poly[i].second*poly[(i+1)%poly.size()].first;
	}
	return fabs(s)/2;
}
double cutoff(double x) // to the right
{
	vector<pdd> t;
	{
		int i=lower_bound(low.begin(),low.end(),make_pair(x,1E20))-low.begin();
		if(i==low.size())
			return 0;
		if(i==0)
		{
			for(int j=0;j<low.size();j++)
				t.push_back(low[j]);
		}
		else
		{
			t.push_back(mp(x,(low[i].second-low[i-1].second)/(low[i].first-low[i-1].first)*(x-low[i-1].first)+low[i-1].second));
			for(int j=i;j<low.size();j++)
				t.push_back(low[j]);
		}
	}
	{
		int i=lower_bound(up.begin(),up.end(),make_pair(x,1E20))-up.begin();
		if(i==up.size())
			return 0;
		if(i==0)
		{
			for(int j=up.size()-1;j>=0;j--)
				t.push_back(up[j]);
		}
		else
		{
			for(int j=up.size()-1;j>=i;j--)
				t.push_back(up[j]);
			t.push_back(mp(x,(up[i].second-up[i-1].second)/(up[i].first-up[i-1].first)*(x-up[i-1].first)+up[i-1].second));
		}
	}
	return geta(t);
}
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		int width,lown,upn;
		scanf("%d%d%d",&width,&lown,&upn);
		int g;
		scanf("%d",&g);
		low.clear();
		for(int i=0;i<lown;i++)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			low.pb(pdd(a,b));
		}
		up.clear();
		for(int i=0;i<upn;i++)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			up.pb(pdd(a,b));
		}
		double tarea=cutoff(-1E20);
//		printf("%lf\n",tarea);
		vector<double> ans;
		for(int i=g-1;i>0;i--)
		{
			double targ=(double)tarea*(double)i/g;
			double low=0,high=width,mid;
			for(int it=0;it<50;it++)
			{
				mid=(low+high)/2;
				double t=cutoff(mid);
//				printf("%lf %lf\n",msid,cutoff(mid));
				if(t>targ)
					low=mid;
				else
					high=mid;
			}
			ans.pb(low);
		}
		printf("Case #%d:\n",tn);
		for(int i=0;i<ans.size();i++)
			printf("%.8f\n",ans[i]);
	}
}
