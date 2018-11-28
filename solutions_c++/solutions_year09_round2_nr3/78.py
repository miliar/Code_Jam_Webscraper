#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <string>
#include <vector>
#include <queue>
#define FOR(i,n) for (int i = 0; i < (int) (n); i++)
using namespace std;

int w, q;

char table[32][32];
string solutions[256];

#define MAXSUM 480

const int dir[4][2] = { { -1, 0 }, { 1, 0}, {0, -1}, {0, 1} };
/*
void bt(int val, int x, int y, int len);

void fs(int val, int x, int y, int len)
{
	pair<int, int> temp[4];
	int c = 0;
	FOR(d, 4) {
		int nx = x + dir[d][0];
		int ny = y + dir[d][1];
		if (nx >= 0 && nx < w && ny >= 0 && ny < w && isdigit(table[ny][nx])) {
			temp[c++] = make_pair(table[ny][nx] - '0', d);
		}
	}
	sort(temp, temp + c);
	FOR(k, c) {
		int d = temp[k].second;
		int nx = x + dir[d][0];
		int ny = y + dir[d][1];
		build[len] = table[ny][nx];
		build[len + 1] = 0;
		bt(val + table[ny][nx] - '0', nx, ny, len + 1);
	}
}

void bt(int val, int x, int y, int len)
{
	if (val > MAXSUM || val < -MAXSUM) return;
	string& dp = done[val + MAXSUM][x][y];
	if (dp != "NULL" && ((int) dp.length() < len || (dp.length() == len && dp <= build))) return;
	dp = build;
	if (1 <= val && val <= 250) {
		string& o = solutions[val];
		if (len <= 5) printf("%s: trying to optimize %s...", build, o.c_str());
		if (o == "NULL" || (int) o.length() > len || ((int) o.length() == len && o > build)) {
			o = build;
			if (len <= 5) printf("success");
		}
		if (len <= 5) printf("\n");
	}
	const char WS[3] = "+-";
	FOR(wws, 2) {
		FOR(d, 4) {
			int nx = x + dir[d][0];
			int ny = y + dir[d][1];
			if (nx >= 0 && nx < w && ny >= 0 && ny < w && table[ny][nx] == WS[wws]) {
				build[len] = table[ny][nx];
				build[len+1] = 0;
				fs(val, nx, ny, len+1);
			}
		}
	}
}*/

int done[2*MAXSUM+1][20][20];

struct State {
	int val, x, y;
	string s;
	State() {}
	State(int vval, int vx, int vy, const string& vs)
	{
		val = vval;
		x = vx;
		y = vy;
		s = vs;
	}
};

int sign(char c) { return c == '+' ? +1 : -1; }

bool inrange(int x, int y) { return x >= 0 && x < w && y >= 0 && y < w; }

vector<int> queries;

void solve(void)
{
	vector<State> q, qn;
	FOR(i, 256) solutions[i] = "NULL";
	FOR(y, w) FOR(x, w) if (isdigit(table[y][x])) {
		char temp[2] = "0";
		temp[0] = table[y][x];
		q.push_back(State(table[y][x] - '0', x, y, temp));
	}
	while (1) {
		qn.clear();
		memset(done, 0xff, sizeof(done));
		for (int ii = 0; ii < (int) q.size(); ii++) {
			State st = q[ii];
			if (st.val >= 1 && st.val <= 250) {
				string& o = solutions[st.val];
				if (o == "NULL")
					o = st.s;
				else if (o.length() == st.s.length() && st.s < o) o = st.s;
			}
			FOR(dd, 16) {
				int d0 = dd / 4;
				int d1 = dd % 4;
				int nx = st.x + dir[d0][0];
				int ny = st.y + dir[d0][1];
				if (!inrange(nx, ny) || isdigit(table[ny][nx])) continue;
				int nnx = nx + dir[d1][0];
				int nny = ny + dir[d1][1];
				if (!inrange(nnx, nny) || !isdigit(table[nny][nnx])) continue;
				int nv = st.val + sign(table[ny][nx]) * (table[nny][nnx] - '0');
				if (nv < -MAXSUM || nv > MAXSUM) continue;
				State ns;
				ns.val = nv;
				ns.x = nnx;
				ns.y = nny;
				ns.s = (st.s + table[ny][nx]) + table[nny][nnx];
				int& xd = done[ns.val+MAXSUM][ns.y][ns.x];
				if (xd != -1) {
					State& other = qn[xd];
					if (other.s > ns.s) other.s = ns.s;
					continue;
				} else {
					xd = (int) qn.size();
					qn.push_back(ns);
				}
			}
		}
		//printf("---------\n");
		if (qn.empty()) break;
		int nonQueryable = 0;
		FOR(i, queries.size()) if (solutions[queries[i]] == "NULL") nonQueryable++;
		if (!nonQueryable) break;
		q = qn;
	}
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		printf("Case #%d:\n", tc + 1);
		scanf("%d%d", &w, &q);
		for (int i = 0; i < w; i++) {
			scanf("%s", table[i]);
		}
		queries.clear();
		for (int i = 0; i < q; i++) {
			int x;
			scanf("%d", &x);
			queries.push_back(x);
		}
		solve();
		FOR(i, q)
			printf("%s\n", solutions[queries[i]].c_str());
	}
	return 0;
}
