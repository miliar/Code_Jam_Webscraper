#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <climits>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define clr(x) memset(x,0,sizeof(x)) 

const int N = 13;

int sta[N][N][N][N];
int wx[4] = {1, 0, -1, 0};
int wy[4] = {0, 1, 0, -1};

bool mat[N][N];
int cases = 1;

int sx1, sy1, sx2, sy2;
int ex1, ey1, ex2, ey2;

int n, m;

bool check(int x, int y) {
	if(x >= 0 && x < n && y >= 0 && y < m && mat[x][y])return true;
	return false;
}

bool cet(int x1, int y1, int x2, int y2) {
	int x, y;
	for(int k = 0; k < 4; k++) {
		x = x1 + wx[k];
		y = y1 + wy[k];
		if(x == x2 && y == y2) {
			return true;
		}
	}
	return false;
}

struct ssta {
	int x1, y1, x2, y2;
	void fix(int xx1, int yy1, int xx2, int yy2) {
		x1 = xx1, y1 = yy1;
		x2 = xx2, y2 = yy2;
	}
}tmp;

bool end(int x1, int y1, int x2, int y2) {
	if(x1 == ex1 && y1 == ey1 && x2 == ex2 && y2 == ey2)return true;
	if(x1 == ex2 && y1 == ey2 && x2 == ex1 && y2 == ey1)return true;
	return false;
}

int bfs2() {
	memset(sta, 0, sizeof(sta));
	tmp.fix(sx1, sy1, sx2, sy2);
	queue<ssta>Q;
	Q.push(tmp);
	sta[sx1][sy1][sx2][sy2] = 1;

	int x1, y1, x2, y2;
	int nx1, ny1, nx2, ny2;
	int fx1, fy1, fx2, fy2;
	while(!Q.empty()) {
		tmp = Q.front(), Q.pop();
		x1 = tmp.x1, y1 = tmp.y1;
		x2 = tmp.x2, y2 = tmp.y2;

		if(end(x1, y1, x2, y2))return sta[x1][y1][x2][y2];

		//printf("%d %d %d %d\n", x1, y1, x2, y2);
		bool flag = cet(x1, y1, x2, y2);

		for(int k = 0; k < 4; k++) {
			int k1 = (k + 2) % 4;
			nx1 = x1, ny1 = y1;
			nx2 = x2 + wx[k], ny2 = y2 + wy[k];
			fx2 = x2 + wx[k1], fy2 = y2 + wy[k1];

			if(check(fx2, fy2) && (fx2 != nx1 || fy2 != ny1) && (nx1 != nx2 || ny1 != ny2)) {
				if(check(nx2, ny2) && (flag || cet(nx1, ny1, nx2, ny2)) && !sta[nx1][ny1][nx2][ny2]) {
					sta[nx1][ny1][nx2][ny2] = sta[x1][y1][x2][y2] + 1;
					tmp.fix(nx1, ny1, nx2, ny2);
					Q.push(tmp);
				}
			}

			nx1 = x1 + wx[k], ny1 = y1 + wy[k];
			fx1 = x1 + wx[k1], fy1 = y1 + wy[k1];
			nx2 = x2, ny2 = y2;
			if(check(fx1, fy1) && (fx1 != nx2 || fy1 != ny2) && (nx1 != nx2 || ny1 != ny2)) {
				if(check(nx1, ny1) && (flag || cet(nx1, ny1, nx2, ny2)) && !sta[nx1][ny1][nx2][ny2]) {
					sta[nx1][ny1][nx2][ny2] = sta[x1][y1][x2][y2] + 1;
					tmp.fix(nx1, ny1, nx2, ny2);
					Q.push(tmp);
				}
			}
		}
	}

	return 0;
}

int sta1[N][N];
struct ssta1 {
	int x, y;
	void fix(int x1, int y1) {
		x = x1, y = y1;
	}
}tmp1;

int bfs1() {
	memset(sta1, 0, sizeof(sta1));
	tmp1.fix(sx1, sy1);
	queue<ssta1>Q;
	Q.push(tmp1);
	int x, y;
	int nx, ny;
	sta1[sx1][sy1] = 1;

	while(!Q.empty()) {
		tmp1 = Q.front(), Q.pop();
		x = tmp1.x, y = tmp1.y;

		if(x == ex1 && y == ey1)return sta1[x][y];

		for(int k = 0; k < 4; k++) {
			nx = x + wx[k];
			ny = y + wy[k];
			if(check(nx, ny) && !sta1[nx][ny]) {
				sta1[nx][ny] = sta1[x][y] + 1;
				tmp1.fix(nx, ny);
				Q.push(tmp1);
			}
		}
	}
	return 0;
}

void solve() {
	memset(mat, false, sizeof(mat));
	scanf("%d %d", &n, &m);
	char c;

	int boxs = 0, goals = 0;

	for(int i = 0; i < n; i++) {
		getchar();
		for(int j = 0; j < m; j++) {
			c = getchar();
			if(c == '.')mat[i][j] = true;
			else if(c == 'o') {
				mat[i][j] = true;
				if(!boxs)sx1 = i, sy1 = j;
				else sx2 = i, sy2 = j;
				boxs++;
			}
			else if(c == 'x') {
				mat[i][j] = true;
				if(!goals)ex1 = i, ey1 = j;
				else ex2 = i, ey2 = j;
				goals++;
			}
			else if(c == 'w') {
				mat[i][j] = true;
				if(!boxs)sx1 = i, sy1 = j;
				else sx2 = i, sy2 = j;
				if(!goals)ex1 = i, ey1 = j;
				else ex2 = i, ey2 = j;
				boxs++;
				goals++;
			}
		}
	}
	//printf("%d %d %d %d\n", sx1, sy1, sx2, sy2);
	//printf("%d %d %d %d\n", ex1, ey1, ex2, ey2);

	printf("Case #%d: ", cases++);
	if(boxs == 2) {
		printf("%d\n", bfs2() - 1);
	}
	else {
		printf("%d\n", bfs1() - 1);
	}
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	while(T--)solve();
	return 0;
}

/*Powered By Lynn-Beta1*/