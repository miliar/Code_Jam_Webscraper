#include<cstdio>
#include<algorithm>

using namespace std;

#define MX 1001001

int tt;
int c,d;
int P[MX];

int main()
{
	scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		scanf("%d%d",&c,&d);
		int n=0;
		for(int i=0;i<c;++i)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			while(b--) P[n++]=a;
		}
		double a=0,b=1e13;
		while(b-a>1e-11)
		{
			double m=(a+b)*.5;
			double x=P[0]-m-2*d;
			int ok=1;
			for(int i=0;i<n;++i)
			{
				double xa=P[i]-m,xb=P[i]+m;
				if (x+d<xa)
				{
					x=xa;
				}
				else if (x+d<=xb)
				{
					x=x+d;
				}
				else
				{
					ok=0;
					break;
				}
			}
			if (ok) b=m; else a=m;
		}
		printf("Case #%d: ",t);
		printf("%.11lf\n",b);
	}
	return 0;
}
