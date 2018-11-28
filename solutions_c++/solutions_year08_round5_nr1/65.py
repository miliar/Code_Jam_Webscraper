#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

string s;

#define x first
#define y second

const int XMAX = 6100;

vector< pair<int, int> > p;
int cx, cy, vx, vy;
int minx[XMAX], miny[XMAX];
int maxx[XMAX], maxy[XMAX];

int ans;

void outdata() {
	cout << ans << endl;
}

void solve() {
	p.clear();
	cx = cy = 3010;
	vx = 0;
	vy = 1;
	p.pb( mp(cx, cy) );
	int gminx = 3010, gminy = 3010;
	int gmaxx = 3010, gmaxy = 3010;
	forn(i, XMAX) {
		minx[i] = miny[i] = 10000000;
		maxx[i] = maxy[i] = -10000000;
	}
	fors(i, s) {
		if (s[i] == 'L') {
			int tx = -vy, ty = vx;
			vx = tx, vy = ty;
		}
		if (s[i] == 'R') {
			int tx = vy, ty = -vx;
			vx = tx, vy = ty;
		}
		if (s[i] == 'F') {
			int nx = cx, ny = cy;
			nx += vx;
			ny += vy;
			if (cx == nx) {
				int my = min(cy, ny);
				minx[my] = min(minx[my], cx);
				maxx[my] = max(maxx[my], cx);
			} else {
				int mx = min(cx, nx);
				miny[mx] = min(miny[mx], cy);
				maxy[mx] = max(maxy[mx], cy);
			}
			cx = nx;
			cy = ny;
			gminx = min(gminx, cx);
			gminy = min(gminy, cy);
			gmaxx = max(gmaxx, cx);
			gmaxy = max(gmaxy, cy);
			p.pb( mp(cx, cy) );
		}
	}
	assert(cx == 3010 && cy == 3010);
//	forv(i, p) cerr << p[i].x << " " << p[i].y << endl;
	int sq = 0;
	forn(i, (int)p.size() - 1) {
    	sq += (p[i].x - p[i + 1].x) * (p[i].y + p[i + 1].y);
	}
	sq = abs(sq);
    assert(sq % 2 == 0);
    sq /= 2;
//    cerr << "sq = " << sq << endl;
    ans = 0;
//    cerr << gminx << " - " << gmaxx << endl;
//    cerr << gminy << " - " << gmaxy << endl;
    for(int x = gminx; x < gmaxx; ++x) {
	    for(int y = gminy; y < gmaxy; ++y) {
	    	if ((miny[x] <= y && y + 1 <= maxy[x]) ||
	    		(minx[y] <= x && x + 1 <= maxx[y])) {
//	    			cerr << "----=== " << x - 3010 << " " << y - 3010 << endl;
	    			++ans;
				}
	    }
    }
//    cerr << "ans prev = " << ans << endl;
    assert(ans >= sq);
    ans -= sq;
}

void readdata() {
	s.clear();
	int l;
	cin >> l;
	forn(i, l) {
		string c;
		int rep;
		cin >> c;
		cin >> rep;
		forn(t, rep) {
			s += c;
		}
	}
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		cerr << i + 1 << endl;
		readdata();
		solve();
		outdata();
	}
	return 0;
}
