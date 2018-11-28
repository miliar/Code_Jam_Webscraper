#include <cstdio>


int Test, n, vis[60];

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*
 * Filename:point.h
 * This file define the type of Point(vector) in 2-dimension graph. It's the base of other functions.
 */
#ifndef POINT_H_MY
#define POINT_H_MY
#include <cmath>
#define ZERO 1e-7
#define PI 3.1415926535897932384626433832795028842

double triangle_area(double a, double b, double c)
{
	double p = (a + b + c) / 2;
	return sqrt(p * (p - a) * (p - b) * (p - c));
}

double check0(double t)
{
	if (fabs(t) < ZERO)
		return 0;
	return t;
}

struct Tpoint
{
	double x, y;
	Tpoint(double _x, double _y):x(_x), y(_y)
	{ }
	Tpoint(double angle):x(cos(angle)), y(sin(angle))
	{ }
	Tpoint():x(0), y(0)
	{}
	inline double getangle()
	{
		return atan2(y, x);
	}
	inline Tpoint rotate(double theta)
	{
		double r = cos(theta), m = sin(theta);
		return Tpoint(r * x - m * y, r * y + m * x);
	}
	inline double len()
	{
		return sqrt(x * x + y * y);
	}
};

inline bool operator ==(Tpoint a, Tpoint b)
{
	return check0(a.x - b.x) == 0 && check0(a.y - b.y) == 0;
}

inline bool operator !=(Tpoint a, Tpoint b)
{
	return check0(a.x - b.x) || check0(a.y - b.y);
}

Tpoint operator +(Tpoint a, Tpoint b)
{
	return Tpoint(a.x + b.x, a.y + b.y);
}

Tpoint operator -(Tpoint a, Tpoint b)
{
	return Tpoint(a.x - b.x, a.y - b.y);
}

Tpoint operator *(Tpoint a, double r)
{
	return Tpoint(a.x * r, a.y * r);
}

Tpoint operator /(Tpoint a, double r)
{
	return Tpoint(a.x / r, a.y / r);
}

Tpoint complex_mul(Tpoint a, Tpoint b)
{
	return Tpoint(a.x * b.x - a.y * b.y, a.x * b.y + a.y * b.x);
}

inline double dot(Tpoint a, Tpoint b)
{
	return check0(a.x * b.x + a.y * b.y);
}

inline double cross(Tpoint a, Tpoint b)
{
	return check0(a.x * b.y - a.y * b.x);
}

#endif
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Tpoint p[60];
double r[60];

bool check2(double c)
{

	int cnt = 0;
	for (int i = 0; i < n; ++i)
	{
		if (!vis[i])
			++cnt;
		if (!vis[i] && r[i] <= c)
			cnt |= 0x10000;
	}
	if (!cnt || cnt == 0x10001)
		return true;
	for (int i = 0; i < n; ++i)
		if (!vis[i])
			for (int j = 0; j < n; ++j)
			{
				if (vis[j] || i == j)
					continue;
				double a = c - r[i], b = c - r[j], d = (p[i] - p[j]).len();
				if (a + b < d - ZERO || a + d < b - ZERO || b + d < a - ZERO)
					continue;
				double coss = acos(check0((a * a + d * d - b * b) / (2 * a * d)));
				Tpoint t = p[j] - p[i];
				t = t.rotate(coss);
				t = t / d * a;
				Tpoint C = p[i] + t;
				int ok = 1;
				for (int k = 0; k < n && ok; ++k)
				{
					if (!vis[k] && (C - p[k]).len() + r[k] > c + ZERO)
						ok = 0;
				}
				if (ok)
					return true;
			}
	return false;
}

#include <cstring>
bool check(double c)
{
	for (int i = 0; i < n; ++i)
	{
		if (r[i] < c)
		{
			memset(vis, 0, sizeof(vis));
			vis[i] = 1;
			if (check2(c))
				return true;
		}
		for (int j = 0; j < n; ++j)
		{
			if (i == j)
				continue;
			double a = c - r[i], b = c - r[j], d = (p[i] - p[j]).len();
			if (a + b < d - ZERO || a + d < b - ZERO || b + d < a - ZERO)
				continue;
			double coss = acos(check0((a * a + d * d - b * b) / (2 * a * d)));
			Tpoint t = p[j] - p[i];
			t = t.rotate(coss);
			t = t / d * a;
			Tpoint C = p[i] + t;
			for (int k = 0; k < n; ++k)
			{
				vis[k] = ((C - p[k]).len() + r[k] < c + ZERO);
			}
			if (check2(c))
				return true;
		}
	}
	return false;
}
void work()
{
	scanf("%d", &n);
	double l = 0, right = 1700;
	for (int i = 0; i < n; ++i)
	{
		scanf("%lf%lf%lf", &p[i].x, &p[i].y, &r[i]);
		if (l < r[i])
			l = r[i];
	}

	while (right - l >= 1e-6)
	{
		double c = (l + right) / 2;
		if (check(c))
			right = c;
		else
			l = c;
	}
	printf("Case #%d: %.6lf\n", ++Test, right);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
