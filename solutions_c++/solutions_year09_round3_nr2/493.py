#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define pb push_back
#define sqr(a) ((a) * (a))

const int LINE = 1000100;

struct tr
{
public:
	double x, y, z, vx, vy, vz;
	tr(double X = 0, double Y = 0, double Z = 0, double Vx= 0, double Vy = 0, double Vz = 0)
	{
		x = X, y = Y, z = Z, vx = Vx, vy = Vy, vz = Vz;
	}
};

vector<tr> bd;
int n;

double dist(double t9)
{
	tr m9 = tr(0, 0, 0, 0, 0, 0);
	forn(i, n)
	{
		m9.x += bd[i].x + bd[i].vx * t9;
		m9.y += bd[i].y + bd[i].vy * t9;
		m9.z += bd[i].z + bd[i].vz * t9;
	}
	m9.x = m9.x / (double)(n);
	m9.y = m9.y / (double)(n);
	m9.z = m9.z / (double)(n);
	return sqrt(1. * sqr(m9.x) + sqr(m9.y) + sqr(m9.z));
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	tr el;
	for(int itm = 1; itm <= T; ++itm)
	{
		scanf("%d", &n);
		forn(i, n)
		{
			scanf("%lf %lf %lf %lf %lf %lf", &el.x, &el.y, &el.z, &el.vx, &el.vy, &el.vz);
			bd.pb(el);
		}
		double d0 = dist(0), t0 = 0;

		double A = 0, B = 0;
		double s1 = 0, s2 = 0;
		forn(i, n)
			s1 += bd[i].x;
		forn(i, n)
			s2 += bd[i].vx;
		A += s1 * s2;
		s1 = 0, s2 = 0;
		forn(i, n)
			s1 += bd[i].y;
		forn(i, n)
			s2 += bd[i].vy;
		A += s1 * s2;
		s1 = 0, s2 = 0;
		forn(i, n)
			s1 += bd[i].z;
		forn(i, n)
			s2 += bd[i].vz;
		A += s1 * s2;

		s1 = 0;
		forn(i, n)
			s1 += bd[i].vx;
		B += sqr(s1);

		s1 = 0;
		forn(i, n)
			s1 += bd[i].vy;
		B += sqr(s1);

		s1 = 0;
		forn(i, n)
			s1 += bd[i].vz;
		B += sqr(s1);

		double t1 = -1 * A / B;
		double d1 = 1e9;
		if(t1 > 0)
			d1 = dist(t1);
		if(d1 < d0)
		{
			d0 = d1;
			t0 = t1;
		}

		printf("Case #%d: %.10lf %.10lf\n", itm, d0, t0);
		bd.clear();
	}
	return 0;
}

