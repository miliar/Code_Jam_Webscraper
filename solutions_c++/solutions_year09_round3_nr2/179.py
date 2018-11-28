#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <iomanip>
#include <utility>

#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define tr(T, i) for (typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))
#define pb push_back

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;

int cmp(double x, double y = 0, double tol = EPS)
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

int main()
{
	int T, C;
	cin >> T;
	
	cout.precision(8);
	cout << fixed;
	for( C = 1; C <= T; C++ ) {
		int n;
		cin >> n;

	//	cout << "Case " << C << " start" << endl;

		double invn = 1.0 / n;
		double x, y, z;
		double vx, vy, vz;
		x = y = z = vx = vy = vz = 0;
		for(int i = 0; i < n; i++) {
			long long int tx, ty, tz, tvx, tvy, tvz;
			cin >> tx >> ty >> tz >> tvx >> tvy >> tvz;
			x += tx * invn; vx += tvx * invn;
			y += ty * invn; vy += tvy * invn;
			z += tz * invn; vz += tvz * invn;
		}
	//	cout << x << " " << y << " " << z << endl;
	//	cout << vx << " " << vy << " " << vz << endl;

		double b = (2.0 * x * vx + 2.0 * y * vy + 2.0 * z * vz);
		double a = (vx*vx + vy*vy + vz*vz);

		double tmin;
		if( a > EPS )
			tmin = -b / (2*a);
		else
			tmin = 0;

		double dmin = 0;
		if( tmin < 0 ) tmin = 0;

		double mx, my, mz;
		mx = (x + tmin*vx);
		my = (y + tmin*vy);
		mz = (z + tmin*vz);
		dmin = sqrt( mx*mx + my*my + mz*mz );

		cout << "Case #" << C << ": " << dmin << " " << tmin << endl;
	}

    return 0;
}
