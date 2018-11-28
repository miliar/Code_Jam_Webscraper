#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

long double sqr (long double x)
{
	return x*x;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;

	REP (T, tt)
	{
		long double x=0, y=0, z=0, vx=0, vy=0, vz=0;

		int n;

		cin >> n;

		long double a;

		REP (i, n)
		{
			cin >> a;
			x+=a;
			cin >> a;
			y+=a;
			cin >> a;
			z+=a;
			cin >> a;
			vx += a;
			cin >> a;
			vy += a;
			cin >> a;
			vz += a;
		}

		x /= n;
		y /= n;
		z /= n;

		vx /= n;
		vy /= n;
		vz /= n;

		//cout << x << " " << y << " " << z << " " << vx << " " << vy << " " << vz << endl;

		long double A, B, C;

		A = vx*vx + vy * vy + vz*vz;
		B = 2*vx*x + 2*vy*y + 2*vz*z;
		C = x*x + y*y + z*z;

		long double t = 0;

		if (A==0)
		{
			if (B!=0)
				t = max ((long double)0.0, -C/B);
		}
		else
		{
			t = max ((long double)0.0, -B/2/A);
		}

		long double d = sqrtl (sqr(x+vx*t) + sqr(y+vy*t) + sqr(z+vz*t));

		printf ("Case #%d: %.8lf %.8lf\n", T+1, (double)d, (double)t);
	}

	return 0;
}
