#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <bitset>
#include <limits>
#include <iterator>
#include <sstream>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i != _b; ++i)
#define REP(i, N) FOR(i, 0, N)
#define REPK(K) REP(_crazyName, K)

#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()

template<typename CType, typename VType>
inline void REMOVE(CType &container, const VType &value) {
	container.erase(remove(ALL(container), value), container.end());
}

#define sz() size()
#define len() length()
#define mp(a, b) make_pair(a, b)
#define pb(x) push_back(x)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef long long LL;

const int dx[] = { -1, 0, 0, 1 },
		dy[] = { 0, -1, 1, 0 };

#define ok1(x, y) (x) >= 0 && (x) < H && (y) >= 0 && (y) < W

int H, W;

int calc(const VVI &grid, VVI &result, int x, int y) {
	if (result[x][y] != -1) return result[x][y];

	int bestX = -1, bestY = -1;
	REP (i, 4) {
		int x1 = x + dx[i], y1 = y + dy[i];
		if (ok1(x1, y1)) {
			if ((bestX == -1 && grid[x1][y1] < grid[x][y]) || (bestX != -1 && grid[x1][y1] < grid[bestX][bestY])) {
				bestX = x1;
				bestY = y1;
			}
		}
	}

	return result[x][y] = calc(grid, result, bestX, bestY);
}

int main() {
	int T, kase;
	scanf("%d", &T);

	FOR (kase, 1, T + 1) {
		scanf("%d %d", &H, &W);

		VVI grid(H, VI(W));
		REP (i, H)
			REP (j, W)
				scanf("%d", &grid[i][j]);

		VVI result(H, VI(W, -1));
		int sinkId = 0;
		REP (i, H) {
			REP (j, W) {
				bool isSink = true;
				REP (k, 4) {
					int x1 = i + dx[k], y1 = j + dy[k];
					if (ok1(x1, y1) && grid[x1][y1] < grid[i][j]) {
						isSink = false;
						break;
					}
				}

				if (isSink) {
					result[i][j] = ++sinkId;
				}
			}
		}

		REP (i, result.sz())
			REP (j, result[i].sz())
				if (result[i][j] == -1)
					calc(grid, result, i, j);

		printf("Case #%d:\n", kase);
		vector<char> seen(sinkId + 1, '-');
		char basinId = 'a';
		REP (i, result.sz()) {
			REP (j, result[i].sz()) {
				if (seen[result[i][j]] == '-') {
					seen[result[i][j]] = basinId++;
				}

				if (j)
					printf(" ");
				printf("%c", seen[result[i][j]]);
			}
			printf("\n");
		}
	}
}

