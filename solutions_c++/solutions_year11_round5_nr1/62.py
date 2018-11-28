#include <stdio.h>
#define eps 1E-8
struct P { double x, y; };
P _P(double x, double y) { P p; p.x=x; p.y=y; return p; }
P operator +(P a, P b) { return _P(a.x+b.x, a.y+b.y); }
P operator -(P a, P b) { return _P(a.x-b.x, a.y-b.y); }
double operator *(P a, P b) { return a.x*b.y-a.y*b.x; }
#define N 110
P d[N], u[N], m[2*N];
int nd, nu;
double get(double x)
{
	int i, k;
	double s;
	k=0;
	for(i=0; i<nd && d[i].x+eps<x; m[k++]=d[i], i++);
	if(i==0) return 0;
	m[k++]=_P(x, d[i-1].y+(d[i].y-d[i-1].y)*(x-d[i-1].x)/(d[i].x-d[i-1].x));
	for(i=nu-1; i>=0 && u[i].x-eps>x; i--);
	if(i<nu-1)
		m[k++]=_P(x, u[i+1].y+(u[i].y-u[i+1].y)*(x-u[i+1].x)/(u[i].x-u[i+1].x));
	for(; i>=0; m[k++]=u[i], i--);
	for(s=0, i=2; i<k; s+=(m[i]-m[0])*(m[i-1]-m[0]), i++);
	if(s<0) s=-s;
	return s;
}
int main()
{
	int ts, t, i, g, w, j;
	double s, l, r, c, h;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		scanf("%d%d%d%d", &w, &nd, &nu, &g);
		for(i=0; i<nd; scanf("%lf%lf", &d[i].x, &d[i].y), i++);
		for(i=0; i<nu; scanf("%lf%lf", &u[i].x, &u[i].y), i++);
		s=get(w);
		printf("Case #%d:\n", t+1);
		for(i=0; i<g-1; i++)
		{
			h=(i+1)*s/g;
			for(l=0, r=w, j=0; j<100; j++)
			{
				c=(l+r)/2;
				if(get(c)<h) l=c;
				else r=c;
			}
			printf("%.13lf\n", (r+l)/2);
		}
	}
	return 0;
}