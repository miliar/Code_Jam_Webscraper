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
int n, m;
int a[128][2];
int d[128][128][128];
int q[1024000][3];
int qb, qe;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		scanf("%d", &n);
		m = 100;
		forn(i, n)
		{
			int x;
			char cc;
			scanf(" %c%d", &cc, &x);
			a[i][0] = cc == 'O';
			a[i][1] = x-1;
		}
		memset(d, 0x3f, sizeof(d));
		d[0][0][0] = 0;
		qb = qe = 0;
		q[qe][0] = 0;
		q[qe][1] = 0;
		q[qe][2] = 0;
		qe++;
		while (qb != qe)
		{
			int p = q[qb][0];
			int x = q[qb][1];
			int y = q[qb][2];
			qb++;
			For(dx, -1, 1)
			{
				For(dy, -1, 1)
				{
					int xn = x + dx;
					int yn = y + dy;
					if (xn < 0 || xn >= m || yn < 0 || yn >= m) continue;
					forn(rx, 2)
					{
						forn(ry, 2)
						{
							if (rx && dx) continue;
							if (ry && dy) continue;
							if (rx && ry) continue;
							if ((rx || ry) && p == n) continue;
							if (rx && (a[p][0] != 0 || a[p][1] != x)) continue;
							if (ry && (a[p][0] != 1 || a[p][1] != y)) continue;
							int pn = p;
							if (rx || ry) pn++;
							if (d[pn][xn][yn] > d[p][x][y] + 1)
							{
								d[pn][xn][yn] = d[p][x][y] + 1;
								q[qe][0] = pn;
								q[qe][1] = xn;
								q[qe][2] = yn;
								qe++;
							}
						}
					}
				}
			}
		}
		
		int ans = 0x3f3f3f3f;
		forn(i, m)
		{
			forn(j, m)
			{
				ans = min(ans, d[n][i][j]);
			}
		}
		printf("%d\n", ans);
	}

	return 0;
}
