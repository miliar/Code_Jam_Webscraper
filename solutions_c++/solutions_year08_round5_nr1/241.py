#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector <ll>	vll;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef pair <double, double> dd;
typedef vector <dd> vdd;         
typedef vector <double> vd;
typedef vector <int> vi;
typedef vector <string> vs;
typedef stringstream ss;

#define sz(v)		((int)(v.size()))
#define fn(i, n)	for(int i = 0; i < (n); ++i)
#define fv(i, v)	for(int i = 0; i < sz(v); ++i)
#define set0(a)		memset(a, 0, sizeof(a))   
#define set1(a)		memset(a, 0x3f, sizeof(a))
#define INF			0x3f3f3f3f
#define INFLL		0x3f3f3f3f3f3f3f3fLL
#define pb(a)		push_back(a)
#define all(a)		a.begin(), a.end()
#define	PI			3.1415926535897932384626433832795
#define	eps			1e-9
#define	eq(a, b)	(fabs((a)-(b)) <= eps)

unsigned char world[8192][8192], line[8192][8192];

#define	NORTH	0
#define	WEST	1
#define	SOUTH	2
#define	EAST	3

int dx[] = {0, -1, 0, 1}, dy[] = {-1, 0, 1, 0};

int main() {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int n, T;
	cin >> T;
	fn(test, T) {
		int r, l, x = 4000, y = 4000, dir = NORTH;
		set0(world);
		set0(line);
		cin >> l;
		string s;
		fn(i, l) {
			cin >> s;
			cin >> r;
			fn(j, r) {
				fv(k, s) {
					if (s[k] == 'L')
						dir = (dir + 1) & 3;
					else if (s[k] == 'R')
						dir = (dir + 3) & 3;
					else {
						x += dx[dir];
						y += dy[dir];
						if (dir == NORTH)
							line[x][y] |= 1;
						else if (dir == SOUTH)
							line[x][y-1] |= 1;
						else if (dir == WEST)
							line[x][y] |= 2;
						else
							line[x-1][y] |= 2;
					}
				}
			}
		}
		bool out = true, first = true;
		int s1 = 0, s2 = 0;
		//for (x = 500; x <= 7500; ++x) {
		for (x = 3800; x <= 4200; ++x) {
			out = true, first = true;
		//	for (y = 500; y <= 7500; ++y) {
		for (y = 3800; y <= 4200; ++y) {
				if (!out) ++s2;
				if (!first) world[x][y] |= 1;
				if (line[x][y+1] & 2) {
					first = false;
					out = !out;
				}
			}
		}
		//for (x = 500; x <= 7500; ++x) {
		for (x = 3800; x <= 4200; ++x) {
			out = true, first = true;
		//	for (y = 7500; y >= 500; --y) {
			for (y = 4200; y >= 3800; --y) {
				if (!out) ++s1;
				if (!first) world[x][y] |= 2;
				if (line[x][y] & 2) {
					first = false;
					out = !out;
				}
			}
		}
		if (s1 != s2) throw "ERR";
		s1 = 0;
		//for (y = 500; y <= 7500; ++y) {
		for (y = 3800; y <= 4200; ++y) {
			out = true, first = true;
		//	for (x = 500; x <= 7500; ++x) {
		for (x = 3800; x <= 4200; ++x) {
				if (!out) ++s1;
				if (!first) world[x][y] |= 8;
				if (line[x+1][y] & 1) {
					first = false;
					out = !out;
				}
			}
		}
		if (s1 != s2) throw "ERR";
		s1 = 0;
		//for (y = 500; y <= 7500; ++y) {
		for (y = 3800; y <= 4200; ++y) {
			out = true, first = true;
		//	for (x = 7500; x >= 500; --x) {
			for (x = 4200; x >= 3800; --x) {
				if (!out) ++s1;
				if (!first) world[x][y] |= 4;
				if (line[x][y] & 1) {
					first = false;
					out = !out;
				}
			}
		}
		if (s1 != s2) throw "ERR";
		s1 = 0;
		int a;
		for (x = 3800; x <= 4200; ++x) {
		for (y = 3800; y <= 4200; ++y) {
		//for (y = 500; y <= 7500; ++y) {
		//	for (x = 500; x <= 7500; ++x) {
				a = world[x][y];
				if ((a & 3) == 3 || (a & 12) == 12) s1++;
			}
		}
		s1 -= s2;
		cout << "Case #" << test+1 << ": " << s1;
		cout << endl;
	}

	return 0;
}
