#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;
string readLine();
int readIntLine();
vector<int> readVI(int n);
vector<string> readVS(int n);
vector<int> itokens(string s, string sep);
vector<string> stokens(string s, string sep);

int dy[] = { 0, 1, 0 };
int dx[] = { -1, 0, 1 };

struct Point {
	Point() {}
	Point(int i, int j) { x = i; y = j; }
	bool operator==(const Point &p) const { return p.x == x && p.y == y; }
	bool operator<(const Point &p) const { return p.y < y ? true : p.x < x; }
	int x, y;
};

vector<Point> flood(vector<string> &b, int sy, int sx) {
	vector<Point> ps;
	queue<int> q;
	q.push(sy*64+sx);
	ps.push_back(Point(sx, sy));
	b[sy][sx] = ',';
	while (!q.empty()) {
		int y = q.front()/64, x = q.front()%64;
		q.pop();
		for (int d = 0; d < 3; d++) {
			int ny = y-dy[d], nx = x+dx[d];
			if (b[ny][nx] == '.') {
				q.push(ny*64+nx);
				ps.push_back(Point(nx, ny));
				b[ny][nx] = ',';
			}
		}
	}
	return ps;
}

void reduce(vector<Point> &p, Point &t, vector<string> &b) {
	int W = b[0].size();
	int xy = 0, ny = 64;
	for (int i = 0; i < p.size(); i++) {
		if (p[i].y < ny) ny = p[i].y;
		if (p[i].y > xy) xy = p[i].y;
	}
//	printf("Start %d points\n", p.size());
	while (p.size() > 1) {
//		printf("pass start %d\n", p.size());
		int tct = p.size();
		for (int i = 0; i < W; i++) {
			bool ok = true;
			for (int j = 0; j < p.size(); j++) {
				if (b[p[j].y][p[j].x-1] == '.') {
					ok = false;
					break;
				}
			}
			if (!ok) break;
			int ct = 0;
			for (int j = 0; j < p.size(); j++) {
				if (b[p[j].y][p[j].x-1] != '#') {
					p[j].x--;
					ct++;
				}
			}
			if (!ct) break;
		}
		sort(p.begin(), p.end());
		p.erase(unique(p.begin(), p.end()), p.end());
//		printf(" left %d\n", p.size());

		for (int i = 0; i < W; i++) {
			bool ok = true;
			for (int j = 0; j < p.size(); j++) {
				if (b[p[j].y][p[j].x+1] == '.') {
					ok = false;
					break;
				}
			}
			if (!ok) break;
			int ct = 0;
			for (int j = 0; j < p.size(); j++) {
				if (b[p[j].y][p[j].x+1] != '#') {
					p[j].x++;
					ct++;
				}
			}
			if (!ct) break;
		}
		sort(p.begin(), p.end());
		p.erase(unique(p.begin(), p.end()), p.end());
//		printf(" right %d\n", p.size());

		// horizontal compression done.  Look for method to drop
		bool okd = false;
		for (int i = 0; i < W; i++) {
			bool ok = true; okd = true;
			int ctd = 0;
			for (int j = 0; j < p.size(); j++) {
				if (b[p[j].y+1][p[j].x] == '.') okd = false;
				else if (b[p[j].y+1][p[j].x] == ',') ctd++;
				if (b[p[j].y][p[j].x-1] == '.') ok = false;
			}
			if (!ctd) okd = false;
//			printf(" at left %d, okd %d, ok %d\n", i, okd?1:0, ok?1:0);
			if (okd) break;
			if (!ok) break;
			int ct = 0;
			for (int j = 0; j < p.size(); j++) {
				if (b[p[j].y][p[j].x-1] != '#') {
					p[j].x--;
					ct++;
				}
			}
			if (!ct) break;
		}

		if (!okd) {
			for (int i = 0; i < W; i++) {
				bool ok = true; okd = true;
				int ctd = 0;
				for (int j = 0; j < p.size(); j++) {
					if (b[p[j].y+1][p[j].x] == '.') okd = false;
					else if (b[p[j].y+1][p[j].x] == ',') ctd++;
					if (b[p[j].y][p[j].x+1] == '.') ok = false;
				}
				if (!ctd) okd = false;
//				printf(" at right %d, okd %d, ok %d\n", i, okd?1:0, ok?1:0);
				if (okd) break;
				if (!ok) break;
				int ct = 0;
				for (int j = 0; j < p.size(); j++) {
					if (b[p[j].y][p[j].x+1] != '#') {
						p[j].x++;
						ct++;
					}
				}
				if (!ct) break;
			}
		}

		if (!okd) break;
		for (int i = 0; i < p.size(); i++) {
			if (b[p[i].y+1][p[i].x] != '#')
				p[i].y++;
		}
		sort(p.begin(), p.end());
		p.erase(unique(p.begin(), p.end()), p.end());
//		printf(" down %d\n", p.size());
	}
//	printf(" done\n");
}

void doCave(char c, vector<string> b) {
	int sy, sx, R = b.size(), C = b[0].size();
	for (int y = 1; y+1 < R; y++) for (int x = 1; x+1 < C; x++) {
		if (b[y][x] == c) {
			sy = y;
			sx = x;
		}
		if (b[y][x] >= '0') {
			b[y][x] = '.';
		}
	}
	vector<Point> ps = flood(b, sy, sx);
//	for (int i = 0; i < R; i++) printf("%s\n", b[i].c_str());
	int ct = ps.size();
	Point t(sx, sy);
	reduce(ps, t, b);
	printf("%c: %d %s\n", c, ct, ps.size() == 1 ? "Lucky" : "Unlucky");
}

int solveIt(int R, int C, vector<string> &b) {
	int N = 0;
	for (int y = 1; y+1 < R; y++) for (int x = 1; x+1 < C; x++)
		if (b[y][x]-'0' > N) N = b[y][x]-'0';
	N++;
	for (int i = 0; i < N; i++) doCave(i+'0', b);

	return 0;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int R, C;
		scanf("%d %d ", &R, &C);
		vector<string> b = readVS(R);

		printf("Case #%d:\n", cn);
		solveIt(R, C, b);
	}
	return 0;
}








string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}
int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}
vector<int> readVI(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}
vector<string> readVS(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<string> v(n);
	for (int i = 0; i < n; i++) v[i] = readLine();
	return v;
}
vector<string> stokens(string s, string sep = " \n\r\t") {
	vector<string> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep = " \n\r\t") {
	vector<int> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}

