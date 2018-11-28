// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <deque>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

struct portal {
	int x, y, dir;
	portal() {}
	portal(int x_, int y_, int dir_) {
		x = x_;
		y = y_;
		dir = dir_;
	}
};

bool operator<(const portal &a, const portal &b) {
	if (a.x != b.x)
		return a.x < b.x;
	if (a.y != b.y)
		return a.y < b.y;
	return a.dir < b.dir;
}

struct state {
	portal blue, yellow;
	int x, y;
};

bool operator<(const state &a, const state &b) {
	if (a.blue < b.blue)
		return true;
	if (b.blue < a.blue)
		return false;
	if (a.yellow < b.yellow)
		return true;
	if (b.yellow < a.yellow)
		return false;
	if (a.x != b.x)
		return a.x < b.x;
	return a.y < b.y;
}

map<state, int> visit;

struct qelem {
	state where;
	int mov;
}qe,nq;

bool operator<(const qelem &a, const qelem &b) {
	return a.mov > b.mov;
}

char grid[10][11];

int dirs[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int n, m;
		scanf("%d %d",&n,&m);
		int sx, sy, cx, cy;
		for (int i=0; i<n; ++i) {
			scanf("%s", grid[i]);
			for (int j=0; j<m; ++j) {
				if (grid[i][j] == 'X') {
					cx = i;
					cy = j;
				}
				else if (grid[i][j] == 'O') {
					sx = i;
					sy = j;
				}
			}
		}
		visit.clear();
		priority_queue<qelem> Q;
		qe.mov = 0;
		qe.where.x = sx;
		qe.where.y = sy;
		qe.where.blue = portal(-1,-1,-1);
		qe.where.yellow = portal(-1,-1,-1);
		visit[qe.where] = 0;
		Q.push(qe);
		while(!Q.empty()) {
			qe = Q.top();
			Q.pop();
			if (qe.where.x == cx && qe.where.y == cy)
				goto done;
//			printf("here with x = %d y = %d %d\n", qe.where.x, qe.where.y, qe.mov);
			for (int d=0; d<4; ++d) {
				nq.mov = qe.mov;
				nq.where = qe.where;
				int x = qe.where.x;
				int y = qe.where.y;
				while(x >= 0 && x < n && y >= 0 && y < m && grid[x][y] != '#') {
					x += dirs[d][0];
					y += dirs[d][1];
				}
				if (qe.where.blue.x == x && qe.where.blue.y == y && qe.where.blue.dir == (d+2)%4)
					continue;
				if (qe.where.yellow.x == x && qe.where.yellow.y == y && qe.where.yellow.dir == (d+2)%4)
					continue;
				nq.where.yellow = portal(x, y, (d+2)%4);
				if (visit.find(nq.where) == visit.end()) {
					visit[nq.where] = nq.mov;
					Q.push(nq);
				}
				nq.where.blue = portal(x, y, (d+2)%4);
				nq.where.yellow = qe.where.yellow;
				if (visit.find(nq.where) == visit.end()) {
					visit[nq.where] = nq.mov;
					Q.push(nq);
				}
				for (int d2=0; d2<4; ++d2) {
					if (d == d2) continue;
					x = qe.where.x;
					y = qe.where.y;
					while(x >= 0 && x < n && y >= 0 && y < m && grid[x][y] != '#') {
						x += dirs[d2][0];
						y += dirs[d2][1];
					}
						if (qe.where.blue.x == x && qe.where.blue.y == y && qe.where.blue.dir == (d2+2)%4)
							continue;
						if (qe.where.yellow.x == x && qe.where.yellow.y == y && qe.where.yellow.dir == (d2+2)%4)
							continue;
						nq.where.yellow = portal(x, y, (d2+2)%4);
						if (visit.find(nq.where) == visit.end()) {
							visit[nq.where] = nq.mov;
							Q.push(nq);
						}
				}
			}
			for (int d=0; d<4; ++d) {
				nq.where = qe.where;
				nq.where.x += dirs[d][0];
				nq.where.y += dirs[d][1];
				if (nq.where.x == nq.where.blue.x && nq.where.y == nq.where.blue.y && nq.where.blue.dir == (d+2)%4 && nq.where.yellow.dir >= 0) {
					nq.where.x = nq.where.yellow.x + dirs[nq.where.yellow.dir][0];
					nq.where.y = nq.where.yellow.y + dirs[nq.where.yellow.dir][1];
				}
				else if (nq.where.x == nq.where.yellow.x && nq.where.y == nq.where.yellow.y && nq.where.yellow.dir == (d+2)%4 && nq.where.blue.dir >= 0) {
					nq.where.x = nq.where.blue.x + dirs[nq.where.blue.dir][0];
					nq.where.y = nq.where.blue.y + dirs[nq.where.blue.dir][1];
				}
				if (nq.where.x < 0 || nq.where.x >= n)
					continue;
				if (nq.where.y < 0 || nq.where.y >= m)
					continue;
				if (grid[nq.where.x][nq.where.y] == '#')
					continue;
				if (visit.find(nq.where) != visit.end() && visit[nq.where] <= qe.mov + 1)
					continue;
				visit[nq.where] = nq.mov = qe.mov + 1;
				Q.push(nq);
			}
		}
		puts("THE CAKE IS A LIE");
		continue;
		done: printf("%d\n", qe.mov);
	}
	return 0;
}
