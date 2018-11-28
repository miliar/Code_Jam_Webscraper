#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment (linker, "/STACK:200000000")
#include <algorithm>
#include <bitset>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
#include <sstream>
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
#define fs  first
#define sc  second
#define pb  push_back
#define mp  make_pair


const int MAXN = 1100;


int n, w, l;
pair<int,int> a[MAXN];


void read() {
	cin >> n >> w >> l;
	forn(i,n) {
		cin >> a[i].fs;
		a[i].sc = i;
	}
}


vector < pair<int,int> > corn;
pair<int,int> ans[MAXN];


bool can_place (int pos, int r) {
	int x1 = corn[pos].fs,  y1 = corn[pos].sc;
	int x2 = x1 + 2*r,    y2 = y1 + 2*r;
	if (x2 > w || y2 > l)
		return false;

	for (int i=pos; i<(int)corn.size()-1; ++i) {
		pair<int,int> p = corn[i];
		pair<int,int> q = corn[i+1];
		if (p.fs >= x2)
			break;
		if (p.sc == q.sc) {
			if (p.fs > x1)
				return false;
		}
		else {
			if (p.sc < q.sc && q.sc > y1)
				return false;
		}
	}
	return true;
}


void place (int pos, int r) {
	int x = corn[pos].fs,  y = corn[pos].sc;

	corn[pos].sc += 2*r;
	if (pos && corn[pos-1] == corn[pos]) {
		corn.erase (corn.begin() + pos);
		--pos;
	}

	int last = pos;
	while (last+1 < (int)corn.size() && (corn[last+1].fs < x+2*r || corn[last+1].fs == x+2*r && corn[last+1].sc <= y+2*r))
		++last;

	if (corn[last].fs == x+2*r) {
		int old_y = corn[last].sc;
		corn[last].sc = y+2*r;
		if (last+1 == (int)corn.size() || corn[last+1].fs != corn[last].fs)
			corn.insert (corn.begin() + last+1, mp (x+2*r, y));
		corn.erase (corn.begin()+pos+1, corn.begin()+last);
	}
	else {
		int nx = x+2*r;
		int ny = corn[last+1].sc;
		corn.insert (corn.begin() + last+1, mp (nx, y+2*r));
		corn.insert (corn.begin() + last+2, mp (nx, ny));
		corn.erase (corn.begin()+pos+1, corn.begin()+last+1);
	}
}


void solve() {
	bool sw = false;
	if (w > l) {
		sw = true;
		swap (w, l);
	}

	corn.clear();
	corn.pb (mp (0, l));
	corn.pb (mp (0, 0));
	corn.pb (mp (w, 0));
	corn.pb (mp (w, l));

	sort (a, a+n);
	random_shuffle (a, a+n);
	ford(i,n) {
		int r = a[i].fs,  id = a[i].sc;

		bool found = false;
		ford(j,corn.size()) {
			int x = corn[j].fs,  y = corn[j].sc;
			if (j && corn[j-1].fs == x && corn[j-1].sc > y)
				if (can_place (j, r)) {
					found = true;
					ans[id] = mp (x + r, y + r);
					place (j, r);
					break;
				}
		}

		if (!found) {
			int ly = -INF;
			forn(j,corn.size())
				if (j && j != (int)corn.size()-1)
					ly = max (ly, corn[j].sc);
			if (ly + 2*r > l)
				throw;
			ans[id] = mp (0, ly + r);

			int y = ly + 2*r;
			corn.clear();
			corn.pb (mp (0, l));
			corn.pb (mp (0, y));
			corn.pb (mp (w, y));
			corn.pb (mp (w, l));
		}
	}

	if (sw)
		forn(i,n)
			swap (ans[i].fs, ans[i].sc);

	forn(i,n)
		printf (" %d %d", ans[i].fs, ans[i].sc);
	puts("");
}


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	forn(tt,ts) {
		read();
		if (! cin)  throw;
		printf ("Case #%d:", tt+1);
		solve();
	}
}