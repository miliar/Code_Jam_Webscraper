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

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
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
	int i, j, x, d;
	rec () {i = j = x = d;}
	rec (int i1, int j1, int x1, int d1)
	{
		i = i1;
		j = j1;
		x = x1;
		d = d1;
	}
};

bool operator < (rec p1, rec p2)
{
	if (p1.i != p2.i)
		return p1.i < p2.i;
	else
	if (p1.j != p2.j)
		return p1.j < p2.j;
	else
	if (p1.x != p2.x)
		return p1.x < p2.x;
	else
		return p1.d < p2.d;
}

int dp0;
int n, m;
char a[30][30];
string res;
string st;
map <rec, string> S;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

string go (int i, int j, int x, int dp)
{
	if (abs (x) > 200 || dp < 0)
		return "z";
	rec T = rec (i, j, x, dp);
	if (S.count (T))
		return S[T];
	string res = "z";
	if (x == 0 && !(dp & 1))
	{
		return S[T] = "";
	}
	st += a[i][j];
	forn (ii, 4)
	{
		int vx = i + dx[ii];
		int vy = j + dy[ii];
		if (vx < 0 || vx >= n || vy < 0 || vy >= n)
			continue;
		int nx = x;
		if (isdigit (a[vx][vy]))
		{
			if (st == "" || st[last(st)] == '+')
				nx -= a[vx][vy] - '0';
			else
				nx += a[vx][vy] - '0';		
		}
		if (go (vx, vy, nx, dp-1) != "z")
			if (res > a[vx][vy] + go (vx, vy, nx, dp-1))	
				res = a[vx][vy] + go (vx, vy, nx, dp-1);
	}
	st.erase (last(st));
	return S[T] = res;
}
                                
int main ()
{
	int tt;
	scanf ("%d", &tt);
	forn (ii, tt)
	{
		printf ("Case #%d:\n", ii+1);
		scanf ("%d%d", &n, &m);
		forn (i, n)
			scanf (" %s", a[i]);
		forn (i, m)
		{
			int x;
			scanf ("%d", &x);
			st = "";
			res = "z";
			S.clear ();
			
			for (dp0 = 0;; dp0 +=2)
			{
				forn (i, n)
					forn (j, n)
					        if (isdigit (a[i][j]))
					        	if (go (i, j, x - (a[i][j] - '0'), dp0) != "z")
								res = min (res, a[i][j] + go (i, j, x - (a[i][j] - '0'), dp0));
				if (res[last (res)] != 'z')
					break;
			}
			cerr << ii << " " << res << endl;
			cout << res << endl;
		}
	}
	return 0;
}
