#include <algorithm>
#include <climits>
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
#include <stack>
#include <vector>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define sz size()
#define It(x) x::iterator
#define clr(x) memset((x), 0, sizeof(x))
#define For(i, l, r) for (int i = int(l); i <= int(r); i++)
#define Ford(i, l, r) for (int i = int(l); i >= int(r); i--)
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = (int(n) - 1); i >= 0; i--)
#define fori(t, i, x) for (t i = x.begin(); i != x.end(); i++)

typedef long double ld;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef pair < int, int > PII;
typedef map < string, int > MSI;

const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

template <class T> inline T sqr(const T& x) { return x * x; }
template <class T> string toStr(T x) { ostringstream os(""); os << x; return os.str(); }

#define MAXN 128
#define MAX_BASINS 32

const int DIR[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int n, m;
int a[MAXN][MAXN];
int p[MAXN * MAXN];
char ans[MAXN * MAXN];
char label[MAXN][MAXN];

int ind(int i, int j)
{
	return i * m + j;
}

int findSet(int x)
{
	if (p[x] != x)
	{
		p[x] = findSet(p[x]);
	}
	return p[x];
}

void join(int x, int y)
{
	if (x < y)
	{
		p[y] = x;
	}
	else
	{
		p[x] = y;
	}
}

inline void unite(int x, int y)
{
	join(findSet(x), findSet(y));
}

struct Cmp
{
	bool operator () (int x, int y)
	{
		return findSet(x) < findSet(y);
	}
};

int main()
{
	freopen("b-large.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	cout << fixed << setprecision(12);

	int tc;
	scanf("%d", &tc);
	forn(tn, tc)
	{
		scanf("%d %d", &n, &m);
		forn(i, n)
		{
			forn(j, m)
			{
				scanf("%d", &a[i][j]);
			}
		}

		forn(i, n * m)
		{
			p[i] = i;
		}
		forn(i, n)
		{
			forn(j, m)
			{
				int mv = a[i][j];
				int to = -1;
				forn(k, 4)
				{
					int ni = i + DIR[k][0];
					int nj = j + DIR[k][1];
					if (ni >= 0 && ni < n && nj >= 0 && nj < m && a[ni][nj] < mv)
					{
						mv = a[ni][nj];
						to = ind(ni, nj);
					}
				}

				if (to != -1)
				{
					unite(ind(i, j), to);
				}
			}
		}

		VI v;
		forn(i, n * m)
		{
			v.pb(findSet(i));
		}
		sort(all(v), Cmp());
		v.erase(unique(all(v)), v.end());

		forn(k, v.sz)
		{
			ans[v[k]] = char('a' + k);
		}
		forn(i, n)
		{
			forn(j, m)
			{
				
				label[i][j] = ans[findSet(ind(i, j))];
			}
		}

		printf("Case #%d:\n", tn + 1);
		forn(i, n)
		{
			forn(j, m)
			{
				putchar(label[i][j]);
				if (j < m - 1)
				{
					putchar(' ');
				}
			}
			puts("");
		}
	}

	return 0;
}
