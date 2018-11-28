#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, R, C, N;
char tmp[20][20];
char tmp2[20][20];
char cur[20][20];
char grid[20][20];
char goal[20][20];
char start[20][20];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

struct State {
	int r, c, id;
};

bool operator<(State a, State b) {
	if (a.r == b.r) {
		if (a.c == b.c) return a.id < b.id;
		return a.c < b.c;
	}
	return a.r < b.r;
}

State getState() {
	State res;
	res.r = res.c = oo;
	res.id = 0;
	FOR(i, 0, R) FOR(j, 0, C) {
		if (cur[i][j] == 'x') {
			res.r = min(res.r, i);
			res.c = min(res.c, j);
		}
	}
	FOR(i, 0, 5) FOR(j, 0, 5) {
		int r = res.r + i, c = res.c + j;
		if (r < 0 || r >= R || c < 0 || c >= C) continue;
		if (cur[r][c] != 'x') continue;
		res.id |= (1 << (5*i+j));
	}
	return res;
}

void setState(State s) {
	FOR(i, 0, R) FOR(j, 0, C) cur[i][j] = grid[i][j];
	FOR(i, 0, 25) {
		if (s.id & (1 << i)) {
			int r = s.r + i/5, c = s.c + i%5;
			cur[r][c] = 'x';
		}
	}
}

map<State, int> dist;
set<pair<int, State> > q;

bool isend() {
	FOR(i, 0, R) FOR(j, 0, C) {
		if (cur[i][j] != goal[i][j]) return false;
	}
	return true;
}

void update(int d) {
	State s = getState();
	if (dist.find(s) == dist.end()) {
		dist[s] = d;
		q.insert(make_pair(d, s));
	} else {
		int dd = dist[s];
		if (d < dd) {
			q.erase(q.find(make_pair(dd, s)));
			dist[s] = d;
			q.insert(make_pair(d, s));
		}
	}
}

bool mark[20][20];
int num;

void dfs(int r, int c) {
	if (r < 0 || r >= R || c < 0 || c >= C) return;
	if (mark[r][c] || cur[r][c] != 'x') return;
	num++;
	mark[r][c] = true;
	FOR(d, 0, 4) {
		int rr = r + dx[d], cc = c + dy[d];
		dfs(rr, cc);
	}
}

bool connected(int r, int c) {
	memset(mark, 0, sizeof(mark));
	num = 0;
	dfs(r, c);
	return num == N;
}

void try_move2(int r, int c, int d, int olddist) {
	if (cur[r][c] != '.') return;
	int rr = r + dx[d], cc = c + dy[d];
	if (rr < 0 || rr >= R || cc < 0 || cc >= C) return;
	if (cur[rr][cc] != 'x') return;
	int rrr = rr + dx[d], ccc = cc + dy[d];
	if (rrr < 0 || rrr >= R || ccc < 0 || ccc >= C) return;
	if (cur[rrr][ccc] != '.') return;
	FOR(i, 0, R) FOR(j, 0, C) tmp2[i][j] = cur[i][j];
	cur[rr][cc] = '.';
	cur[rrr][ccc] = 'x';
	if (connected(rrr, ccc)) update(olddist + 1);
	FOR(i, 0, R) FOR(j, 0, C) cur[i][j] = tmp2[i][j];
}

void do_check(int r, int c, int ds) {
	if (connected(r, c)) {
		update(ds);
	} else {
		FOR(i, 0, R) FOR(j, 0, C) FOR(d, 0, 4) {
			try_move2(i, j, d, ds);
		}
	}
}

void try_move(int r, int c, int d, int olddist) {
	if (cur[r][c] != '.') return;
	int rr = r + dx[d], cc = c + dy[d];
	if (rr < 0 || rr >= R || cc < 0 || cc >= C) return;
	if (cur[rr][cc] != 'x') return;
	int rrr = rr + dx[d], ccc = cc + dy[d];
	if (rrr < 0 || rrr >= R || ccc < 0 || ccc >= C) return;
	if (cur[rrr][ccc] != '.') return;
	FOR(i, 0, R) FOR(j, 0, C) tmp[i][j] = cur[i][j];
	cur[rr][cc] = '.';
	cur[rrr][ccc] = 'x';
	do_check(rrr, ccc, olddist + 1);
	FOR(i, 0, R) FOR(j, 0, C) cur[i][j] = tmp[i][j];
}

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> R >> C;
		string row;
		FOR(i, 0, R) {
			cin >> row;
			FOR(j, 0, C) {
				if (row[j] == '#' || row[j] == '.') {
					start[i][j] = goal[i][j] = grid[i][j] = row[j];
				} else if (row[j] == 'x') {
					start[i][j] = grid[i][j] = '.';
					goal[i][j] = 'x';
				} else if (row[j] == 'o') {
					start[i][j] = 'x';
					grid[i][j] = goal[i][j] = '.';
				} else {
					start[i][j] = goal[i][j] = 'x';
					grid[i][j] = '.';
				}
			}
		}
		FOR(i, 0, R) FOR(j, 0, C) cur[i][j] = start[i][j];
		N = 0;
		FOR(i, 0, R) FOR(j, 0, C) if (cur[i][j] == 'x') N++;
		State s = getState();
		dist.clear();
		dist[s] = 0;
		q.clear();
		q.insert(make_pair(0, s));
		while (!q.empty()) {
			int ds = q.begin()->first;
			s = q.begin()->second;
			q.erase(q.begin());
			setState(s);
			if (isend()) {
				cout << "Case #" << cs << ": " << ds << endl;
				goto end;
			}
			FOR(i, 0, R) FOR(j, 0, C) FOR(d, 0, 4) {
				try_move(i, j, d, ds);
			}
		}
		cout << "Case #" << cs << ": -1" << endl;
end:	;
	}
	return 0;
}
