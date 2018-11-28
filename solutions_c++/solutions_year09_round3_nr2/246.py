#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

const int MAX_N = 504;

long long xo, yo, zo, vxo, vyo, vzo;
double dmin, tmin;
int n;

void enter()
{
	cin >> n;
	xo = yo = zo = 0;
	vxo = vyo = vzo = 0;
	for (int i = 0; i < n; ++i)
	{
		long long x, y, z, vx, vy, vz;
		cin >> x >> y >> z >> vx >> vy >> vz;
		xo += x;
		yo += y;
		zo += z;
		vxo += vx;
		vyo += vy;
		vzo += vz;
	}
	/*
	x0 = x0 / n;
	y0 = y0 / n;
	z0 = z0 / n;
	vx0 = vx0 / n;
	vy0 = vy0 / n;
	vz0 = vz0 / n;
	*/
}

void solve()
{
	long long a = vxo * vxo + vyo * vyo + vzo * vzo;
	long long b = 2 * (vxo * xo + vyo * yo + vzo * zo);
	long long c = xo * xo + yo * yo + zo * zo;
	dmin = 1e+15;
	tmin = 1e+15;
	if (a == 0)
	{
		if (b == 0)
		{
			tmin = 0.0;
			dmin = sqrt(c * 1.0) / n;
		}
		else
		{
			if ((double)(-c) / b >= 0)
			{
				tmin = (double)(-c) / b;
				dmin = 0.0;
			}
			else
			{
				tmin = 0.0;
				dmin = sqrt(c * 1.0) / n;
			}
		}
	}
	else
	{
		if (b >= 0)
		{
			tmin = 0.0;
			dmin = sqrt(c * 1.0) / n;
		}
		else
		{
			tmin = (double)(-b) / (2 * a);
			dmin = sqrt(c - (double)(b*b) / (4 * a)) / n;
		}
	}
	
}

int main()
{
	int T;
	cin >> T;
	for (int run = 1; run <= T; ++run)
	{
		enter();
		solve();
		cout << setprecision(8) << fixed << "Case #" << run << ": " << dmin << " " << tmin << endl;
	}
	
	return 0;
}
