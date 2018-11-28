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

struct tpoint
{
	ld x,y,r;
};

tpoint a[5];
int n,t;

int main()
{
#ifdef HOME
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d",&t);
	forn(tt,t)
	{
		printf("Case #%d: ",tt+1);
		scanf("%d",&n);
		forn(i,n)
		{
			int x,y,r;
			scanf("%d%d%d",&x,&y,&r);
			a[i].x=x;
			a[i].y=y;
			a[i].r=r;
		}
		n++;
		a[n-1]=a[0];
		n++;
		a[n-1]=a[1];

		ld mm=100000.0;
		forn(i,n-2)
		{
			mm=min(mm,max((sqrt(sqr(a[i].x-a[i+1].x)+sqr(a[i].y-a[i+1].y))+a[i].r+a[i+1].r)/2,a[i+2].r));
		}
		if (n==4) mm=max(a[0].r,a[1].r);
		cout << mm << endl;
	}

	return 0;
}
