#include <iostream>
#include <cmath>
using namespace std;

const double EPS = 1e-8;

int n,m;
int p[210],v[210];

bool Test(double t)
{
	double left,right,now=-1e20;
	int i;
	for(i=1;i<=n;++i)
	{
		left=p[i]-t;
		if(now<left) now=left;
		right=now+(v[i]-1)*m;
		if(fabs(p[i]-right)>t+EPS) return false;
		now=right+m;
	}
	return true;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%d%d",&n,&m);
		int i,sumv=0;
		for(i=1;i<=n;++i)
		{
			scanf("%d%d",&p[i],&v[i]);
			sumv+=v[i];
		}
		double l,r,mid;

		l=0;r=m*sumv;
		while(l+EPS<r)
		{
			mid=(l+r)/2;
			if(Test(mid))
			{
				r=mid;
			}
			else
			{
				l=mid+EPS;
			}
		}
		
		printf("Case #%d: %.7lf\n",cas,l);

	}

	return 0;
}