#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
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
#define x first
#define y second
#define It(x) x::iterator
#define CIt(x) x::const_iterator
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

int T;
int n, s, p;
int a[128];
int surp[128];
int unsurp[128];

int main()
{
#ifdef HOME
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >> T;
	for(int t = 0;t<T;t++)
	{
		cin >> n >> s >> p;
		clr(surp);
		clr(unsurp);
		for(int i=0;i<n;i++)
		{
			cin >> a[i];
			int x = a[i] / 3;
			int y = a[i] % 3;
			if (y == 1)
			{
				if (x == 0) surp[i] = -1; else surp[i] = x + 1;
				unsurp[i] = x + 1;
			}
			if (y == 2)
			{
				if (x == 9) surp[i] = -1; else surp[i] = x + 2;
				unsurp[i] = x + 1;
			}
			if (y == 0)
			{
				surp[i] = x;
				if (x != 0) surp[i]++; 
				if (x == 10) surp[i] = -1;
				unsurp[i] = x;
			}
		}

		int ans = 0;
		for(int i=0;i<n;i++)
		{
			if (unsurp[i] < p && surp[i] >= p && s > 0)
			{
				ans++;
				s--;
			}
		}
		for(int i=0;i<n;i++)
		{
			if (unsurp[i] >= p) ans++;
		}

		printf("Case #%d: %d\n", t+1, ans);

	}


	return 0;
}
