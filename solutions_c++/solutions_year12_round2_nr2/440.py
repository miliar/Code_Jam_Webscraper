#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

#define debug 1
#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define Rep(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb push_back
#define mp make_pair
#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define cp(a) cerr << "(" << #a << "," << a << ") "
#define cen cerr << endl

typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int inf = 0x7fffffff;

const int Size = 1000 * 1000 + 1;
char buffer[Size];

const int size = 101;
int up[size][size];
int down[size][size];

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};
double minTime[size][size];
int color[size][size];

struct Vert {
	double h;
	int r, c;
	Vert(int r, int c, double h) : r(r), c(c), h(h) {}
};

int solution(int nTest) {
	printf("Case #%d: ", nTest + 1);
	double H;
	scanf("%lf", &H);
	int R, C;
	scanf("%d%d", &R, &C);
	For(i, 0, R) {
		For(j, 0, C) {
			minTime[i][j] = inf;
			color[i][j] = 0;
			scanf("%d", &up[i][j]);
		}
	}
	For(i, 0, R) {
		For(j, 0, C) {
			scanf("%d", &down[i][j]);
		}
	}
	Vert source(0, 0, H);
	queue<Vert> q;
	minTime[0][0] = 0;
	color[0][0] = 1;
	q.push(source);
	while(sz(q)) {
		Vert u = q.front();
		q.pop();
		double h = u.h;
		int r = u.r;
		int c = u.c;
		For(k, 0, 4) {
			int nr = r + dr[k];
			int nc = c + dc[k];
			if(nr < 0 || nr >= R || nc < 0 || nc >= C) {
				continue;
			}
			if(color[nr][nc]) {
				continue;
			}
			if(up[nr][nc] - h < 50 || up[nr][nc] - down[nr][nc] < 50
					|| up[nr][nc] - down[r][c] < 50) {
				continue;
			}
			if(up[r][c] - down[nr][nc] < 50) {
				continue;
			}
			q.push(Vert(nr, nc, h));
			color[nr][nc] = 1;
			minTime[nr][nc] = 0;
		}
	}
	priority_queue<pair<double, pii> > pq;
	For(i, 0, R) {
		For(j, 0, C) {
			pq.push(mp(-minTime[i][j], mp(i, j)));
		}
	}
	while(sz(pq)) {
		double t = -pq.top().first;
		int r = pq.top().second.first;
		int c = pq.top().second.second;
		pq.pop();
		if(minTime[r][c] < t) {
			continue;
		}
		double h = H - t * 10;
		h = max(0., h);
		minTime[r][c] = t;
		For(k, 0, 4) {
			int nr = r + dr[k];
			int nc = c + dc[k];
			if(nr < 0 || nr >= R || nc < 0 || nc >= C) {
				continue;
			}
			if(up[nr][nc] - down[nr][nc] < 50
					|| up[nr][nc] - down[r][c] < 50) {
				continue;
			}
			if(up[r][c] - down[nr][nc] < 50) {
				continue;
			}
			double time = t;
			if(up[nr][nc] - h < 50) {
				time += (50 - (up[nr][nc] - h)) / 10.;
			}
			double nh = H - time * 10;
			if(nh - down[r][c] >= 20) {
				time += 1;
			}
			else {
				time += 10;
			}
			if(minTime[nr][nc] <= time) {
				continue;
			}
			pq.push(mp(-time, mp(nr, nc)));
		}
	}

	printf("%.9lf\n", minTime[R - 1][C - 1]);
	


	return 1;
}

int main() {
	if(debug) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}


	int i = 0, n = 99999;
	scanf("%d", &n);
	while(i < n && solution(i)) {
		i++;
	}

	return 0;
}
