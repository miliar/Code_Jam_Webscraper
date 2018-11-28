#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 15

int i, j, k, n, m, x, y, z, t, T;
int xx, yy, xxx, yyy;

struct pt {
	int x;
	int y;
	friend int operator < (pt a, pt b) {
		if (a.x != b.x) {
			return a.x < b.x;
		}
		return a.y < b.y;
	}
};
pt p, p1, p2, p3;
vector<pt> v, v1, v2, tg;

map<vector<pt>, int> d;
char a[N][N], b[N][N], c[N][N], u[N][N];
queue<vector<pt> > q;

int ch(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

void dfs(int x, int y) {
	int i, xx, yy;
	u[x][y] = 1;
	for (i = 0; i < 4; i ++) {
		xx = x + dx[i];
		yy = y + dy[i];
		if (ch(xx, yy)) {
			if (u[xx][yy] == 0 && b[xx][yy] == 'x') {
				dfs(xx, yy);
			}
		}
	}
}

int isst() {
	memset(u, 0, sizeof(u));
	int i, j, t, f = 0;
	for (i = 0; i < n; i ++) {
		for (j = 0; j < m; j++) {
			if (b[i][j] == 'x') {
				dfs(i, j);
				f = 1;
				break;
			}
		}
		if (f == 1) {
			break;
		}
	}
	for (i = 0; i < n; i++) {
		for ( j= 0; j < m; j ++) {
			if (b[i][j] == 'x' && u[i][j] == 0) {
				return 0;
			}
		}
	}
	return 1;
}

int res, f;

int main() {
	freopen("big.in", "r", stdin);
	freopen("big.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n >> m;
		memset(a, 0, sizeof(a));
		memset(c, 0, sizeof(c));
		memset(b, 0, sizeof(b));
		d.clear();
		while (!q.empty()) {
			q.pop();
		}
		for ( i= 0; i < n; i++) {
			cin >> a[i];
		}
		v.clear();
		tg.clear();
		for (i = 0; i <n; i ++) {
			for (j = 0;  j< m; j ++) {
				if (a[i][j] == 'o') {
					p.x = i;
					p.y = j;
					v.push_back(p);
				}
				if (a[i][j] == 'x') {
					p.x = i;
					p.y = j;
					tg.push_back(p);
				}
				if (a[i][j] == 'w') {
					p.x = i;
					p.y = j;
					v.push_back(p);
					tg.push_back(p);
				}
			}
		}
		sort(v.begin(), v.end());
		sort(v2.begin(), v2.end());
		for (i = 0; i < n; i++ ){
			for (j = 0; j < m; j++) {
				if (a[i][j] == 'x' || a[i][j] == 'o' || a[i][j] == 'w') {
					a[i][j] = '.';
				}
			}
		}
		d[v] = 0;
		q.push(v);


		while (!q.empty()) {
			v = q.front();
			q.pop();
			for (i = 0; i < v.size(); i ++) {
				if (v[i].x != tg[i].x || v[i].y != tg[i].y) {
					break;
				}
			}
			if (i == v.size()) {
				break;
			}
			memset(b, 0, sizeof(b));
			for (i=  0; i < n; i ++) {
				for (j = 0; j < m; j ++) {
					b[i][j] = a[i][j];
				}
			}
			for (i = 0; i < v.size(); i ++) {
				b[v[i].x][v[i].y] = 'x';
			}
			if (isst()) {
				f = 1;
			} else {
				f = 0;
			}
			for (i = 0; i < v.size(); i ++) {
				x = v[i].x;
				y = v[i].y;
				for (j = 0; j < 4; j ++) {
					xx = v[i].x + dx[j];
					yy = v[i].y + dy[j];
					xxx = v[i].x + dx[(j + 2) % 4];
					yyy = v[i].y + dy[(j + 2) % 4];
					if (ch(xx ,yy) && ch(xxx, yyy)) {
						if (b[xx][yy] == '.' && b[xxx][yyy] == '.') {
							if (f == 1) {
								v2 = v;
								v2[i].x = xx;
								v2[i].y = yy;
								sort(v2.begin(), v2.end());
								if (d.find(v2) == d.end()) {
									d[v2] = d[v] + 1;
									q.push(v2);
								}
							} else {
								b[x][y] = '.';
								b[xx][yy] = 'x';
								if (isst()) {
									v2 = v;
									v2[i].x = xx;
									v2[i].y = yy;
									sort(v2.begin(), v2.end());
									if (d.find(v2) == d.end()) {
										d[v2] = d[v] + 1;
										q.push(v2);
									}
								}
								b[x][y] = 'x';
								b[xx][yy] = '.';
							}
						}
					}
				}
				
			}
			
			
		}


		if (d.find(tg) == d.end()) {
			res = -1;
		} else {
			res = d[tg];
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
	}






	
