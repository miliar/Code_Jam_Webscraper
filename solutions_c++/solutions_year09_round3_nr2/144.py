#include <valarray>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

typedef valarray<double> Vector;

Vector make_vector(double x, double y, double z)
{
	Vector res(3);
	res[0] = x;
	res[1] = y;
	res[2] = z;
	return res;
}

double dot(const Vector& a, const Vector& b)
{
	double res = 0;
	for (int i = 0; i < 3; ++i)
		res += a[i] * b[i];
	return res;
}

int main()
{
	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		int n;
		scanf("%d", &n);

		Vector p(3), v(3);
		for (int i = 0; i < n; ++i)
		{
			double x, y, z, dx, dy, dz;
			cin >> x >> y >> z >> dx >> dy >> dz;
			p += make_vector(x, y, z);
			v += make_vector(dx, dy, dz);
		}
		p /= n;
		v /= n;

		double tt;
		if (dot (v, v) == 0)
			tt = 0.;
		else
			tt = max(dot(v, -p) / dot(v, v), 0.);

		Vector w = p + tt * v;
		double dd = sqrt(dot(w, w));

		printf("Case #%d: %.8f %.8f\n", t, dd, tt);
	}

	return 0;
}
