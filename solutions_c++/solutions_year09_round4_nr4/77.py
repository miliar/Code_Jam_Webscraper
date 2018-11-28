#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
using namespace std;
#define sz(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(), (a).end()
typedef pair<int, int> pii;
typedef vector<int> vint;
typedef long long lint;

const double eps = 1e-8;
inline bool eq(double a, double b)
{
	return fabs(a - b) < eps;
}
inline bool lt(double a, double b)
{
	return a < b && !eq(a, b);
}
inline bool gt(double a, double b)
{
	return a > b && !eq(a, b);
}
inline bool le(double a, double b)
{
	return a < b || eq(a, b);
}



struct Point
{
	double x, y;
	Point(double x = 0, double y = 0) : x(x), y(y) {}
};
inline Point operator-(Point a, Point b)
{
	return Point(a.x - b.x, a.y - b.y);
}
inline Point operator+(Point a, Point b)
{
	return Point(a.x + b.x, a.y + b.y);
}
inline Point operator*(Point a, double b)
{
	return Point(a.x * b, a.y * b);
}
inline double Scal(Point a, Point b)
{
	return a.x * b.x + a.y * b.y;
}
inline double Dist(Point a)
{
	return sqrt(Scal(a, a));
}
inline Point Normal(Point a)
{
	return Point(-a.y, a.x);
}


Point P[44];
double R[44];
int N;

lint Mask(Point O, double r)
{
	lint ret = 0;
	for(int i = 0; i < N; ++i)
	{
		double s = Dist(O - P[i]) + R[i];
		if(le(s, r))
			ret += 1LL << i;
	}
	return ret;
}

bool Solve(int test)
{
	scanf("%d", &N);
	double lo = 0.0, hi = 100000;
	for(int i = 0; i < N; ++i)
	{
		scanf("%lf %lf %lf", &P[i].x, &P[i].y, R + i);
		lo = max(lo, R[i]);
	}
	if(N == 1)
	{
		printf("Case #%d: %.7lf\n", test, R[0]);
		return true;
	}
	vector<lint> v;
	while(hi - lo > eps)
	{
		double r = 0.5 * (lo + hi);
		v.clear();
		for(int i = 0; i < N; ++i)
			v.pb(1LL << i);
		for(int i = 0; i < N; ++i)
			for(int j = i + 1; j < N; ++j)
			{
				double a = r - R[i];
				double b = r - R[j];
				double l = Dist(P[i] - P[j]);
				if(gt(l, a + b))
					continue;
				double x = 0.5 * (l * l + a * a - b * b) / l;
				double h = sqrt(a * a - x * x);
				Point q = P[i] + (P[j] - P[i]) * (x / l);
				Point n = Normal(P[j] - P[i]);
				Point p1 = q + n * (h / l);
				Point p2 = q - n * (h / l);
				v.pb(Mask(p1, r));
				v.pb(Mask(p2, r));
			}
		bool ok = false;
		for(int i = 0; !ok && i < sz(v); ++i)
			for(int j = 0; !ok && j < sz(v); ++j)
				if((v[i] | v[j]) == (1LL << N) - 1)
					ok = true;
		if(ok)
			hi = r;
		else
			lo = r;
	}
	printf("Case #%d: %.7lf\n", test, hi);
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//*/while(Solve(++t));
	return 0;
}