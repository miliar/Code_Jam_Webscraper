#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN=1005;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		int X,R,S,t,N;
		vector<pair<int,pair<int,int> > > v;
		printf("Case #%d: ",tt);
		scanf("%d%d%d%d%d",&X,&R,&S,&t,&N);
		int j=0;
		for(int i=0;i<N;i++)
		{
			int b,e,w;
			scanf("%d%d%d",&b,&e,&w);
			if (b!=j)
				v.push_back(make_pair(0,make_pair(j,b)));
			v.push_back(make_pair(w,make_pair(b,e)));
			j=e;
		}
		if (j!=X)
			v.push_back(make_pair(0,make_pair(j,X)));
		sort(v.begin(),v.end());
		double ans=0;
		double left=t;
		for(int i=0;i<(int)v.size();i++)
		{
			int len=v[i].second.second-v[i].second.first;
			if (left*(S+v[i].first)>=len)
			{
				double spend=double(len)/(S+v[i].first);
				left-=spend;
				ans+=spend;
			}
			else
			{
				ans+=left+(double(len)-left*(S+v[i].first))/(R+v[i].first);
				left=0;
			}
		}
		printf("%lf\n",ans);
	}
	return 0;
}
