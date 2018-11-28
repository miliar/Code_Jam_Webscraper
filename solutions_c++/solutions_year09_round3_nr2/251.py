#include <iostream>
#include <cmath>
char mark[128];
inline double calc(double x, double y, double z)
{
	return x*x + y*y + z*z;
}
void solve()
{
	int i, j;
	int n;
	double x0, y0, z0;
	double tx, ty, tz;
	double vx, vy, vz;

	x0=y0=z0=vx=vy=vz=0;

	scanf("%d", &n);
	for(i=0;i<n;i++)
	{
		scanf("%lf%lf%lf", &tx, &ty, &tz);
		x0+=tx;
		y0+=ty;
		z0+=tz;
		scanf("%lf%lf%lf", &tx, &ty, &tz);
		vx+=tx;
		vy+=ty;
		vz+=tz;
	}
	x0/=n;
	y0/=n;
	z0/=n;
	vx/=n;
	vy/=n;
	vz/=n;
	
	//emunate time 
	double delta = 1e100; 
	double tl, tr, t= delta;
	double left, right, mid;
	mid = calc(x0+vx*t, y0+vy*t, z0+vz*t);
	while(delta > 1e-10)
	{
		tl = t-delta;
		tr = t+delta;
		if(tl>=0)
			left = calc(x0+vx*tl, y0+vy*tl, z0+vz*tl);
		right = calc(x0+vx*tr, y0+vy*tr, z0+vz*tr);
		if(tl<0 || left > right)
		{
			if(right<=mid)
				mid = right, t = tr;
		}
		else 
		{
			if(left<=mid)
				mid = left, t = tl;
		}
		delta /=2;
	}
	printf("%.8lf %.8lf\n", sqrt(mid), t);
	return;
}
int main()
{
	int ncase, icase;
	freopen("test.in", "r+", stdin);
	freopen("test.out", "w+", stdout);
	scanf("%d", &ncase);
	for(icase = 1;icase<=ncase;icase++)
	{
		printf("Case #%d: ", icase);
		solve();
	}
	return 0;
}