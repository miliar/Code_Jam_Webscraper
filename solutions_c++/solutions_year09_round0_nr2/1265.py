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

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int qq, n, m, k;
int a[128][128];
int h[128][128];
char ans[128][128];
int pa[26];

int go(int x, int y)
{
	if (h[x][y] != -1) return h[x][y];

	int mi = 100000;
	int j = -1;
	forn(l, 4)
	{
		int xn = x + dx[l];
		int yn = y + dy[l];

		if (xn < 0 || xn >= n || yn < 0 || yn >= m || a[xn][yn] >= a[x][y]) continue;
		if (a[xn][yn] < mi)
		{
			mi = a[xn][yn];
			j = l;
		}
	}

	if (j == -1)
	{
		h[x][y] = k++;
	}
	else
	{
		h[x][y] = go(x + dx[j], y + dy[j]);
	}
	return h[x][y];
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		scanf("%d%d", &n, &m);
		forn(i, n)
		{
			forn(j, m)
			{
				scanf("%d", &a[i][j]);
			}
		}

		k = 0;
		memset(h, 0xff, sizeof(h));
		forn(i, n)
		{
			forn(j, m)
			{
				go(i, j);
			}
		}

		k = 0;
		memset(pa, 0xff, sizeof(pa));
		forn(i, n)
		{
			forn(j, m)
			{
				if (pa[h[i][j]] == -1)
				{
					pa[h[i][j]] = k++;
				}
			}
		}

		printf("Case #%d:\n", ii+1);
		forn(i, n)
		{
			forn(j, m)
			{
				if (j) putchar(' ');
				printf("%c", 'a' + pa[h[i][j]]);
			}
			puts("");
		}
	}

	return 0;
}
