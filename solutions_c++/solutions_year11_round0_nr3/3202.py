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
template <class _T> inline _T sgn(const _T& x) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }
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



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int testsCount;
	scanf("%d", &testsCount);
	forn(testNumber, testsCount)
	{
		int n;
		int a[16];
		
		scanf("%d", &n);
		forn(i, n)
		{
			scanf("%d", &a[i]);
		}
		
		int ans = -1;
		For(mask, 1, (1 << n) - 2)
		{
			int s1[2] = {0, 0};
			int s2[2] = {0, 0};
			forn(i, n)
			{
				s1[(mask >> i) & 1] += a[i];
				s2[(mask >> i) & 1] ^= a[i];
			}
			if (s2[0] == s2[1])
			{
				ans = max(ans, max(s1[0], s1[1]));
			}
		}
		
		printf("Case #%d: ", testNumber + 1);
		if (ans == -1)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", ans);
		}
	}

	return 0;
}
