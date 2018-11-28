#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


typedef long long int64;
//typedef double old_double;
//#define double long double
const int INF = (int) 1E9;
const int64 INF64 = (int64) 1E18;
const double EPS = 1E-9;
const double PI = acos((double)0) * 2;

#define forn(i,n)  for (int i=0; i<int(n); ++i)
#define ford(i,n)  for (int i=int(n)-1; i>=0; --i)
#define fore(i,l,n)  for (int i=int(l); i<int(n); ++i)
#define all(a)  a.begin(), a.end()
#define pb  push_back
#define mp  make_pair
#define fs  first
#define sc  second


double x, s, r, t;
int n, comp;

struct item {
	double l, r, s;

	bool operator< (item it) const {
		if (comp == 0)
			return s < it.s - EPS;
		if (comp == 1)
			return s > it.s + EPS;
		throw;
	}
};

item a[1100];


void read() {
	cin >> x >> s >> r >> t >> n;
	forn(i,n)
		cin >> a[i].l >> a[i].r >> a[i].s;
}


void solve() {
	double more = x;
	forn(i,n)
		more -= a[i].r - a[i].l;
	if (more > EPS) {
		a[n].l = 0;
		a[n].r = more;
		a[n].s = 0;
		++n;
	}

	double gans = 1E20;

	forn(iter,2) {
		comp = iter;
	
		sort (a, a+n);

		int p[1100];
		forn(i,n)
			p[i] = i;
		item aa[1100];
		forn(i,n)
			aa[i] = a[i];
		double tt = t;
		do {
			t = tt;
			forn(i,n)
				a[i] = aa[p[i]];

			double ans = 0;
			forn(i,n) {
				//if (t < EPS)  break;

				double ct = t;
				double dst = t * (r + a[i].s);

				if (dst > a[i].r - a[i].l) {
					dst = a[i].r - a[i].l;
					ct = dst / (r + a[i].s);
					if (ct > t + EPS)  throw;
				}

				ans += ct;
				t -= ct;

				double left = a[i].r - a[i].l - dst;
				double t2 = left / (s + a[i].s);
				ans += t2;
			}

			gans = min (gans, ans);

			break;
		}
		while (next_permutation (p, p+n));

	}

	printf ("%.20lf\n", gans);
	//cerr << gans << endl;
}


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	forn(tt,ts) {
		read();
		printf ("Case #%d: ", tt+1);
		solve();
	}

}