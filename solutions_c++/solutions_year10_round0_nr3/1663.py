#include <algorithm>
#include <cassert>
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

#define bublic public
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

const int MAXN = 1024;

int n, m, k;
int a[MAXN];
int r[MAXN];
i64 c[MAXN];

int main()
{
//	freopen("c.in", "rt", stdin);
//	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("C-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int testsCount;
	scanf("%d", &testsCount);
	forn(testNumber, testsCount)
	{
		cout << "Case #" << testNumber + 1 <<": ";

		scanf("%d %d %d", &m, &k, &n);
		forn(i, n)
		{
			scanf("%d", &a[i]);
		}

		memset(r, 0xFF, sizeof(r));
		clr(c);

		int cur = 0;
		int i = 0;
		for (i = 1; i <= m && r[cur] == -1; ++i)
		{
			r[cur] = i;
			i64 e = 0;
			int prev = cur;
			while (e + a[cur] <= k)
			{
				e += a[cur];
				cur = (cur + 1) % n;
				if (cur == prev) break;
			}
			c[i] = c[i - 1] + e;
		}

		int stepsCount = i - r[cur];
		m -= r[cur] - 1;
		i64 ans = c[r[cur] - 1];
		ans += (c[i - 1] - c[r[cur] - 1]) * (m / stepsCount);
		int rem = m % stepsCount;
		ans += c[r[cur] + rem - 1] - c[r[cur] - 1];

		cout << ans << endl;
	}

	return 0;
}
