#include <stdio.h>
#include <math.h>
#include <vector>

const double eps = 1e-12;

#define sqr(a) ((a)*(a))
#define sign(a) ((a) < 0 ? -1 : 1)
#define PI       3.14159265358979323846

struct vector
{
	double x, y;
	vector(double X = 0.0, double Y = 0.0) { x = X; y = Y; }
	double operator *(const vector &t) const
	{
		return x * t.x + y * t.y;
	}
	vector operator *(const double &t) const
	{
		return vector(x * t, y * t);
	}
	vector operator +(const vector &t) const
	{
		return vector(x + t.x, y + t.y);
	}
	vector operator -(const vector &t) const
	{
		return vector(x - t.x, y - t.y);
	}
	double len()
	{
		return sqrt(*this * *this);
	}
	bool operator !=(const vector &t)
	{
		return abs(x - t.x) > eps || abs(y - t.y) > eps;
	}
} zero;


vector inter(const vector &r0, const vector &r1, double r)
{
	vector a = r1 - r0;
	double d4 = sqr(a * r0) - sqr(a) * (sqr(r0) - sqr(r));
	if (d4 < 0.0) return vector();
	double t = (-(a * r0) - sqrt(d4)) / sqr(a);
	if (eps <= t && t <= 1 + eps) return r0 + a * t;
	t = (-(a * r0) + sqrt(d4)) / sqr(a);
	if (eps <= t && t <= 1 + eps) return r0 + a * t;
	return vector();
}

double d, h, g, r;

inline double norm(double c)
{
	if (c > 1.0) return 0;
	return acos(c);
}

double area(double x, double y)
{
	vector t(x, y);
	if (t * t <= r * r) return x * y;
	std::vector<vector> p;
	vector tmp;
	tmp = inter(vector(0, 0), vector(x, 0), r);
	if (tmp != zero) p.push_back(tmp);
	tmp = inter(vector(x, 0), vector(x, y), r);
	if (tmp != zero) p.push_back(tmp);
	tmp = inter(vector(x, y), vector(0, y), r);
	if (tmp != zero) p.push_back(tmp);
	tmp = inter(vector(0, y), vector(0, 0), r);
	if (tmp != zero) p.push_back(tmp);
	if (p.size() != 2) throw "something wrong!";
  	double l = norm(p[0] * p[1] / sqrt(sqr(p[0]) * sqr(p[1])));
	return (r * r * l * sign(x * y) + p[0].x * p[0].y + p[1].x * p[1].y) / 2;
}

double area(int n, int m)
{
	return 
		area(d * n + h, d * m + h) +
		area(d * n + h + g, d * m + h + g) -
		area(d * n + h, d * m + h + g) -
		area(d * n + h + g, d * m + h);
}

double go()
{
	if (g < 0 || r < 0) return 0.0;
	double ret = 0.0;
	for (int n = -60; n <= 60; ++n)
		for (int m = -60; m <= 60; ++m)
			ret += abs(area(n, m));
	return ret;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
	{
		double f, R, t, r, g;
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		d = 2 * r + g;
		h = r + f;
		::g = g - 2 * f;
		::r = R - t - f;
		printf("Case #%d: %.6lf\n", i, abs(1 - go() / (PI * R * R)));
	}
}