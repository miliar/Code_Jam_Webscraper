#include <cstdio>

#define max(a,b) (((a)>(b))?(a):(b))

int p[222], v[222];
double x[222], y[222];

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		int d,c;
		scanf("%d%d", &c, &d);
		for (int j=0;j<c;j++)
			scanf("%d%d", &p[j], &v[j]);
		for (int i=0;i<c;i++)
		{
			x[i]=p[i]-1.0*d*(v[i]-1)/2.0;
			y[i]=p[i]+1.0*d*(v[i]-1)/2.0;
		}
		double cm = p[0]-x[0];
		for (int i=1;i<c;i++)
		{
			if (x[i]-y[i-1]>=d)
			{
				if (cm>p[i]-x[i])				
				{
					double tx = y[i-1]+d;
					double ty = y[i]+tx-x[i];
					double tt = p[i]-tx;
					if (tt>cm)
					{
						tx += tt-cm;
						ty += tt-cm;
					}
					x[i]=tx;
					y[i]=ty;
				}
				cm = max(cm, p[i]-x[i]);
			}
			else
			{
				double tx = y[i-1]+d;
				double ty = y[i]+tx-x[i];
				double tt = ty-p[i];
				if (tt > cm)
				{
					x[i]=tx-(tt-cm)/2;
					y[i]=ty-(tt-cm)/2;
					cm=(tt+cm)/2;					
				}
				else
				{
					x[i]=tx;
					y[i]=ty;
				}
			}
		}
		printf("Case #%d: %.7lf\n", i, cm);		
	}
	return 0;
}