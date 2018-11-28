#include <stdio.h>

int cases, c, v;
double t, d, p, x;

int main()
{
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		t=0; x=-1000000000;
		scanf(" %d %lf", &c, &d);
		for(int i=0; i<c; i++)
		{
			scanf(" %lf %d", &p, &v);
			for(int j=0; j<v; j++)
			{
				double y=p;
				if (y-t>x+d) y-=t;
				else if (y+t<x+d) y+=t;
				else y=x+d;


				double dt=(d-(y-x))/2.0;
				if (dt<0) dt=0;
				x=y+dt;
				t+=dt;
				// printf("%f %f\n", t, x);
			}
		}
		printf("Case #%d: %.1f\n", cs, t);
	}
	return 0;
}
