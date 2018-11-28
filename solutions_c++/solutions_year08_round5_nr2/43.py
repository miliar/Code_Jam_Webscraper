#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <deque>

using namespace std;

const int dd[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

const int MAXN = 64 * 64 * 64;

char s[100][100];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		map<vector<int>, int> d;
		deque<vector<int> > q;
		int n, m; scanf("%d %d", &n, &m);
		int sx = 0, sy = 0, tx = 0, ty = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%s", s[i]);
			for (int j = 0; j < m; ++j) {
				if (s[i][j] == 'O') {
					s[i][j] = '.';
					sx = i, sy = j;
				} else if (s[i][j] == 'X') {
					s[i][j] = '.';
					tx = i, ty = j;
				}
			}
		}
		vector<int> v;
		v.push_back((sx << 3) + sy);
		v.push_back(-1);
		v.push_back(-1);
		q.push_back(v);
		d[v] = 0;
		int result = -1;
		while (q.size()) {
			vector<int> v = *q.begin();
			q.pop_front();
			if (v[0] == (tx << 3) + ty) {
				result = d[v];
				break;
			}
			int r = d[v];
			int x, y, x1, y1, x2, y2;
			x = v[0] >> 3; y = v[0] & 7;
			if (v[1] == -1) {
				x1 = y1 = -1;
			} else {
				x1 = v[1] >> 3; y1 = v[1] & 7;
			}
			if (v[2] == -1) {
				x2 = y2 = -1;
			} else {
				x2 = v[2] >> 3; y2 = v[2] & 7;
			}
			for (int i = 0; i < 4; ++i) {
				int xx = x + dd[i][0], yy = y + dd[i][1];
				if ((xx >= 0) && (yy >= 0) && (xx < n) && (yy < m) && (s[xx][yy] != '#')) {
					v[0] = (xx << 3) + yy;
					if (d.find(v) == d.end()) {
						d[v] = r + 1;
						q.push_back(v);
					}
					v[0] = (x << 3) + y;
				}
				xx = x, yy = y;
				while ((xx >= 0) && (yy >= 0) && (xx < n) && (yy < m) && (s[xx][yy] != '#')) {
					xx += dd[i][0], yy += dd[i][1];
				}
				xx -= dd[i][0], yy -= dd[i][1];
				v[1] = (xx << 3) + yy;
				if (d.find(v) == d.end()) {
					d[v] = r;
					q.push_front(v);
				}
				if (x1 == -1) v[1] = -1;
				else v[1] = ((x1 << 3) + y1);
				v[2] = ((xx << 3) + yy);
				if (d.find(v) == d.end()) {
					d[v] = r;
					q.push_front(v);
				}
				if (x2 == -1) v[2] = -1;
				else v[2] = ((x2 << 3) + y2);
			}
			if ((x1 != -1) && (x2 != -1)) {
//			cout << x << " " << y << " " << x1 << " "<< y1 << " " << x2 << " " << y2 << " " << r << endl;
				if ((x == x1) && (y == y1)) {
					v[0] = (x2 << 3) + y2;
					if (d.find(v) == d.end()) {
						d[v] = r + 1;
						q.push_back(v);
					}
				}
				if ((x == x2) && (y == y2)) {
					v[0] = (x1 << 3) + y1;
					if (d.find(v) == d.end()) {
						d[v] = r + 1;
						q.push_back(v);
					}
				}
			}
		}
		printf("Case #%d: ", tt + 1);
		if (result == -1) printf("THE CAKE IS A LIE\n");
		else printf("%d\n", result);
	}
	return 0;
}
