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

int64 L, K;
vector <int64> a;
int n;
int64 d[100000];
bool u[100000];
set <pair <int64, int> > D;

int gcd (int a, int b)
{
	return a ? gcd (b % a, a) : b;
}

int64 calccalc (int64 P)
{
	forn (i, P)
		d[i] = inf64;
	d[0] = 0;
	seta (u, 0);
	D.clear ();
	D.insert (mp (0, 0));
	while (!D.empty ())
	{
	        set <pair <int64, int> > :: iterator it;
	        it = D.begin();
		pair <int64, int> v = *it;
		u[v.sc] = 1;
		if (v.sc == L % P)
			return ((v.fs + L) / P); 
		D.erase (it);
		forn (i, n)
		{
			pair <int64, int> w;
			w.fs = v.fs + P - a[i];
			w.sc = (v.sc + a[i]) % P;
			if (!u[w.sc])
			{
				it = D.find (mp (d[w.sc], w.sc));
				if (it != D.end())
					D.erase (it);
				d[w.sc] = w.fs;
				D.insert (w);
			}	
		}
	}
	return -1;
}

void calc ()
{
	cin >> L >> n;
	a.resize (n);
	forn (i, n)
		cin >> a[i];
	int d = a[0];
	forn (i, n)
		d = gcd (d, a[i]);
	if (L % d != 0)
	{
		printf ("IMPOSSIBLE\n");
		return;
	}
	sort (all (a));
	reverse (all (a));
	int64 res = inf64;
	forn (i, 1)
		res = min (res, calccalc (a[i]));
	cout << res << endl;
}

int main ()
{
	int tt;
	scanf ("%d", &tt);
	forn (ii, tt)
	{
		printf ("Case #%d: ", ii+1);
		calc ();
	}
	return 0;
}
