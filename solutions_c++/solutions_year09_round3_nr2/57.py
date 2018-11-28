#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define fst first
#define snd second
#define It(x) __typeof((x).begin())
#define For(i, st, en) for(__typeof(en) i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(__typeof(n) i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

ld dist(ld x, ld y, ld z)
{
	return sqrt(x * x + y * y + z * z);
}


int main()
{
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn, n;
	cin >> tcn;
	for (int tc = 0; tc < tcn; tc++)
	{
		cin >> n;
		ld x = 0.0, y = 0.0, z = 0.0, vx = 0.0, vy = 0.0, vz = 0.0;
		for (int i = 0; i < n; ++i)
		{
			int xx, yy, zz, vxx, vyy, vzz;
			cin >> xx >> yy >> zz >> vxx >> vyy >> vzz;
			x += xx;
			y += yy;
			z += zz;
			vx += vxx;
			vy += vyy;
			vz += vzz;
		}
		x /= n;
		y /= n;
		z /= n;
		vx /= n;
		vy /= n;
		vz /= n;

		ld d = dist(x, y, z);
		ld t = 0.0;

		ld a = x * vx + y * vy + z * vz;
		ld b = vx * vx + vy * vy + vz * vz;

		if (fabs(b) > EPS)
		{
			ld tt = -a / b;
			if (tt > EPS)
			{
				t = tt;
				d = dist(x + vx * t, y + vy * t, z + vz * t);
			}
		}
	
		cout << "Case #" << tc + 1 << ": " << d << " " << t << endl;
	}


	return 0;
}
