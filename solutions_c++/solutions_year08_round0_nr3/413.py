#include <stdio.h>
#include <math.h>
#include <cassert>


template <class T>
T sqr(T a)
{
	return a * a;
}

const double eps = 1e-7;
const double Pi = 4*atan(1.);
class point
{
public:
	double x,y;
	point(double x = 0., double y = 0.)
	{
		this->x = x;
		this->y = y;
	}
	point operator + (point p)
	{
		return point (x + p.x, y + p.y);
	}
	point operator * (double a)
	{
		return point (x * a, y * a);
	}
	bool operator == (point p)
	{
		return fabs(x - p.x) + fabs(y - p.y) < eps;
	}
	bool operator != (point p)
	{
		return fabs(x - p.x) + fabs(y - p.y) > eps;
	}
};

const point inside = point(-1., -1.);
const point outside = point(-2., -2.);

class segment
{
public:
	point a,b;
	segment(point a = point(0,0), point b = point(0,0))
	{
		this->a = a;
		this->b = b;
	}
	point intersect(double r)
	{
		double r1, r2;
		r1 = sqrt(sqr(a.x) + sqr(a.y));
		r2 = sqrt(sqr(b.x) + sqr(b.y));
		if (r1 - r > eps && r2 - r > eps)
			return outside;
		if (r1 -r < - eps && r2 -r < - eps)
			return inside;
		double A, B, C;
		A = sqr(a.x - b.x) + sqr(a.y - b.y);
		B = 2 * (a.x*b.x +a.y*b.y - sqr(b.x) - sqr(b.y));
		C = sqr(b.x) + sqr(b.y) - sqr(r);
		double _a = (-B + sqrt(sqr(B) - 4*A*C)) / (2.*A);
		if (_a < -eps || _a > 1 + eps)
			_a = (-B - sqrt(sqr(B) - 4*A*C)) / (2.*A);
		return a * _a + b * (1 - _a);
	}
	double length()
	{
		return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
	}
	double area(double R)
	{
		double len = length()/2;
		return R*R*asin(len/R) - sqrt(sqr(R)-sqr(len))*len;
	}
};

void solve(int test_case)
{
	double f, R, r, t, g;
	scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
	t += f;
	r += f;
	g -= f * 2.;
	R -= t;
	double answer = 0;
	if (g <= 0)
	{
		answer = 0;
	}
	else
	for(int i = 0; ; i++)
	{
		point ld, lu, rd, ru;
		for(int j = 0; ; j++)
		{
			ld = point(i * (g + 2*r) + r, j * (g + 2*r) + r);
			lu = point(i * (g + 2*r) + r, j * (g + 2*r) + r + g);
			rd = point(i * (g + 2*r) + r + g, j * (g + 2*r) + r);
			ru = point(i * (g + 2*r) + r + g, j * (g + 2*r) + r + g);
			if (sqr(ld.x) + sqr(ld.y) >= sqr(R) - eps)
				break;
			if (sqr(ru.x) + sqr(ru.y) <= sqr(R) + eps)
			{
				answer += g*g;
				continue;
			}
			point left = segment(ld, lu).intersect(R);
			point right = segment(rd,ru).intersect(R);
			point up = segment(lu,ru).intersect(R);
			point down = segment(rd,ld).intersect(R);
			if (down != inside && left != inside)
				answer += segment(down,ld).length()*segment(left, ld).length()/2 + segment(left, down).area(R);
			else if (down != inside && up != outside)
				answer += (segment(down,ld).length() + segment(up, lu).length())*g/2 + segment(up, down).area(R);
			else if (left != inside && right != outside)
				answer += (segment(left,ld).length() + segment(right, rd).length())*g/2 + segment(left, right).area(R);
			else if (up != outside && right != outside)
				answer += g*g - segment(right, ru).length()*segment(up, ru).length()/2 + segment(up, right).area(R);
			else
			{
				assert(false);
			}
		}
		if (ld.x > R)
			break;
	}
	answer = (Pi*sqr(R+t) - 4 * answer) / (Pi*sqr(R+t));
	if (answer <= 0)
		answer = 0;
	if (answer > 1)
		answer = 1;
	printf("Case #%d: %.6lf\n", test_case, answer);

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);
	return 0;
}
