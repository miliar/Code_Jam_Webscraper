#include <cstdio>
#include <cmath>
#include <cstring>

#include <memory>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

#define TASK "B"
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;

typedef long long int64;
typedef pair <int, int> Point;

const int di[4] = {-1, 0, 0, 1},
		  dj[4] = {0, -1, 1, 0};

const int MAXN = 128, MAXV = MAXN*MAXN, MAXE = 3*MAXV, MAX_ALTITUDE = 16384;

int T, n, m, colors, es;

int a[MAXN][MAXN];
int color[MAXN][MAXN];
bool mark[MAXN][MAXN];

int first[MAXV], next[MAXE], jj[MAXE];

inline int code(int i, int j) {
	return i * MAXN + j;
}

inline Point decode(int v) {
	return MP(v / MAXN, v % MAXN);
}

void addEdge(int a, int b) {
	es++;
	next[es] = first[a];
	first[a] = es;
	jj[es] = b;
}

void firstDFS(int v) {
	bool isSink = true;
	int i = decode(v).first, j = decode(v).second;
	
	int lowestAlt = MAX_ALTITUDE;
	int where = -1;

	if (mark[i][j]) return;
	
	mark[i][j] = true;

	for (int k = 0; k < 4; k++) {
		int newi = i + di[k], newj = j + dj[k], newv = code(newi, newj);
		if (1 <= newi && newi <= n && 1 <= newj && newj <= m) {
			if (a[newi][newj] < a[i][j]) {
				isSink = false;
				if (a[newi][newj] < lowestAlt) {
					lowestAlt = a[newi][newj];
					where = newv;
				}
			}
		}
	}

	if (!isSink) {
		assert(where != -1);

		addEdge(v, where);
		addEdge(where, v);
		firstDFS(where);
	}
}

void secondDFS(int v) {
	int i = decode(v).first, j = decode(v).second;
	color[i][j] = colors;

	for (int u = first[v]; u != 0; u = next[u]) {
		int newi = decode(jj[u]).first, newj = decode(jj[u]).second;
		if (color[newi][newj] == 0) {
			secondDFS(jj[u]);
		}
	}
}

int main() {
	freopen(TASK ".in", "rt", stdin);
	freopen(TASK ".out", "wt", stdout);

	scanf("%d\n", &T);

	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d:\n", cs);

		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				scanf("%d", &a[i][j]);
			}
		}

		es = 0;
		colors = 0;
		memset(mark, 0, sizeof(mark));
		memset(color, 0, sizeof(color));
		memset(first, 0, sizeof(first));
		memset(next, 0, sizeof(next));
		memset(jj, 0, sizeof(jj));

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				firstDFS(code(i, j));
			}
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (color[i][j] == 0) {
					colors++;
					assert(colors <= 26);
					secondDFS(code(i, j));
				}
			}
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				printf("%c ", 'a'+color[i][j]-1);
			}
			printf("\n");
		}
	}

	return 0;
}
