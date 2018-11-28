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
#define pb push_back
#define mp make_pair
#define sz size()
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
typedef long long i64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

#define add(a, b) do { a = (a + (b)) % 10000; } while (0)

const char *a = "welcome to code jam";

int qq, n, m;
char s[10240];
int d[512][20];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	m = strlen(a);

	gets(s);
	sscanf(s, "%d", &qq);
	forn(ii, qq)
	{
		gets(s);

		int ans = 0;
		n = strlen(s);

		clr(d);
		d[0][0] = 1;
		forn(i, n)
		{
			d[i+1][0] = 1;
			forn(j, m)
			{
				add(d[i+1][j+1], d[i][j+1]);
				if (s[i] == a[j]) add(d[i+1][j+1], d[i][j]);
			}
		}

		ans = d[n][m];

		printf("Case #%d: %04d\n", ii+1, ans);
	}

	return 0;
}
