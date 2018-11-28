#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 10000000000000000LL
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

struct Pos {
	int x, y, d;
	Pos(): x(0), y(0), d(0){}
	Pos(int x, int y, int d): x(x), y(y), d(d){}
	int operator < (const Pos& p) const {
		if(p.x != x) return x < p.x;
		if(p.y != y) return y < p.y;
		if(p.d != d) return d < p.d;
		return 0;
	}
};

typedef pair<long long, Pos> P;

int s[30][30], w[30][30], T[30][30];
int dist[30][30][4];
int dir[4][4][3] = {
	{{0, 0, 1}, {1, 0, 1}, {0, 0, 3}, {0, -1, 3}}, 
	{{0, 0, 0}, {-1, 0, 0}, {0, 0, 2}, {0, -1, 2}}, 
	{{0, 0, 3}, {-1, 0, 3}, {0, 0, 1}, {0, 1, 1}}, 
	{{0, 0, 2}, {1, 0, 2}, {0, 0, 0}, {0, 1, 0}}, 
};

long long norm(long long a, long long m) {
	return (a % m + m) % m;
}

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				cin >> s[i][j] >> w[i][j] >> T[i][j];
				for(int k = 0; k < 4; ++k) dist[i][j][k] = INF;
			}
		}
		dist[n - 1][0][0] = 0;
		priority_queue<P, vector<P>, greater<P> > que;
		que.push(P(0, Pos(n - 1, 0, 0)));
		while(que.size()) {
			Pos p = que.top().second;
			long long di = que.top().first;
			que.pop();
			if(dist[p.x][p.y][p.d] < di) continue;
			if(p.x == 0 && p.y == m - 1&& p.d == 2) break;
			for(int i = 0; i < 4; ++i) {
				int xx = p.x + dir[p.d][i][0], yy = p.y + dir[p.d][i][1], dd = dir[p.d][i][2];
				if(xx < 0 || yy < 0 || xx >= n || yy >= m) continue;
				long long nextt = di;
				if(xx == p.x && yy == p.y) {
					long long next = norm(di - T[p.x][p.y], s[p.x][p.y] + w[p.x][p.y]);
					if(next < s[p.x][p.y]) {
						if(i < 2) nextt = di + 1;
						else nextt = di + 1 + s[p.x][p.y] - next;
					}else {
						if(i < 2) nextt = di + 1 + w[p.x][p.y] + s[p.x][p.y] - next;
						else nextt = di + 1;
					}
				}else {
					nextt += 2;
				}
				if(dist[xx][yy][dd] <= nextt) continue;
				dist[xx][yy][dd] = nextt;
				que.push(P(nextt, Pos(xx, yy, dd)));
			}
		}
		printf("Case #%d: %d\n", t + 1, dist[0][m - 1][2]);
	}
	return 0;
}
