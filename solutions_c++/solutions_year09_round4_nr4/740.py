#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const double pi = acos(-1.0);
struct circle {
	int x, y;
	double r;
	
	double area()
	{ return pi * r * r; }
} p[45];

double dist(int a, int b)
{ 
	return sqrt((p[a].x - p[b].x) * (p[a].x - p[b].x) + (p[a].y - p[b].y) * (p[a].y - p[b].y)); 
}
double getr(int a, int b)
{
	double d = dist(a, b);
	if (d > fabs(p[a].r - p[b].r))
		return (d + p[a].r + p[b].r) / 2;
	return max(p[a].r, p[b].r);
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int c, n, i;
	double a1, a2, a3;
	
	cin >> c;
	for (int id = 1; id <= c; ++id)
	{
		cin >> n;
		if (n == 1) {
			cin >> p[0].x >> p[0].y >> p[0].r;
			cout << "Case #" << id << ": " << p[0].r << endl;
		} else if (n == 2) {
			cin >> p[0].x >> p[0].y >> p[0].r;
			cin >> p[1].x >> p[1].y >> p[1].r;
			cout << "Case #" << id << ": " << max(p[0].r, p[1].r) << endl;
		} else if (n == 3) {
			for (i = 0; i < 3; ++i)
				cin >> p[i].x >> p[i].y >> p[i].r;
			a1 = max(p[0].r, getr(1, 2));
			a2 = max(p[1].r, getr(0, 2));
			a3 = max(p[2].r, getr(0, 1));
			cout << "Case #" << id << ": " << min(a1, min(a2, a3)) << endl;
		}
	}
	return 0;
}
