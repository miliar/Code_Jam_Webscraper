#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef pair<int, int> P;

struct state {
	P ps[5];
	int size, d;
	state() {
		size = 0;
		d = 0;
	}
	void norm() {
		sort(ps, ps + size);
	}
	bool connect() {
		int used[5] = {0};
		queue<int> que;
		que.push(0);
		used[0] = 1;
		int n = 1;
		while(que.size()) {
			int p = que.front(); que.pop();
			for(int i = 0; i < size; ++i) if(!used[i] && abs(ps[p].first - ps[i].first) + abs(ps[p].second - ps[i].second) == 1) {
				que.push(i);
				used[i] = 1;
				++n;
			}
		}
		return n == size;
	}
	int operator <(const state& st) const {
		for(int i = 0; i < size; ++i) if(ps[i] != st.ps[i]) return less<P>()(ps[i], st.ps[i]);
		return 0;
	}
};

char m[20][20];
int dir[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

bool ok(const P& p, int r, int c) {
	if(p.first < 0 || p.second < 0 || p.first >= r || p.second >= c) return false;
	if(m[p.first][p.second] == '#') return false;
	return true;
}

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		int r, c;
		cin >> r >> c;
		for(int i = 0; i < r; ++i) cin >> m[i];
		set<state> used;
		state init, end;
		for(int i = 0; i < r; ++i) {
			for(int j = 0; j < c; ++j) {
				if(m[i][j] == 'o') {
					init.ps[init.size++] = P(i, j);
					m[i][j] = '.';
				}else if(m[i][j] == 'x') {
					end.ps[end.size++] = P(i, j);
					m[i][j] = '.';
				}else if(m[i][j] == 'w') {
					init.ps[init.size++] = P(i, j);
					end.ps[end.size++] = P(i, j);
					m[i][j] = '.';
				}
			}
		}
		init.norm(); end.norm();
		queue<state> que;
		que.push(init);
		used.insert(init);
		int res = -1;
		while(que.size()) {
			state st = que.front(); que.pop();
			if(!(st < end) && !(end < st)) {
				res = st.d;
				break;
			}
			bool con = st.connect();
			for(int i = 0; i < st.size; ++i) {
				for(int j = 0; j < 4; ++j) {
					state next = st;
					next.ps[i] = P(st.ps[i].first + dir[j][0], st.ps[i].second + dir[j][1]);
					P pp = P(st.ps[i].first - dir[j][0], st.ps[i].second - dir[j][1]);
					if(!ok(next.ps[i], r, c) || !ok(pp, r, c)) continue;
					if(!con && !next.connect()) continue;
					bool o = true;
					for(int k = 0; k < st.size; ++k) if(i != k && next.ps[i] == next.ps[k]) o = false;
					for(int k = 0; k < st.size; ++k) if(pp == next.ps[k]) o = false;
					if(!o) continue;
					next.norm();
					if(!used.insert(next).second) continue;
					++next.d;
					que.push(next);
				}
			}
		}
		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}
