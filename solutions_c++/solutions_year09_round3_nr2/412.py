#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;
double eps = 1e-9;
struct node
{
	double x,y,z,vx,vy,vz;
}a[505];
int n;
double cal (double t)
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
double tri (double low, double mid, double high)
{
	double mid1, mid2;
	mid1 = (low + mid) / 2;
	mid2 = (mid + high) / 2;
	while (fabs (mid1 - mid2) > eps)
	{
		//if (fabs (cal (mid1) - cal (mid2)) < eps)break;
		if (cal (mid1) < cal (mid2))
			high = mid2;
		else low = mid1;
		mid = (low + high) / 2;
		mid1 = (low + mid) / 2;
		mid2 = (mid + high) / 2;
		//cout << mid1 << " " << mid2 << endl;
	}
	//cout << "hello\n";
	return (mid1 + mid2) / 2;
}
int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca = 1;
	int t;
	cin >> t;
	while (t--)
	{
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i].x >> a[i].y >> a[i].z >> a[i].vx >> a[i].vy >> a[i].vz;
		double ans = tri(0, (0+100000.0)/2, 100000.0);
		if (ans > 90000)ans = 0;
		//cout << ans << endl;
		//cout << sqrt (cal(0.01)) << endl;
		printf ("Case #%d: %.8lf %.8lf\n", ca++, sqrt(cal(ans)), ans);
	}
}