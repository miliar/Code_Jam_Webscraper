#include <stdio.h>
#define N 1000100
long long x[N];
int main()
{
	int i, j, k, n, t, ts;
	long long d, l, r, c, h;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%lld", &k, &h), h*=2, n=0; k--; )
			for(scanf("%lld%d", &d, &j); j--; x[n++]=2*d);
		for(l=0, r=h*n; l<r; )
		{
			c=(l+r)/2;
			d=x[0]-c;
			for(i=0; i<n; i++)
				if(d<x[i])
				{
					if(x[i]-c>d) d=x[i]-c; 
					d+=h;
				}
				else
				{
					if(x[i]+c<d) break;
					d+=h;
				}
			if(i<n) l=c+1;
			else r=c;
		}
		printf("Case #%d: %lld.%lld\n", t+1, r/2, r%2*5);
	}
	return 0;
}