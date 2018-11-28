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

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

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

int qq;
int a[2024000];
VI b[2024000];
bool u[2024000];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	For(i, 1, 2000000)
	{
		int l = 1;
		int p10 = 1;
		while (p10 * 10 <= i) p10 *= 10, l++;
		int x = i;
		VI z;
		int mi = i;
		bool bb = true;
		forn(j, l)
		{
			if (bb && x <= 2000000)
			{
				mi = min(mi, x);
				z.pb(x);
			}
			int c = x % 10;
			bb = c;
			x = c * p10 + x / 10;
		}
		sort(z.begin(), z.end());
		z.erase(unique(z.begin(), z.end()), z.end());
		b[mi] = z;
		forn(j, z.sz)
		{
			a[z[j]] = mi;
		}
	}

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);

		clr(u);
		int l, r;
		scanf("%d%d", &l, &r);
		i64 ans = 0;
		For(i, l, r)
		{
			int t = a[i];
			if (u[t]) continue;
			u[t] = true;
			int cnt = 0;

			VI &z = b[t];
			forn(k, z.sz)
			{
				if (z[k] >= l && z[k] <= r) cnt++;
			}

			ans += cnt * (i64)(cnt - 1) / 2;
		}
		cout << ans << endl;
		
		fflush(stdout);
	}

	return 0;
}
