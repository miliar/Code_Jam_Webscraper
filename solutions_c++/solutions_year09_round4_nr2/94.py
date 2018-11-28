// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
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
typedef pair<short, int> PCI;

char grid[64][65];

struct qelem {
	int x, y, cost, mask;
}qe, nq;

bool operator<(const qelem &a, const qelem &b) {
	return a.cost > b.cost;
}

int dist[10][6][1<<12];

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int n, m, f;
		scanf("%d %d %d", &n, &m, &f);
		for (int i=0; i<n; ++i)
			scanf("%s", grid[i]);
		qe.x = qe.y = 0;
		qe.mask = 0;
		for (int i=0; i<n && i < 2; ++i)
			for (int j=0; j<m; ++j)
				if (grid[i][j] == '.')
					qe.mask |= 1 << (i * m + j);
		memset(dist, 0X7F, sizeof(dist));
		dist[qe.x][qe.y][qe.mask] = 0;
		qe.cost = 0;
		priority_queue<qelem> Q;
		Q.push(qe);
		while(!Q.empty()) {
			qe = Q.top();
			if (qe.x == n-1) {
				printf("Yes %d\n", qe.cost);
				goto done;
			}
			Q.pop();
	//		if (qe.cost > dist[qe.x][qe.y][qe.mask])
	//			continue;
		/*	if (qe.x == 0 && qe.y == 3) {
			printf("%d %d %d %d\n", qe.x, qe.y, qe.mask, qe.cost);
			for (int i=0; i<2; ++i) {
				for (int j=0; j<m; ++j) {
					if (qe.mask & (1 << (i * m + j)))
						putchar('.');
					else putchar('#');
				}
				puts("");
			}
			}*/
			// dig if possible
			for (int dy=-1; dy<=1; dy += 2) {
				nq.y = qe.y + dy;
				if (nq.y >= 0 && nq.y < m && (qe.mask & (1 << nq.y)) && !(qe.mask & (1 << (m + nq.y)))) {
					nq.mask = qe.mask | (1 << (m + nq.y));
					nq.cost = qe.cost + 1;
					nq.x = qe.x;
					nq.y = qe.y;
			//		if (nq.x == 0 && nq.y == 3)
			//			printf("here with %d %d %d\n", nq.mask, dy, dist[nq.x][nq.y][nq.mask]);
					if (nq.cost < dist[nq.x][nq.y][nq.mask]) {
						dist[nq.x][nq.y][nq.mask] = nq.cost;
						Q.push(nq);
					}
				}
			}
			// move if possible
			for (int dy=-1; dy<=1; dy += 2) {
				nq.y = qe.y + dy;
				if (nq.y >= 0 && nq.y < m && (qe.mask & (1<<nq.y))) {
					// determine how far it falls
					if (qe.mask & (1 << (nq.y + m))) {
						int dfall = 1;
						nq.mask = qe.mask >> m;
						for (int r=qe.x + 2; r < n; ++r, ++dfall) {
							if (grid[r][nq.y] == '#')
								break;
							nq.mask  = 0;
						}
				//		if (qe.x == 0 && qe.y == 3)
				//			printf("**** %d %d %d %d\n", nq.y, dfall, qe.cost, nq.mask);
						if (dfall <= f) {
							nq.x = qe.x + dfall;
							for (int i=0; i < 2 && i + nq.x < n; ++i)
								for (int j=0; j<m; ++j)
									if (grid[nq.x + i][j] == '.')
										nq.mask |= (1 << (i * m + j));
							nq.cost = qe.cost;
						}
						else
							nq.cost = 0X7F7F7F7F;
					}
					else {
						nq.x = qe.x;
						nq.mask = qe.mask;
						nq.cost = qe.cost;
					}
					if (nq.cost < 0X7F7F7F7F && nq.cost < dist[nq.x][nq.y][nq.mask]) {
						dist[nq.x][nq.y][nq.mask] = nq.cost;
						Q.push(nq);
					}
				}
			}
		}
		puts("No");
		continue;
done:;
	}
	return 0;
}
