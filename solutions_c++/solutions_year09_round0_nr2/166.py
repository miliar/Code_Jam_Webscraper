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

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

int mp[102][102];

int dx[4] = { 0, -1, 1, 0 };
int dy[4] = { -1, 0, 0, 1 };

void solveIt(int h, int w) {
	vector<vector<int> > wb(h+2, vector<int>(w+2, -1));
	vector<int> bsink;
	int next = 0;
	for (int oy = 1; oy <= h; oy++) for (int ox = 1; ox <= w; ox++) if (wb[oy][ox] < 0) {
		int y = oy, x = ox;
		vector<int> seen;
		while (true) {
			wb[y][x] = next;
			seen.push_back(y*128+x);
			int ny = y, nx = x, na = mp[y][x];
			for (int d = 0; d < 4; d++) if (mp[y+dy[d]][x+dx[d]] < na) {
				ny = y+dy[d];
				nx = x+dx[d];
				na = mp[ny][nx];
			}
			if (ny == y && nx == x) {
				// found a sink
				bsink.push_back(y*128+x);
				next++;
				break;
			}
			if (wb[ny][nx] >= 0) {
				// found a basin
				int b = wb[ny][nx];
				for (unsigned int i = 0; i < seen.size(); i++) {
					wb[seen[i]/128][seen[i]%128] = b;
				}
				break;
			}
			y = ny;
			x = nx;
		}
	}
	vector<char> b2c(next, 0);
	char nextc = 'a';
	for (int y = 1; y <= h; y++) {
		if (b2c[wb[y][1]] < 'a') b2c[wb[y][1]] = nextc++;
		printf("%c", b2c[wb[y][1]]);
		for (int x = 2; x <= w; x++) {
			if (b2c[wb[y][x]] < 'a') b2c[wb[y][x]] = nextc++;
			printf(" %c", b2c[wb[y][x]]);
		}
		printf("\n");
	}
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int h, w;
		scanf("%d %d", &h, &w);
		memset(mp, 0x7f, sizeof(mp));
		for (int y = 1; y <= h; y++) for (int x = 1; x <= w; x++)
			scanf("%d", &mp[y][x]);

		printf("Case #%d:\n", cn);
		solveIt(h, w);
	}
	return 0;
}

