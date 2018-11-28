#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

#define Eo(x) { cerr << #x << " = " << x << endl; }

typedef long long int64;
typedef double real;

typedef pair<int, int> ipair;

#define inf 0x3f3f3f3f

const int dx[4] = { 1, 0,-1, 0};
const int dy[4] = { 0, 1, 0,-1};

inline int idist(ipair a, ipair b) {
	return abs(a.first-b.first) + abs(a.second-b.second);
}

ipair operator -= (ipair& a, ipair b) {
	a.first -= b.first;
	a.second -= b.second;
	return a;
}
ipair operator += (ipair& a, ipair b) {
	a.first += b.first;
	a.second += b.second;
	return a;
}

int n;

struct figure {
	ipair a[5];

	ipair normalize() {
		int b = 0, i;
		for(i = 1; i < n; i++)
			if(a[i].first < a[b].first || (a[i].first == a[b].first && a[i].second < a[b].second))
				b = i;
		ipair g = a[b];
		for(i = 0; i < n; i++)
			a[i] -= g;
		sort(a, a+n);
		return g;
	}

	bool operator < (const figure& f) const {
		return memcmp(a, f.a, sizeof(a[0])*n) < 0;
	}
};

bool danger(const figure& f) {
	int was[5] = {0}, q[5], l, r, i, j;
	was[0] = 1; q[(r=0)++] = 0;
	for(l = 0; l < r; l++)
		for(i = 0; i < n; i++)
			if(idist(f.a[q[l]], f.a[i]) == 1 && !was[i]) {
				was[i] = 1;
				q[r++] = i;
			}
	return l < n;
}

struct state {
	ipair pos;
	figure fig;

	bool operator < (const state& st) const {
		if(pos != st.pos) return pos < st.pos;
		return fig < st.fig;
	}
};

char fld[1 << 4][1 << 4];
int r, c;

map<state, int> dist;

void depict(const state& st) {
	int i, j;
	for(i = 0; i < r; i++)
		for(j = 0; j < c; j++)
			if(fld[i][j] != '#') fld[i][j] = '.';
	for(i = 0; i < n; i++)
		fld[st.pos.first + st.fig.a[i].first][st.pos.second + st.fig.a[i].second] = 'x';
}

inline bool onb(int x, int y) {
	return x >= 0 && x < r && y >= 0 && y < c;
}

ostream& operator << (ostream& out, const state& st) {
	for(int i = 0; i < n; i++)
		out << "(" << st.pos.first + st.fig.a[i].first << "," << st.pos.second + st.fig.a[i].second << ") ";
	return out;// << endl;
}

int main() {
	int t = 1, tc, i, j, k, l;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:", t);
		scanf("%d%d", &r, &c);
		for(i = 0; i < r; i++)
			scanf(" %s", fld[i]);
		state start, end;
		int sc = 0, ec = 0;
		for(i = 0; i < r; i++)
			for(j = 0; j < c; j++) {
				if(fld[i][j] == 'o' || fld[i][j] == 'w')
					start.fig.a[sc++] = ipair(i, j);
				if(fld[i][j] == 'x' || fld[i][j] == 'w')
					end.fig.a[ec++] = ipair(i, j);
			}
		assert(sc == ec);
		n = sc;
		assert(n <= 5);
		assert(!danger(start.fig) && !danger(end.fig));
		start.pos = start.fig.normalize();
		end.pos = end.fig.normalize();
		dist.clear();
		dist[start] = 0;
		vector<state> q;
		q.push_back(start);
		Eo(t);
		for(l = 0; l < q.size() && dist.find(end) == dist.end(); l++) {
			state cur = q[l];
			int dst = dist[cur];
			//Eo(cur << ' ' << dst);
			depict(cur);
			bool dang = danger(cur.fig);
			for(i = 0; i < n; i++)
				for(k = 0; k < 4; k++) {
					int nx = cur.fig.a[i].first + cur.pos.first + dx[k], ny = cur.fig.a[i].second + cur.pos.second + dy[k];
					int px = cur.fig.a[i].first + cur.pos.first - dx[k], py = cur.fig.a[i].second + cur.pos.second - dy[k];
					if(!onb(nx, ny) || !onb(px, py)) continue;
					if(fld[nx][ny] != '.' || fld[px][py] != '.') continue;
					state next = cur;
					next.fig.a[i] = ipair(cur.fig.a[i].first+dx[k], cur.fig.a[i].second+dy[k]);
					if(dang && danger(next.fig)) continue;
					next.pos += next.fig.normalize();
					if(dist.find(next) == dist.end()) {
						dist[next] = dst + 1;
						q.push_back(next);
					}
				}
		}
		Eo(q.size());
		if(dist.find(end) == dist.end()) puts(" -1");
		else printf(" %d\n", dist[end]);
		//Eo(end << ' ' << dist[end]);
		fflush(stdout);

	}
	return 0;
}
