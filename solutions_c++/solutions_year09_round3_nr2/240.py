#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <list>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a)*(a))

typedef long long ll;

struct Vector{
	double x, y, z;
	Vector(double X = 0, double Y = 0, double Z = 0) : x(X), y(Y), z(Z) {};
	Vector operator * (double a)
	{
		return Vector(x * a, y * a, z * a);
	}
	Vector operator + (Vector &b)
	{
		return Vector(x + b.x, y + b.y, z + b.z);
	}
	void norm()
	{
		double l = sqrt(sqr(x) + sqr(y) + sqr(z));
		x /= l;
		y /= l;
		z /= l;
	}
};

double angle(Vector a, Vector b)
{
	a.norm();b.norm();
	return (a.x * b.x + a.y * b.y + a.z * b.z);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	REP(tt, t)
	{
		int n;
		scanf("%d", &n);
		double x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0;
		int X, Y, Z, Vx, Vy, Vz;
		REP(i, n)
		{
			scanf("%d%d%d%d%d%d", &X, &Y, &Z, &Vx, &Vy, &Vz);
			x += X;y += Y;z += Z;vx += Vx;vy += Vy;vz += Vz;
		}
		x /= (double)n;
		y /= (double)n;
		z /= (double)n;
		vx /= (double)n;
		vy /= (double)n;
		vz /= (double)n;
//		cerr << tt + 1 << " " << x << " " << y  << " " << z << " " << vx << " " << vy << " " << vz << endl;
		if ((fabs(x) < 1e-9 && fabs(y) < 1e-9 && fabs(z) < 1e-9) || (fabs(vx) < 1e-9 && fabs(vy) < 1e-9 && fabs(vz) < 1e-9))
		{
			printf("Case #%d: %.8lf 0.0000000\n", tt + 1, sqrt(sqr(x) + sqr(y) + sqr(z)));
			continue;
		}
		if (fabs(x * vy - vx * y) < 1e-9 && fabs(x * vz - vx * z) < 1e-9 && fabs(y * vz - vy * z) < 1e-9)
		{
			double K = 0.0;
			if (fabs(vx) > 1e-9)
				K = - x / vx;
			else if (fabs(vy) > 1e-9)
				K = - y / vy;
			else
				K = - z / vz;
			if (K <= 1e-9)
			{
				printf("Case #%d: %.8lf 0.0000000\n", tt + 1, sqrt(sqr(x) + sqr(y) + sqr(z)));
				continue;
			}
			else
			{
				printf("Case #%d: %.8lf %.8lf\n", tt + 1, 0.0, K);
				continue;
			}
		}
		double kk = 0;
		double cosa = angle(Vector(-x, -y, -z), Vector(vx, vy, vz));
		if (cosa <= 1e-9)
		{
			printf("Case #%d: %.8lf %.8lf\n", tt + 1, sqrt(sqr(x) + sqr(y) + sqr(z)), 0.0);
			continue;
		}
		double T = sqrt(sqr(x) + sqr(y) + sqr(z)) * cosa / sqrt(sqr(vx) + sqr(vy) + sqr(vz));
//		cerr << x << " " << y  << " " << z << " " << vx << " " << vy << " " << vz << endl;
		Vector tmp = (Vector(vx, vy, vz) * T);
		Vector p = Vector(x, y, z) + tmp;
//		cerr << p.x << " " << p.y << " " << p.z << endl;
		double dst = sqrt(sqr(p.x) + sqr(p.y) + sqr(p.z));
		printf("Case #%d: %.8lf %.8lf\n", tt + 1, dst, T);
	}
	return 0;
}
