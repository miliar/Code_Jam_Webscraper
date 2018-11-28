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


const int MAXN = 510;

int n, m, d, w[MAXN][MAXN];

void read() {
	cin >> n >> m >> d;
	forn(i,n)
		forn(j,m) {
			char c;
			scanf (" %c", &c);
			w[i][j] = c - '0';
		}
}


int sum (int x1, int y1, int x2, int y2, bool is_x, bool left) {
	int s = 0;
	fore(x,x1,x2+1)
		fore(y,y1,y2+1) {
			if (x==x1 && y==y1 && left)  continue;
			if (x==x1 && y==y2 && (is_x && left || !is_x && !left))  continue;
			if (x==x2 && y==y1 && (is_x && !left || !is_x && left))  continue;
			if (x==x2 && y==y2 && (is_x && !left || !is_x && !left))  continue;

			int cur = d + w[x][y];
			if (is_x)
				cur *= left ? (x2 - x + 1) : (x - x1 + 1);
			else
				cur *= left ? (y2 - y + 1) : (y - y1 + 1);
			if (cur < 0)  throw;
			s += cur;
		}
	return s;
}


bool check (int x1, int y1, int x2, int y2) {
	int mx1 = x1 + (x2 - x1 - 1) / 2;
	int mx2 = x2 - (x2 - x1 - 1) / 2;
	if (sum (x1, y1, mx1, y2, true, true) != sum (mx2, y1, x2, y2, true, false))
		return false;

	int my1 = y1 + (y2 - y1 - 1) / 2;
	int my2 = y2 - (y2 - y1 - 1) / 2;
	if (sum (x1, y1, x2, my1, false, true) != sum (x1, my2, x2, y2, false, false))
		return false;

	return true;
}


void solve() {
	int ans = 0;
	forn(x1,n)
		forn(y1,m)
			fore(x2,x1+2,n)
				fore(y2,y1+2,m)
					if (x2-x1 == y2-y1)
						if (check (x1, y1, x2, y2))
							ans = max (ans, x2-x1+1);

	if (ans == 0)
		puts ("IMPOSSIBLE");
	else
		printf ("%d\n", ans);
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