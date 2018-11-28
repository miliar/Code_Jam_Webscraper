#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

const int N = 150;

int ce[N][N];
int fl[N][N];

int tm[N][N];

int h, n, m;

const int INF = 0x7fffffff;
void edge(int xi, int yi, int xj, int yj, priority_queue<pair<int, pair<int, int> > > &pq) {
	// 3rd
	if (xj < 0) return;
	if (xj >= n) return;
	if (yj < 0) return;
	if (yj >= m) return;
	// 2nd
	if (fl[xj][yj] + 50 > ce[xj][yj]) return;
	// 1st 1
	if (fl[xi][yi] + 50 > ce[xj][yj]) return;

	if (fl[xj][yj] + 50 > ce[xi][yi]) return;

	int t = tm[xi][yi];

	int water = max(0, h-t);
	int maxF = ce[xj][yj] - 50;
	
	if (water > maxF) {
		t += water - maxF;
	}

	if (t > 0) {
		water = max(0, h-t);
		if (fl[xi][yi] + 20 > water) {
			t += 100;
		} else {
			t += 10;
		}
	} 
	if (tm[xj][yj] <= t) return;
	tm[xj][yj] = t;
	pq.push(make_pair(-t, make_pair(xj, yj)));
}

int main(void) {
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; ++tc) {
		scanf("%d%d%d", &h, &n, &m);
		for (int i=0; i<n; ++i) for (int j=0; j<m; ++j) {
			scanf("%d", ce[i]+j);
		}
		for (int i=0; i<n; ++i) for (int j=0; j<m; ++j) {
			 scanf("%d", fl[i]+j);
			 tm[i][j] = INF;
		}
		tm[0][0] = 0;
		priority_queue<pair<int, pair<int,int> > > pq;
		pq.push(make_pair(0, make_pair(0,0)));
		while (!pq.empty()) {
			int t = -pq.top().first;
			int x = pq.top().second.first;
			int y = pq.top().second.second;
			pq.pop();
			if (tm[x][y] < t) continue;
			edge(x, y, x-1, y, pq);
			edge(x, y, x+1, y, pq);
			edge(x, y, x, y-1, pq);
			edge(x, y, x, y+1, pq);
		}
		printf("Case #%d: %.1lf\n", tc, ((double)tm[n-1][m-1])/10);
	}
	return 0;
}
