#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORC( it, V ) for( __typeof( (V).begin() ) it = (V).begin(); it != (V).end(); ++it )
#define SZ(a) a.size()
#define INF 1000000000
#define MAXQ 1000
string i2s(int x) { ostringstream tmp;  tmp << x;  return tmp.str(); }
int s2i(string s) { istringstream i(s);  int x;  i >> x;  return x; } 

const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

int m, n;
string a[30];
int sx, sy;
int ex, ey;
int qx[MAXQ];
int qy[MAXQ];
int first, last;
int f[30][30];
int dem;
bool inqueue[33][33];
bool kt[33][33];
int bay[33][33][5];

void read_data() {
	cin >> m >> n;
	REP(i, m) cin >> a[i];
}

void init() {
	REP(i, m) REP(j, n) {
		if (a[i][j] == 'O') {
			sx = i;
			sy = j;
			a[i][j] = '.';
		}
		if (a[i][j] == 'X') {
			ex = i;
			ey = j;
			a[i][j] = '.';
		}
		inqueue[i][j] = false;
	}
	REP(i, m) REP(j, n) f[i][j] = INF;
	first = 1;
	last = 1;
	dem = 1;
	qx[1] = sx;
	qy[1] = sy;
	f[sx][sy] = 0;
	inqueue[sx][sy] = true;	
}

void init2() {
	REP(x, m) REP(y, n) {
		kt[x][y] = false;
		REP(dir, 4) {
			int xx = x + dx[dir];
			int yy = y + dy[dir];
			if (xx < 0 || m <= xx || yy < 0 || n <= yy || a[xx][yy] == '#') kt[x][y] = true;
		}
		if (!kt[x][y]) continue;
		REP(dir, 4) {
			int xx = x;
			int yy = y;
			while (true) {
				xx = xx + dx[dir];
				yy = yy + dy[dir];
				if (xx < 0 || m <= xx || yy < 0 || n <= yy || a[xx][yy] == '#') {
					bay[x][y][dir] = abs(x - xx) + abs(y - yy) - 1;
					break;
				}
			}
		}
	}
}

void process() {
	while (dem) {
		int x = qx[first];
		int y = qy[first];
//		cout << "pop " << x << " " << y << " " << f[x][y] << endl;
		inqueue[x][y] = false;
		first = (first + 1) % MAXQ;
		dem--;
		REP(dir, 4) {
			int xx = x + dx[dir];
			int yy = y + dy[dir];
			if (xx < 0 || m <= xx || yy < 0 || n <= yy || a[xx][yy] == '#') continue;
//			cout << "push " << xx << " " << yy << endl;
			if (f[xx][yy] > f[x][y] + 1) {
//				cout << xx << " " << yy << endl;
				f[xx][yy] = f[x][y] + 1;
				if (!inqueue[xx][yy]) {
					inqueue[xx][yy] = true;
					last = (last + 1) % MAXQ;
					qx[last] = xx;
					qy[last] = yy;
					dem++;
					
				}
			}
		}
		if (!kt[x][y]) continue;
		REP(dir, 4) {
			int t = bay[x][y][dir];
			int xx = x + dx[dir] * t;
			int yy = y + dy[dir] * t;
			if (xx < 0 || m <= xx || yy < 0 || n <= yy || a[xx][yy] == '#') continue;
//			cout << "push " << xx << " " << yy << endl;
			if (f[xx][yy] > f[x][y] + 1) {
//				cout << xx << " " << yy << endl;
				f[xx][yy] = f[x][y] + 1;
				if (!inqueue[xx][yy]) {
					inqueue[xx][yy] = true;
					last = (last + 1) % MAXQ;
					qx[last] = xx;
					qy[last] = yy;
					dem++;
					
				}
			}			
		}
	}
	if (f[ex][ey] == INF) {
		cout << "THE CAKE IS A LIE" << endl;
	} else {
		cout << f[ex][ey] << endl;
	}
}

int main() {
	int test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ": ";
		read_data();
		init();
		init2();
		process();
	}
	return 0;
};

