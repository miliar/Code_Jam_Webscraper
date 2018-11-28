#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>

const long double eps = 1e-9;

using namespace std;
const long double Pi = 3.1415926535897932384626433832795;


long double Rfly, R, r, l, gap;

void Load()
{
	cin >> Rfly >> R >> r >> l >> gap;
	r = R - r;
	l = 2 * l;
}



long double CountSq(long double x1, long double x2, long double y1, long double y2, long double r)
{
	long double res = 0;
	long double p1, p2;
	long double ang;
	if (sqrt(x2 * x2 + y2 * y2) < r + eps) return (x2 - x1) * (y2 - y1);
	if (sqrt(x1 * x1 + y1 * y1) > r - eps) return 0;
	if (sqrt(x1 * x1 + y2 * y2) < r + eps && sqrt(x2 * x2 + y1 * y1) < r + eps) {
		p1 = sqrt(r * r - y2 * y2);
		p2 = sqrt(r * r - x2 * x2);
		res = (p1 - x1)	* (y2 - y1) + (p2 - y1) * (x2 - x1) - (p1 - x1) * (p2 - y1);
		res += (x2 - p1) * (y2 - p2) / 2.0;
		ang = atan2(y2, p1) - atan2(p2, x2);
		res += fabs(ang * r * r) / 2.0 - fabs(p1 * p2 - x2 * y2) / 2.0;
	} else 	if (sqrt(x1 * x1 + y2 * y2) > r - eps && sqrt(x2 * x2 + y1 * y1) > r - eps) {
		p1 = sqrt(r * r - y1 * y1);
		p2 = sqrt(r * r - x1 * x1);
		res += (x1 - p1) * (y1 - p2) / 2.0;
		ang = atan2(y1, p1) - atan2(p2, x1);
		res += fabs(ang * r * r) / 2.0 - fabs(p1 * p2 - x1 * y1) / 2.0;
	} else {
		if (sqrt(y1 * y1 + x2 * x2) > r - eps) {
			return CountSq(y1,y2,x1,x2,r);
		}
			p1 = sqrt(r * r - x1 * x1);
			p2 = sqrt(r * r - x2 * x2);
			res = (x2 - x1) * (p1 - y1 + p2 - y1) / 2.0;
			ang = atan2(p1, x1) - atan2(p2, x2);
			res += fabs(ang * r * r) / 2.0 - fabs(p1 * x2 - x1 * p2) / 2.0;
	}
//	cerr << x1 << " " << y1 << " " << x2 << " " << y2 << " " << r << "\n";
//	cerr << res << "\n";
	return res;
}

void Solve()
{
	long double Allsq, sq, tsq;
	l += 2 * Rfly; gap -= 2 * Rfly;
	r -= Rfly;
	Allsq = Pi * R * R / 4;

	sq = 0;
	long double x, y;
	long double a, b, c, ang;
	long double xx, yy, aa, bb;
	int jj;
	int j;
	if (gap < eps || l / 2 > r - eps) {
		sq = 1;            
	} else {
		x = l / 2;
		y = l / 2 + gap;
		j = 0;
		sq = 0;
		while (x < r - eps) {
			if (y > r - eps) y = r;
			j++;
			xx = l / 2;
			yy = xx + gap;
			jj = 0;
			while (xx < r - eps) {
				if (yy > r - eps) yy = r;
				jj++;           
//				cerr << j << " " << jj << " " << xx << " " << yy << " " << r << "\n";
				sq += CountSq(x, y, xx, yy, r);
				xx = yy + l;
				yy = xx + gap;
			}
			x = y + l;
			y = x + gap;
		}
		sq = 1 - sq / Allsq;
	}
	if (sq > 1 - eps) sq = 1;
	if (sq < 0 + eps) sq = 0;
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(8);
	cout << sq << "\n";
}

void Save()
{
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		printf("Case #%d: ", tt);
		Load();
		Solve();
		Save();
	}
	return 0;
}