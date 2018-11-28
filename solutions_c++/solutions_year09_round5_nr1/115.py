#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

struct rec
{
	vector <pii> a;
	int tp;
};

bool operator < (rec p1, rec p2)
{
	if (p1.a != p2.a)
		return p1.a < p2.a;
	else
		return p1.tp < p1.tp;
}

map <rec, int> d;
bool g[12][12];
bool u[5];
const int dx[4] = {0, 0, 1, -1};
const int dy[4] = {-1, 1, 0, 0};
rec q[1000000];
int n, m;
map < vector<pii> , int> checkmap;

void gop (int v, rec &p)
{
	if (u[v])
		return;
	u[v] = 1;
	forn (i, p.a.size())
		if (abs (p.a[v].x - p.a[i].x) + abs (p.a[v].y - p.a[i].y) <= 1)
			gop (i, p);
}

int check (rec p)
{
	int x = 0;
	int y = 0;
	forn (i, p.a.size())
	{
		x = max (x, p.a[i].x);
		y = max (y, p.a[i].y);
	}
	forn (i, p.a.size())
	{
		p.a[i].x -= x;
		p.a[i].y -= y;
	}
	if (checkmap.count (p.a))
		return checkmap[p.a];
	seta (u, 0);
	int tmp = 0;
	gop (0, p);
	forn (i, p.a.size())
		if (!u[i])
			return checkmap[p.a] = 0;
	return checkmap[p.a] = 1;
}

bool check_inside (pii &p)
{
	if (p.x < 0 || p.x >= n || p.y < 0 || p.y >= m)
		return 0;
	return g[p.x][p.y];
}

int main ()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	int tt;
	scanf ("%d", &tt);
	checkmap.clear ();
	forn (ii, tt)
	{
		printf ("Case #%d: ", ii+1);
		scanf ("%d%d", &n, &m);
		seta (g, 0);
		rec st;
		rec fn;
		st.a.clear ();
		fn.a.clear ();
		forn (i, n)
			forn (j, m)
			{
				char ch;
				scanf (" %c", &ch);
				if (ch != '#')
					g[i][j] = 1;
				else
					g[i][j] = 0;
				if (ch == 'x' || ch == 'w')
					fn.a.pb (mp (i, j));
				if (ch == 'o' || ch == 'w')
					st.a.pb (mp (i, j));
			}
		sort (all (fn.a));
		sort (all (st.a));
		fn.tp = check (fn);
		st.tp = check (st);
		d.clear ();
		d[st] = 0;
		int h = 0;
		int t = 0;
		q[h] = st;
		while (h <= t)
		{
			rec v = q[h++];
			forn (i, v.a.size())
			{
				forn (j, 4)
				{
					rec w = v;
					w.a[i].x += dx[j];
					w.a[i].y += dy[j];
					pii p = mp (v.a[i].x - dx[j], v.a[i].y - dy[j]);
					if (!check_inside (w.a[i]) || !check_inside (p))
						continue;
					bool ok = 1;
					forn (k, w.a.size())
						if ((k != i && w.a[k] == w.a[i]) || (w.a[k] == p))
						{
							ok = 0;
							break;
						}
					if (!ok)
						continue;
					w.tp = check (w);
					if (w.tp == -1)
						continue;
					if (v.tp || w.tp)
					{
						sort (all (w.a));
						w.tp = check (w);
						if (!d.count (w))
						{
							d[w] = d[v] + 1;
							t ++;
							q[t] = w;
						}
					}
				}
			}
		}
		if (!d.count (fn))
			d[fn] = -1;
		printf ("%d\n", d[fn]);
	}
	return 0;
}
