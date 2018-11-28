#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <sstream>
#include <cstdlib>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef  vector<int> VI;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"
const int NMAX = 216;
const int SHIFT = 105;
struct Point {
	int x, y;
};

vector<Point> p;
int n;

int intersect(double x, double y, Point p1, Point p2, int type) {
	int res = 0;
	if (type == 0) {
		if (p1.y == p2.y) return 0;
		int y1 = min(p1.y, p2.y);
		int y2 = max(p1.y, p2.y);
		res = int(y1 * 1.0 < y && y < y2 * 1.0 && p1.x * 1.0 > x);
	} else if (type == 1) {
		if (p1.x == p2.x) return 0;
		int x1 = min(p1.x, p2.x);
		int x2 = max(p1.x, p2.x);
		res = (int)(x1*1.0 < x && x < x2*1.0 && p1.y*1.0 > y);		
	} else if (type == 2) {
		if (p1.y == p2.y) return 0;
		int y1 = min(p1.y, p2.y);
		int y2 = max(p1.y, p2.y);
		res = int(y1*1.0 < y && y < y2*1.0 && p1.x*1.0 < x);
	} else {
		if (p1.x == p2.x) return 0;
		int x1 = min(p1.x, p2.x);
		int x2 = max(p1.x, p2.x);
		res = int(x1*1.0 < x && x < x2*1.0 && p1.y*1.0 < y);		
	}
	return res;
}

int inside(double x, double y, int type) {
	int cnt = 0;
	forn(i, n) {
		cnt += intersect(x, y, p[i], p[i+1], type);
	}
	return cnt;
}

int square() {
	int ret = 0;
	forn(i, NMAX) {
		forn(j, NMAX) {
			double x = i - SHIFT;
			double y = j - SHIFT;
			if (x == 2 && y == 2) {
				x += 1;
				x -= 1;
			}
			x += 0.5;
			y += 0.5;
			int i0 = inside(x, y, 0);
			int i1 = inside(x, y, 1);
			int i2 = inside(x, y, 2);
			int i3 = inside(x, y, 3);
			if (
				(i0 % 2 == 0 && i2 % 2 == 0 && i0 > 0 && i2 > 0) ||
				(i1 % 2 == 0 && i3 % 2 == 0 && i1 > 0 && i3 > 0)) {
					ret++;
				}
		}
	}
	return ret;
}
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);

	int tc; cin >> tc;
	forn(it, tc) {
		int cnt; cin >> cnt;
		p.clear();
		Point t;
		t.x = 0;
		t.y = 0;
		int dir = 0;
		p.pb(t);
		forn(i, cnt) {
			string s;
			int c;
			cin >> s >> c;
			forn(dfdf, c) {
				forv(j, s) {
					if (s[j] == 'F') {
						t.x += dx[dir];
						t.y += dy[dir];
						p.pb(t);
					} else if (s[j] == 'R') {
						dir = (dir + 3) % 4;
					} else {
						dir = (dir + 1) % 4;
					}
				}
			}
		}
		n = p.size()-1;
		printf("Case #%d: %d\n", it+1, square());
	}

	return 0;
}
