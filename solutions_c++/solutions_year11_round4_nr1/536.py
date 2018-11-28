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

int n, s, r, l, t;
int qq;
int a[1024][10];
int b[1024][2];
int ind[1024];

bool cmp(int p1, int p2)
{
	return b[p1][1] < b[p2][1];
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);

		scanf("%d", &l);
		scanf("%d%d", &s, &r);
		scanf("%d", &t);
		scanf("%d", &n);
		int l1 = l;
		int k = 0;
		forn(i, n)
		{
			forn(j, 3)
			{
				scanf("%d", &a[i][j]);
			}
			l1 -= a[i][1] - a[i][0];
		}
		b[k][0] = l1;
		b[k][1] = 0;
		k++;
		forn(i, n)
		{
			b[k][0] = a[i][1] - a[i][0];
			b[k][1] = a[i][2];
			k++;
		}
		forn(i, k)
		{
			ind[i] = i;
		}
		sort(ind, ind+k, cmp);

		ld ans = 0.0;
		ld x = t;
		forn(i1, k)
		{
			int i = ind[i1];
			if (x > 0)
			{
				ld tt = b[i][0] * 1.0 / (r + b[i][1]);
				if (tt <= x)
				{
					x -= tt;
					ans += tt;
				}
				else
				{
					ans += x;
					ld len = b[i][0] - (r + b[i][1]) * x;
					x = 0;
					tt = len * 1.0 / (s + b[i][1]);
					ans += tt;
				}
			}
			else
			{
				ld tt = b[i][0] * 1.0 / (s + b[i][1]);
				ans += tt;
			}
		}

		printf("%0.10lf\n", (double)ans);
		
		fflush(stdout);
	}

	return 0;
}
