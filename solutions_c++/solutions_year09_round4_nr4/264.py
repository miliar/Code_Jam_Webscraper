#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>


using namespace std;
const long double eps = 1e-9;
const long double eps2 = 1e-6;
const long double Pi = 3.1415926535897932384626433832795;



int n;

class Point{
public:
	long double x, y;
};

Point pc[44];
int rr[44];
void Load()
{
	cin >> n;
	int i;
	for (i = 1; i <= n; i++) {
		cin >> pc[i].x >> pc[i].y >> rr[i];
	}
}



long double R;



Point GetCircle(int i, int j)
{
	long double r1, r2;
	Point res;
	if (i == j) {
		res.x = pc[i].x;		
		res.y = pc[i].y;
		return res;
	}
	r1 = R - rr[i];
	r2 = R - rr[j];
//	cerr << i << " " << j << " p1: " << pc[i].x << " " << pc[i].y << " " << r1 << " p2: " << pc[j].x << " " << pc[j].y << " " << r2 << "\n";
	long double a1, b1, c1;
	long double a2, b2, c2;
	a1 = 2 * (pc[j].x - pc[i].x);
	b1 = 2 * (pc[j].y - pc[i].y);
	c1 = r2 * r2 - pc[j].x * pc[j].x - pc[j].y * pc[j].y - r1 * r1 + pc[i].x * pc[i].x + pc[i].y * pc[i].y;
	a2 = pc[i].y - pc[j].y;
	b2 = pc[j].x - pc[i].x;
	c2 = - pc[i].x * a2 - pc[i].y * b2;
	c1 = -c1;c2 = -c2;
	long double d;
	d = a1 * b2 - a2 * b1;
	res.x = c1 * b2 - c2 * b1;
	res.y = a1 * c2 - a2 * c1;
	res.x /= d;
	res.y /= d;
	long double vx, vy;
	vx = a2;
	vy = b2;
	d = sqrt(vx * vx + vy * vy);
	vx /= d; vy /= d;
	d = sqrt((pc[i].x - res.x) * (pc[i].x - res.x) + (pc[i].y - res.y) * (pc[i].y - res.y));
	if (d > r1 + eps) return res;
	d = sqrt(r1 * r1 - d * d);
	res.x += vx * d;
	res.y += vy * d;
	return res;

}

bool Can(int i1, int i2, int j1, int j2)
{
	Point c1, c2;
	c1 = GetCircle(i1, i2);
	c2 = GetCircle(j1, j2);
//	cerr << i1 << " " << i2 << " " << j1 << " " << j2 << " : R = " << R << " " << c1.x << " " << c1.y << " " << c2.x << " " << c2.y << "\n"; 
	int i;
	long double d1, d2;
	for (i = 1; i <= n; i++) {
		d1 = sqrt((pc[i].x - c1.x) * (pc[i].x - c1.x) + (pc[i].y - c1.y) * (pc[i].y - c1.y)) + rr[i];
		d2 = sqrt((pc[i].x - c2.x) * (pc[i].x - c2.x) + (pc[i].y - c2.y) * (pc[i].y - c2.y)) + rr[i];
		if (d1 > R + eps && d2 > R + eps) return false;
	}
	return true;

}



void Solve()
{
	int i1, i2, j1, j2;
	long double l, r;
	l = 0;
	for (int i = 1; i <= n; i++) {
		if (l < rr[i] - eps) l = rr[i];
	}
	r = 20000;
	while(l < r - eps2) {
		long double t = (r + l) / 2.0;
		R = t;
		bool can = false;
		for (i1 = 1; i1 <= n; i1++) {
			for (i2 = 1; i2 <= n; i2++) {
				for (j1 = 1; j1 <= n; j1++) {
					for (j2 = 1; j2 <= n; j2++) {
						if (Can(i1, i2, j1, j2)) {
							can = true;
							goto mark;
						}			
					}
				}
			}
		}
mark:
		if (can) r = t;
		else l = t;
	}	
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(11);
	cout << r << "\n";
}



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t, nt;
	cin >> nt;
	for (t = 1; t <= nt; t++) {
		Load();
		cout << "Case #" << t << ": ";
		Solve();
	}
	return 0;
}