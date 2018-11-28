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

int qq, n, m;
char a[5200][32];
char s[102400];
bool b[16][256];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d%d%d", &n, &m, &qq);
	forn(i, m)
	{
		scanf("%s", a[i]);
	}
	forn(ii, qq)
	{
		scanf("%s", s);

		int ans = 0;
		clr(b);

		char *h = s;
		forn(i, n)
		{
			if (*h == '(')
			{
				h++;
				while (*h != ')')
				{
					b[i][(int)*h] = true;
					h++;
				}
				h++;
			}
			else
			{
				b[i][(int)*h] = true;
				h++;
			}
		}

		forn(i, m)
		{
			bool bb = true;
			forn(j, n)
			{
				if (!b[j][(int)a[i][j]])
				{
					bb = false;
					break;
				}
			}
			ans += bb;
		}

		printf("Case #%d: %d\n", ii+1, ans);
	}

	return 0;
}
