#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;



long double R, r, g, f, t;

const long double eps = 1e-9;
const long double eps2 = 1e-12;
const long double Pi = 3.1415926535897932384626433832795;

int n;

void Load()
{
	cin >> f >> R >> t >> r >> g;
	g = g + 2*r;
	n = int((R - t)/ g + 2.0);

	cerr << "f = " << f << " R = " << R << " t = " << t << " r = " << r << " g = " << g << " n = " << n << "\n";

}

// area chord-arc space. chord length in squre.
long double GetAr(long double r, long double ch)
{
	long double a = 1 - ch/(2*r*r);
	a = acos(a);
//	cerr << "alp = " << a << "\n";
	return (a*r*r-sin(a)*r*r)/2.0;

}


// get intersection area of square x1-x2 X y1-y2 and circle radii r
long double Area(long double x1, long double x2, long double y1 , long double y2, long double r)
{

//	cerr << x1 << " " << x2 << " " << y1 << " " << y2 << " " << r << "\n";

	if (x1 > x2 + eps2 && y1 > y2 + eps2) return 0.0;
	int f11, f12, f21, f22;
	f11 = f12 = f21 = f22 = 0;
	long double x, y, xx, yy;
	
	if (x1*x1+y1*y1 > r*r + eps) f11 = 1;
	if (x2*x2+y1*y1 > r*r + eps) f21 = 1;
	if (x1*x1+y2*y2 > r*r + eps) f12 = 1;
	if (x2*x2+y2*y2 > r*r + eps) f22 = 1;

//	cerr << f21<< f22<<"\n"<< f11<< f12 << "\n";


	if (f11 + f12 + f21 + f22 == 4 ) return 0.0;

	if (f11 + f12 + f21 + f22 == 0) return (x2-x1)*(y2-y1);

	if (f11 + f12 + f21 + f22 == 1) // 1 corner cropped
	{
		if (f22 == 1)
		{
			y = sqrt(r*r - x2*x2);
			x = sqrt(r*r - y2*y2);
			return GetAr(r, (x-x2)*(x-x2) + (y-y2)*(y-y2)) + (x2-x1)*(y2-y1) - (x2-x)*(y2-y)/2.0;
		}
		return 0;
	}
	if (f11 + f12 + f21 + f22 == 2) // 1 side cropped
	{
		if (f22 == 1 && f12 == 1)
		{
			y = sqrt(r*r - x1*x1);
			yy = sqrt(r*r - x2*x2);
			return GetAr(r, (y-yy)*(y-yy) + (x2-x1)*(x2-x1)) + (y-y1+yy-y1)*(x2-x1)/2.0;
		}
		if (f21 == 1 && f22 == 1)
		{
			x = sqrt(r*r - y1*y1);
			xx = sqrt(r*r - y2*y2);
			return GetAr(r, (x-xx)*(x-xx) + (y2-y1)*(y2-y1)) + (x-x1+xx-x1)*(y2-y1)/2.0;
		}
		return 0;
	}
	if (f11 + f12 + f21 + f22 == 3) // 1 corner inside
	{
		if (f11 == 0)
		{
			y = sqrt(r*r - x1*x1);
			x = sqrt(r*r - y1*y1);
			return GetAr(r, (x-x1)*(x-x1) + (y-y1)*(y-y1)) + (x-x1)*(y-y1)/2.0;
		}
		return 0;
	}
	return 0;
}

void Solve()
{
	long double tot;
	long double gd;
	tot = Pi * (R) * (R);
	gd = 0;
	int i, j;
	if (g < f + r + eps)
	{
//		cerr << "obvious\n";
		cout << 1.000000 <<"\n";
		return;
	}
	long double cur;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			cur = Area(i*g+f+r, i*g+g-f-r, j*g+f+r, j*g+g-f-r, R-t-f);
			gd += cur;

//			if (cur < 10) cerr << " ";
//			cerr << cur << "\n";
//			cerr << cur << " ";
		}
//		cerr << "\n";
	}
	gd *= 4;
	cout << 1 - gd / tot << "\n";
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(7);
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++)
	{
		cout << "Case #" << tt << ": ";
		Load();
		Solve();
	}
	return 0;
	
}