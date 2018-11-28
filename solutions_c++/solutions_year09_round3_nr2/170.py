#include <stdio.h>
#include <math.h>
#define N 600
#define eps 1E-9
struct P { double x, y, z; };
P _P(double x, double y, double z) { P p; p.x=x; p.y=y; p.z=z; return p; }
P operator +(P a, P b) { return _P(a.x+b.x, a.y+b.y, a.z+b.z); }
P operator -(P a, P b) { return _P(a.x-b.x, a.y-b.y, a.z-b.z); }
P operator *(P a, double k) { return _P(a.x*k, a.y*k, a.z*k); }
double operator &(P a, P b) { return a.x*b.x+a.y*b.y+a.z*b.z; }
double operator !(P a) { return sqrt(a&a); }
P b[N], v[N], B, V, O, a;
int main()
{
	int i, t, ts, n;
	O=_P(0, 0, 0);
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(B=O, V=O, scanf("%d", &n), i=0; i<n; scanf("%lf%lf%lf%lf%lf%lf", &b[i].x, &b[i].y, &b[i].z, &v[i].x, &v[i].y, &v[i].z), B=B+b[i], V=V+v[i], i++);
		B=B*(1.0/n);
		V=V*(1.0/n);
		if((V&(O-B))<eps)
			printf("Case #%d: %.9lf %.9lf\n", t+1, !B, 0.0);
		else
		{
			a=V*(((O-B)&V)/(V&V));
			printf("Case #%d: %.9lf %.9lf\n", t+1, !(B+a), !a/!V);
		}
	}
	return 0;
}