#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
#define all(x) (x.begin(),x.end())
using namespace std;
const double eps=1e-8;
int dblcmp(double d)
{
    if (fabs(d)<eps)return 0;
    return d>eps?1:-1;
}
int a[1200000];
int x,s,r,t,n;
pair<int,int>pr[1200000];
int main()
{
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		memset(a,0,sizeof(a));
		for (i=0;i<x;i++)
		{
			a[i]=s;
		}
		for (i=0;i<n;i++)
		{
			int q,w,e;
			scanf("%d%d%d",&q,&w,&e);
			for (j=q;j<w;j++)
			{
				a[j]=e+s;
			}
		}
		for (i=0;i<x;i++)
		{
			pr[i]=mp(a[i],i);
		}
		sort(pr,pr+x);
		double now=0;
		double ans=0;
		int pos=-1;
		for (i=0;i<x;i++)
		{
			if (fabs(now-t*1.0)<1e-8)break;
			a[pr[i].second]+=r-s;
			double tmp=now;
			now+=1.0/a[pr[i].second];
			if (dblcmp(now-t*1.0)>=0)
			{
				pos=pr[i].second;
				break;
			}
		}
		for (i=0;i<x;i++)
		{
			//if (i==pos)continue;
			ans+=1.0/(a[i]*1.0);
		}
		if (pos>=0)
		{
			now-=t;
			double ss=a[pos]*1.0*now;
			double tt=a[pos]*1.0-(r-s)*1.0;
			//printf("%lf %lf\n",tt,a[pos]*1.0);
			ans+=ss/tt-ss/a[pos]*1.0;
		}
		printf("Case #%d: %.10lf\n",++cc,ans);
	}
	return 0;
}
