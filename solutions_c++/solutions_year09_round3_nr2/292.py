#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

struct point
{
	double x, y, z;

	point() {}

	point(double _x, double _y, double _z)
	{
		x = _x;
		y = _y;
		z = _z;
	}

	point(const point &p)
	{
		x = p.x;
		y = p.y;
		z = p.z;
	}

	point &operator = (const point &p)
	{
		x = p.x;
		y = p.y;
		z = p.z;

		return *this;
	}

	point operator +(point &p)
	{
		point l(*this);
		l.x += p.x;
		l.y += p.y;
		l.z += p.z;

		return l;
	}

	point operator -(point &p)
	{
		point l(*this);
		l.x -= p.x;
		l.y -= p.y;
		l.z -= p.z;

		return l;
	}

	point operator / (double k)
	{
		return point(x / k, y / k, z / k);
	}

	point operator * (double k)
	{
		return (*this) / (1 / k);
	}

	double operator * (point &p)
	{
		return x * p.x + y * p.y + z * p.z;
	}

	double norm()
	{
		return sqrt(x * x + y * y + z * z);
	}
};

typedef vector<point> vp;

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int n;
	scanf("%d\n", &n);

	for (int step = 0; step < n; step++)
	{
		int m;
		cin >> m;

		vp a, av;
		double _x, _y, _z;
		for (int i = 0; i < m; i++)
		{
			cin >> _x >> _y >> _z;
			a.push_back(point(_x, _y, _z));

			cin >> _x >> _y >> _z;
			av.push_back(point(_x, _y, _z));
		}

		point cm(a[0]), cv(av[0]);
		for (int i = 1; i < m; i++)
		{
			point vm = a[i] - cm;

			cm = cm + (vm / (i + 1)); 
			cv = cv + av[i]; 
		}

		cv = cv / m;

		point o(0, 0, 0);
		point ocm(o - cm);

		if (cv.norm() < 1e-9)
		{
			cout .precision(12);
			cout << "Case #" << step + 1 << ": ";
			cout << ocm.norm() << " " << 0 << endl;
			continue;
		}
		double d = (ocm * cv) / cv.norm();
		double t;
		if (d < 0)
		{
			d = cm.norm();
			t = 0;
		}
		else
		{
			t = d / cv.norm();
			d = point(o - (cm + (cv * t))).norm();
		}

		cout .precision(12);
		cout << "Case #" << step + 1 << ": ";
		cout << d << " " << t << endl;
	}

	return 0;
}