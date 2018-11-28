#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<utility>
#include<climits>
#include<complex>
#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>

using namespace std;

double eps=1e-8;
int dblcmp(double d)
{
    if (fabs(d)<eps)return 0;
    return d>eps?1:-1;
}

int n;
pair<double,double>pr[1200000];

double d; 

double p[1200000];

int main()
{
	freopen("C:\\1\\out.txt","w",stdout);
	int i,j,k;
	int  _;
	int T=0;
	scanf("%d",&_);
	while (_--)
	{
		scanf("%d%lf",&n,&d);
		int pos=0;
		for (i=0;i<n;i++)
		{
			double h;
			int g;
			scanf("%lf%d",&h,&g);
			while (g--)
			{
				p[pos++]=h;
			}
		}
		sort(p,p+pos);
		double l=0,r=1e8;
		int cnt=300;
		while (cnt--)
		{
			double m=(l+r)/2.0;
			for (i=0;i<pos;i++)
			{
				pr[i]=make_pair(p[i]-m,p[i]+m);
			}
			double lim=d+pr[0].first;
			for (i=1;i<pos;i++)
			{
				if (dblcmp(pr[i].first-lim)>=0)
				{
					lim=pr[i].first+d;
					continue;
				}
				if (dblcmp(pr[i].second-lim)>=0)
				{
					lim+=d;
					continue;
				}
				break;
			}
			if (i==pos)
			{
				r=m;
			}
			else 
			{
				l=m;
			}
		}
		printf("Case #%d: %.10lf\n",++T,l);
	}
	return 0;
}
