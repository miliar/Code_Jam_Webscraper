#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pf push_front
#define mp make_pair
#define popf pop_front
#define popb pop_back
#define sz size()
#define fst first
#define snd second
#define It(x) x::iterator
#define CIt(x) x::const_iterator
#define For(i, st, en) for(int i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

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

int x[10],y[10],r[10];
int t,n;

ld dist(int xc, int yc)
{
	return sqrt(sqr((x[xc]-x[yc])*1.0)+sqr((y[xc]-y[yc])*1.0));
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("d.in", "rt", stdin);
    freopen("d.out", "wt", stdout);
#endif 

	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &t);

	for (int o=0;o<t;o++)
	{
		scanf("%d", &n);

		for (int i=0;i<n;i++)
		{
			cin >> x[i] >> y[i] >> r[i];

		}

		ld ans=1000000000;

		if (n==1)
		{
			ans=r[0];
		} else
		if (n==2)
		{
			ans=max(r[0], r[1]);
		} else
		if (n==3)
		{
			ld r1=(dist(0, 1) + r[0] + r[1])/2.0;
			ld r2=(dist(0, 2) + r[0] + r[2])/2.0;
			ld r3=(dist(1, 2) + r[1] + r[2])/2.0;

			ld a1=max((ld)r[2]*1.0, r1);
			ld a2=max((ld)r[1]*1.0, r2);
			ld a3=max((ld)r[0]*1.0, r3);

			ans=min(a1, min(a2, a3));
		}

		printf("Case #%d: %0.6lf\n", o+1, double(ans));
	}
	

	return 0;
}
