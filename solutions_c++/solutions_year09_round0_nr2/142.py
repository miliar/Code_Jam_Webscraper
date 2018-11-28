#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

template <class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }
typedef long long LL;
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define FORU(i, a) for (int i = a; ; ++i)
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int grid[100][100];
int h, w;
char res[100][100];

int choose(int x, int y) {
	int dir = -1, best = INT_MAX;
	FOR(i, 0, 4) {
		int nx = x+d[i][0], ny = y+d[i][1];
		if (nx >= 0 && nx < h && ny >= 0 && ny < w && grid[nx][ny] < grid[x][y] && grid[nx][ny] < best) {
			dir = i;
			best = grid[nx][ny];
		}
	}
	return dir;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		cin >> h >> w;
		FOR(j, 0, h) FOR(k, 0, w) cin >> grid[j][k];
		SET(res, 0);
		char cur = 'a';
		start:
		FOR(j, 0, h) FOR(k, 0, w) {
			if (res[j][k] != 0) continue;
			res[j][k] = cur;
			vector< pair<int, int> > comp(1, make_pair(j, k));
			FORE(l, comp) {
				int x = comp[l].first, y = comp[l].second;
				int dir = choose(x, y);
				if (dir != -1) {
					int nx = x+d[dir][0], ny = y+d[dir][1];
					if (res[nx][ny] == 0) {
						res[nx][ny] = cur;
						comp.push_back(make_pair(nx, ny));
					}
				}
				FOR(m, 0, 4) {
					int px = x+d[m][0], py = y+d[m][1];
					if (px >= 0 && px < h && py >= 0 && py < w && res[px][py] == 0) {
						dir = choose(px, py);
						if (dir == -1) continue;
						int nx = px+d[dir][0], ny = py+d[dir][1];
						if (nx == x && ny == y) {
							res[px][py] = cur;
							comp.push_back(make_pair(px, py));
						}
					}
				}
			}
			++cur;
			goto start;
		}
		cout << "Case #" << i+1 << ":\n";
		FOR(j, 0, h) {
			cout << res[j][0];
			FOR(k, 1, w) cout << ' ' << res[j][k];
			cout << endl;
		}
	}
}
