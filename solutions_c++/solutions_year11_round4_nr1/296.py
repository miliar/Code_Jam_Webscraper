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
vector<pair<int,pnt> > b;
vector<pair<pnt,int> > a;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(test,0,t)
	{
		a.clear();
		b.clear();
		int x,s,r,tim,n;
		scanf("%d%d%d%d%d",&x,&s,&r,&tim,&n);
		double tt=tim;
		double res=0;
		FOR(i,0,n)
		{
			int left,right,v;
			scanf("%d%d%d",&left,&right,&v);
			a.push_back(mp(mp(left,right),v));
		}
		sort(a.begin(),a.end());
		if (a[0].first.first>0)
			b.push_back(mp(0,mp(0,a[0].first.first)));
		int last=a[0].first.second;
		pair<int, pnt> tmp;
		tmp.first=a[0].second;
		tmp.second=a[0].first;
		b.push_back(tmp);
		FOR(i,1,a.size())
		{
			if (a[i].first.first>last)
				b.push_back(mp(0,mp(last,a[i].first.first)));
			last=a[i].first.second;
			pair<int, pnt> tmp;
			tmp.first=a[i].second;
			tmp.second=a[i].first;
			b.push_back(tmp);
		}
		if (last<x)
			b.push_back(mp(0,mp(last,x)));
		sort(b.begin(),b.end());
		FOR(i,0,b.size())
		{
			double dist=tt*(b[i].first+r);
			if (dist>=b[i].second.second-b[i].second.first)
			{
				tt-=(b[i].second.second-b[i].second.first)/(double)(b[i].first+r);
				res+=(b[i].second.second-b[i].second.first)/(double)(b[i].first+r);
			}
			else
			{
				res+=tt;
				tt=0;
				res+=(b[i].second.second-b[i].second.first-dist)/(double)(b[i].first+s);
			}
		}
		printf("Case #%d: %.10lf\n",test+1,res);
	}
	return 0;
}
