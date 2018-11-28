#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long ll;

#define EQUAL(a,b) (fabs((a)-(b))<1e-9)

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		
		vector<pair<pair<int,int>,int> > corr;

		int X,S,R,t,N;
		cin>>X>>S>>R>>t>>N;
		R-=S;
		for(int i=0;i<N;i++)
		{
			int a,b,c;
			cin>>a>>b>>c;
			corr.push_back(make_pair(make_pair(a,b),c+S));
		}
		sort(corr.begin(),corr.end());

		vector<pair<double,int> > segs;

		int start = 0;
		for(int i=0;i<N;)
		{
			if (corr[i].first.first!=start)
			{
				segs.push_back(make_pair(S,corr[i].first.first-start));
				start = corr[i].first.first;
			}
			else
			{
				segs.push_back(make_pair(corr[i].second,corr[i].first.second-corr[i].first.first));
				start = corr[i].first.second;
				++i;
			}
		}
		if (start!=X)
			segs.push_back(make_pair(S,X-start));

		sort(segs.begin(),segs.end());

		int n = segs.size();
		double remt = t;
		for(int i=0;i<n;i++)
		{
			if (EQUAL(remt,0)) break;
			double runSpeed = segs[i].first + R;
			double runTime = segs[i].second / runSpeed;
			if (runTime<remt)
			{
				remt-=runTime;
				segs[i].first = runSpeed;
			}
			else
			{
				runTime = remt;
				remt = 0;
				double walkTime = (segs[i].second - runTime*runSpeed) / segs[i].first;
				segs[i].first = segs[i].second/(runTime+walkTime);
			}
		}
		double ans = 0;
		for(int i=0;i<n;i++)
			ans+=segs[i].second/segs[i].first;
		printf("%.9lf\n",ans);

	}
	return 0;
}
