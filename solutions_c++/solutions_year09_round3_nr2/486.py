#include<stdafx.h>
//



#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;
double eps = 1e-9;
struct ff
{
	double x,y,z,vx,vy,vz;
}a[505];
int n;
double calc (double t)
{
	double x, y, z;
	x = y = z = 0;
	for (int i = 0; i < n; i++)
	{
		x += (a[i].x + t * a[i].vx);
		y += (a[i].y + t * a[i].vy);
		z += (a[i].z + t * a[i].vz);
	}
	x /= n;
	y /= n;
	z /= n;
	return (x * x + y * y + z * z);
}
double Slove (double low, double mid, double high)
{
	double middd, midmid;
	middd = (low + mid) / 2;
	midmid = (mid + high) / 2;
	while (fabs (middd - midmid) > eps)
	{
		if (calc (middd) < calc (midmid))
			high = midmid;
		else low = middd;
		mid = (low + high) / 2;
		middd = (low + mid) / 2;
		midmid = (mid + high) / 2;
	}
	
	return (middd + midmid) / 2;
}
int main ()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	int tt = 0;
	int t;
	scanf("%d",&t);
	while (t--)
	{
		tt++;
		scanf("%d",&n);
		for (int i = 0; i < n; i++)
			scanf("%lf %lf %lf %lf %lf %lf",&a[i].x,&a[i].y,&a[i].z,&a[i].vx,&a[i].vy,&a[i].vz);

		double ans = Slove(0, (0+100000.0)/2, 100000.0);
		if (ans > 90000)ans = 0;
		printf ("Case #%d: %lf %lf\n", tt, sqrt(calc(ans)), ans);
	}
}
