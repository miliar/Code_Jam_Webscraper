#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;


const long double eps = 1e-9;

class Circle
{
	public:
	long double x, y, r;
};



Circle c[100];
int n;

void Load()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> c[i].x >> c[i].y >> c[i].r;

}



int was[100];


int Inter(Circle &a, Circle &b, long double &x, long double &y)
{
	long double A, B, C;
	if (a.r < -eps || b.r < -eps) return 0;
	long double x1, y1, dx, dy, t;
	A = -2*(b.x - a.x);
	B = -2*(b.y - a.y);
	if (fabs(A) < eps && fabs(B) < eps) return 0;
	C = -b.r*b.r + a.r*a.r + b.y*b.y + b.x*b.x - a.y*a.y - a.x*a.x;
	if (fabs(A) > eps)
	{
		y1 = 0;
		x1 = -C / A;
	}
	else
	{
		x1 = 0;
		y1 = -C / B;
	}
	dx = -B;
	dy = A;
	A = dx*dx+dy*dy;
	B = 2*(x1-a.x)*dx + 2*(y1-a.y)*dy;
	C = (x1-a.x)*(x1-a.x) + (y1-a.y)*(y1-a.y) - a.r*a.r;
	long double D;
	D = B*B-4*A*C;
	if (D < -eps) return 0;
	D = sqrt(fabs(D));
	t = (-B-D) / (2*A);
	x = x1 + dx * t;
	y = y1 + dy * t;
	return 1;
}




int Good(Circle &c, long double x, long double y, long double R)
{
	long double t = (c.x - x)*(c.x - x) +  (c.y - y)*(c.y - y);
	t = sqrt(fabs(t));
	if (t + c.r > R + eps) return 0;
	else return 1;
}

int Check(int a1, int a2, int a3, int a4, long double R)
{
	Circle a, b, c, d;
	long double x1, y1, x2, y2;
	if (a1 >= 0)
	{
		a = ::c[a1]; b = ::c[a2]; 
		a.r = R - a.r;
		b.r = R - b.r;
		if (!Inter(a, b, x1, y1)) return 0;
	}
	else
	{
		x1 = ::c[a2].x;
		y1 = ::c[a2].y;
	}

	if (a3 >= 0)
	{
		c = ::c[a3]; d = ::c[a4];
		c.r = R - c.r;
		d.r = R - d.r;	
		if (!Inter(c, d, x2, y2)) return 0;
	}
	else
	{
		x2 = ::c[a4].x;
		y2 = ::c[a4].y;		
	}
	
	
	


	for (int i = 0; i < n; i++)
	{
		if (!Good(::c[i], x1, y1, R) && !Good(::c[i], x2, y2, R)) return 0;
	}


	return 1;

}

int Test(long double R)
{
	int i, j, k, l;

	for (i = -1; i < n; i++)
	{
		for (j = 0; j <= n; j++)
		{
			if (i == j) continue;
			for (k = -1; k < n; k++)
			{
				for (l = 0; l < n; l++)
				{
					if (k == l) continue;
					if (Check(i, j, k, l, R)) return 1;
				}
			}
		}
	}
	return 0;

}


void Solve()
{
	long double l, r, m;
	l = 0;
	r = 20000;
	while (r - l > 1e-9)
	{
		m = (l + r) / 2.0;
		if (Test(m))
			r = m;
		else l = m;
	}

	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(9);
	cout << (l + r) / 2.0 << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
