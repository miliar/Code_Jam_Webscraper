#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))
#define P 300

using namespace std;

struct state {
	int x, y;
	int p1, p2;
	state(int X, int Y, int P1, int P2) {
		x = X; y = Y; p1 = P1; p2 = P2;
	}	
};

struct port {
	int x, y;
	int dir;
	friend bool operator < (const port &u, const port &v) {
		if (MP(u.x, u.y) == MP(v.x, v.y)) return u.dir < v.dir;
		return MP(u.x, u.y) < MP(v.x, v.y);
	}
};


map<port, int> ports;
int pk;
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

int n, m;
char a[22][22];
int d[15][15][P][P];
deque<state> q;
int fire[15][15][4];
int px[P], py[P];

int pnum(port po) {
	if (ports.count(po) > 0) return ports[po];	
	pk++;
	px[pk] = po.x;
	py[pk] = po.y;
	return ports[po] = pk;
}


void push(state st, bool zero, int dist) {
	int &D = d[st.x][st.y][st.p1][st.p2];
	if (D == -1) {
		D = dist;
		if (zero) q.push_front(st); else q.push_back(st);
	}
}

void bulidfire() {
	FOR(i, n) FOR(j, m) FOR(dir, 4) {
		int x = i, y = j;
		while (1) {
			int xx = x + dx[dir], yy = y + dy[dir];
			if (xx < 0 || yy < 0 || xx >= n || yy >= m) break;
			if (a[xx][yy] == '#') break;
			x = xx; y = yy;
		}
		port po;
		po.dir = dir;
		po.x = x;
		po.y = y;
		fire[i][j][dir] = pnum(po);
	}
}

void solvecase() {
	pk = 0;
	ports.clear();
	CLR(d, -1);
	scanf("%d%d\n", &n, &m);
	FOR(i, n) scanf("%s\n", a[i]);
	int x0 = 0, y0 = 0, x1, y1;
	FOR(i, n) FOR(j, m) {
		if (a[i][j] == 'O') { x0 = i; y0 = j; }
		if (a[i][j] == 'X') { x1 = i; y1 = j; }
	}
	bulidfire();
	q.clear();
	push(state(x0, y0, 0,0), false, 0);	
	while (!q.empty()) {
		state st = q.front();
		q.pop_front();
		int dist = d[st.x][st.y][st.p1][st.p2];
		if (st.x == x1 && st.y == y1) {
			printf("%d", dist);
			return;
		}
		// just go
		FOR(dir, 4) {
			int x = st.x + dx[dir];
			int y = st.y + dy[dir];
			if (x < 0 || y < 0 || x >= n || y >= m) continue;
			if (a[x][y] != '#') {
				push(state(x,y,st.p1,st.p2), false, dist+1);
			}
		}
		// go to p1
		if (st.p1 && st.p2 && st.x == px[st.p1] && st.y == py[st.p1]) {
			push(state(px[st.p2], py[st.p2], st.p1, st.p2), false, dist+1);
		}
		// go to p2
		if (st.p1 && st.p2 && st.x == px[st.p2] && st.y == py[st.p2]) {
			push(state(px[st.p1], py[st.p1], st.p1, st.p2), false, dist+1);
		}
		// fire p1
		FOR(i, 4) {
			push(state(st.x, st.y, fire[st.x][st.y][i], st.p2), true, dist);
		}
		// fire p2
		FOR(i, 4) {
			push(state(st.x, st.y, st.p1, fire[st.x][st.y][i]), true, dist);
		}
	}
	printf("THE CAKE IS A LIE");
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}