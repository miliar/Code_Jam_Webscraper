#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
using namespace std;
#pragma comment(linker, "/STACK:16777216")
#define inf 1000000000
#define ll long long
#define eps 1e-9
#define VI vector<int>
#define pb push_back
#define L(s) (int)((s).size())
#define all(s) (s).begin(), (s).end()
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
int dx[] = {0, 1, 1, 0, -1, -1};
int dy[] = {1, 1, 0, -1, -1, 0};
const int lim = 6006;
int f[lim][lim];	
pii p[lim][lim];
int state[lim][lim];
int can[lim][lim];
int t, s, m;
pii moves[11111];
void dfs_can(int i, int j) {
	can[i][j] = 1;
	for(int w = 0; w < 6; ++w) {
		int ni = i + dx[w];
		int nj = j + dy[w];
		if (can[ni][nj] == 0) dfs_can(ni, nj);
	}
}
bool dfs_ring(int i, int j, int when) {
	can[i][j] = 2;
	bool ans = 1;
	for(int w = 0; w < 6; ++w) {
		int ni = i + dx[w];
		int nj = j + dy[w];
		if (can[ni][nj] == -1) { ans = 0; continue; }
		if (can[ni][nj] == 2) continue;
		if (f[ni][nj]  == 0 || f[ni][nj] > when) {
			ans &= dfs_ring(ni, nj, when);
		}
	}
	return ans;
}
inline bool exists_ring(int when) {
	for(int i = 1; i < 2 * s; ++i)
		for(int j = 1; j < 2 * s; ++j)
			if (can[i][j] == 2) can[i][j] = 1;
	for(int i = 1; i < 2 * s; ++i)
		for(int j = 1; j < 2 * s; ++j)
			if (can[i][j] == 1 && (f[i][j] == 0 || f[i][j] > when)) {
				if (dfs_ring(i, j, when)) return 1;
			}
	return 0;
}
pii P(int x, int y) { if (p[x][y].x == x && p[x][y].y == y) return mp(x, y); else return p[x][y] = P(p[x][y].x, p[x][y].y); }
inline void U(pii x, pii y) {
	x = P(x.x, x.y);
	y = P(y.x, y.y);
	if (rand() % 2) {
		p[x.x][x.y] = y;
		f[y.x][y.y] |= f[x.x][x.y];
	}  else {
		p[y.x][y.y] = x;
		f[x.x][x.y] |= f[y.x][y.y];
	}
}
int dfs_fork(int i, int j, int when) {
	int ans = state[i][j];
	can[i][j] = 2;
	for(int w = 0; w < 6; ++w) {
		int ni = i + dx[w];
		int nj = j + dy[w];
		if (can[ni][nj] != 1) continue;
		if (f[ni][nj]   && f[ni][nj] <= when) {
			ans |= dfs_fork(ni, nj, when);
		}
	}
	return ans;
}
inline bool exists_fork(int when) {
	for(int i = 1; i < 2 * s; ++i)
		for(int j = 1; j < 2 * s; ++j)
			if (can[i][j] == 2) can[i][j] = 1;
	for(int i = 1; i < 2 * s; ++i)
		for(int j = 1; j < 2 * s; ++j)
			if (can[i][j] == 1 && f[i][j] && f[i][j] <= when) {
				int val = dfs_fork(i, j, when);
				int bits = 0;
				for(int w = 0; w < 6; ++w) if (val & (1 << w)) ++bits;
				if (bits >= 3) return 1;
			}
	return 0;
}
inline bool exists_bridge(int when) {
	for(int i = 1; i < 2 * s; ++i)
		for(int j = 1; j < 2 * s; ++j)
			if (can[i][j] == 2) can[i][j] = 1;
	for(int i = 1; i < 2 * s; ++i)
		for(int j = 1; j < 2 * s; ++j)
			if (can[i][j] == 1 && f[i][j] && f[i][j] <= when) {
				int val = dfs_fork(i, j, when);
				int bits = 0;
				for(int w = 0; w < 6; ++w) if (val & (1 << (w + 6))) ++bits;
				if (bits >= 2) return 1;
			}
	return 0;
}
int main() {
	freopen("B-small-attempt3.in", "r", stdin);
//	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tn = 1; tn <= t; ++tn) {
		cerr << tn << endl;
		memset(f, 0, sizeof(f));
		memset(state, 0, sizeof(state));
		memset(can, 0, sizeof(can));
		cin >> s >> m;
	//	cerr << s << " " << m << endl;
		pii cur = mp(1, 1);
		for(int i = 0; i < 6; ++i) {
			state[cur.x][cur.y] |= (1 << (6 + i));
			can[cur.x + dx[(i + 4) % 6]][cur.y + dy[(i + 4) % 6]] = -1;
			can[cur.x + dx[(i + 5) % 6]][cur.y + dy[(i + 5) % 6]] = -1;
			for(int j = 0; j < s - 1; ++j) {
				cur.x += dx[i];
				cur.y += dy[i];
				if (j < s - 2) state[cur.x][cur.y] |= (1 << (i));
				can[cur.x + dx[(i + 5) % 6]][cur.y + dy[(i + 5) % 6]] = -1;
			}
		}
		dfs_can(1, 1);
		for(int i = 0; i < m; ++i) {
			cin >> moves[i].x >> moves[i].y;
			f[moves[i].x][moves[i].y] = i + 1;
		}
		int ring_time = inf, fork_time = inf, bridge_time = inf;
		for(int i = 1; i <= m; ++i) if (exists_ring(i)) { ring_time = i; break; }
		for(int i = 1; i <= m; ++i) if (exists_fork(i)) { fork_time = i; break; }
		for(int i = 1; i <= m; ++i) if (exists_bridge(i)) { bridge_time = i; break; }

	/*	for(int i = 0; i < 2 * s; ++i)
			for(int j = 0; j < 2 * s; ++j) {
				if (can[i][j] == 2) can[i][j] = 1;
				f[i][j] = 0;
				p[i][j] = mp(i, j);
			}
		int bridge_time = inf;
		int fork_time = inf;
		for(int i = 0; i < m; ++i) {
			f[moves[i].x][moves[i].y] = state[moves[i].x][moves[i].y];
			can[moves[i].x][moves[i].y] = 2;
			for(int w = 0; w < 6; ++w) {
				int ni = moves[i].x + dx[w];
				int nj = moves[i].y + dy[w];
				if (can[ni][nj] != 2) continue;
				if (P(moves[i].x, moves[i].y) != P(ni, nj)) {
					U(moves[i], mp(ni, nj));
				}
			}
			int low_cnt = 0, high_cnt = 0;
			for(int w = 0; w < 6; ++w) {
				pii cur = P(moves[i].x, moves[i].y);
				if (f[cur.x][cur.y] & (1 << w)) low_cnt++;
				if (f[cur.x][cur.y] & (1 << (w + 6))) high_cnt++;
			}
			if (low_cnt >= 3) fork_time = min(fork_time, i + 1);
			if (high_cnt >= 2) bridge_time = min(bridge_time, i + 1);
		}*/
		int when = min(min(ring_time, fork_time), bridge_time);
		cerr << ring_time << " " << bridge_time << " " << fork_time << endl;
		cout << "Case #" << tn << ": ";
		if (when == inf) cout << "none\n"; else
		if (when == ring_time && when == bridge_time && when == fork_time) cout << "bridge-fork-ring in move " << when << endl; else
			if (when == ring_time && when == bridge_time) cout << "bridge-ring in move " << when << endl; else
				if (when == ring_time && when == fork_time) cout << "fork-ring in move " << when << endl; else
					if (when == bridge_time && when == fork_time) cout << "bridge-fork in move " << when << endl; else
						if (when == ring_time) cout << "ring in move " << when << endl; else
							if (when == bridge_time) cout << "bridge in move " << when << endl; else
								if (when == fork_time) cout << "fork in move " << when << endl; else {
									cerr << "ERROR\n";
								}
	}
}