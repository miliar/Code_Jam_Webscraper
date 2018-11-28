#include<stdio.h>
int p[205];
int v[205];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("b.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		int c,d;
		int total=0;
		scanf("%d %d",&c,&d);
		for(int i=0;i<c;i++)
		{
			scanf("%d %d",&p[i],&v[i]);
		}
		double dist;
		double l=0.0,r=10000000000000.0;
		while(r-l>1e-7)
		{
			dist=(l+r)/2;
			double now = -1000000000.0;
			for(int i=0;i<c;i++)
			{
				if(p[i]-dist<now)
				{
					now=now+d*v[i];
				}
				else
				{
					now=(p[i]-dist)+d*v[i];
				}
				if(now-d>p[i]+dist)
				{
					l=dist;
					break;
				}
				if(i==c-1) r=dist;
			}
		}
		dist=(l+r)/2;
		printf("Case #%d: %.10lf\n",t,dist);
	}
	return 0;
}
