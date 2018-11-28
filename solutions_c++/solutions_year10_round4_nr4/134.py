#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cassert>
#include <ctime>
#include <map>
#include <set>
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(s) (int)(s).size()
#define mpmake_pair

using namespace std;

typedef long long li;
typedef pair<double, double> pt;
pt a[3], b[20];
int t, n, m;
double dist(pt a, pt b){
	return sqrt((a.X - b.X) * (a.X - b.X) + (a.Y - b.Y) * (a.Y - b.Y));
}
double Sec(double r, double angle){
	return (r * r * angle) / 2.0;
}
double S(double a, double b, double angle){
	return (0.5 * a * b * sin(angle));
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> t;
	forn(q, t){
		cin >> n >> m;
		double ans = 1e9, a1 = -1, a2 = -1;
		forn(i, n)
			cin >> a[i].X >> a[i].Y;
		forn(i, m)
			cin >> b[i].X >> b[i].Y;
		cout << "Case #" << q + 1 <<":";
		forn(i, m){
			double A;
			if(dist(a[0], a[1]) < dist(b[i], a[0]) + dist(b[i], a[1])){
				pt t1, t2;
				pt v(a[1].X - a[0].X, a[1].Y - a[0].Y);
				double r1 = dist(a[0], b[i]), r2 = dist(a[1], b[i]), d = dist(a[0], a[1]);
				double angle1 = 2 * acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d));
				double angle2 = 2 * acos((r2 * r2 + d * d - r1 * r1) / (2 * r2 * d));
				double S1 = S(r1, r1, angle1), S2 = S(r2, r2, angle2), Se1 = Sec(r1, angle1), Se2 = Sec(r2, angle2);
				A = Sec(r1, angle1) + Sec(r2, angle2) - S(r1, r1, angle1) - S(r2, r2, angle2);
			}
			else
				A = 0;
			cout.precision(6);
			cout << " " << fixed << A;
		}
		cout << endl;
		
	}
	return 0;
}