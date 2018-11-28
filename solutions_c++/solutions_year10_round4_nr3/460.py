#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>

#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

struct Rec {
	int x1, x2, y1, y2;
};
vector<Rec> recs;

vector<int> F;

int f(int v) {
	if (F[v] != -1) return F[v];
	int curX = recs[v].x1;
	int curY = recs[v].y1;

	F[v] = 0;

	for (int i = 0; i < recs.size(); ++i) {
		if (i != v && recs[i].x1 <= curX && curX <= recs[i].x2
			&& recs[i].y1 <= curY && curY <= recs[i].y2) {
	
				int dx = curX - recs[i].x1;
				int dy = curY - recs[i].y1;
				if (dx + dy > 0) {
					int t = f(i) + dx + dy;
					F[v] = max(F[v], t);
				}
		}
	}
	return F[v];
}

bool intersect(int l1, int r1, int l2, int r2) {
	if (max(l1, r1) < min(l2, r2)) return false;
	if (max(l2, r2) < min(l1, r1)) return false;
	return true;
}

bool intersect(int i, int j) {
	bool x = intersect(recs[i].x1, recs[i].x2, recs[j].x1, recs[j].x2);
	bool y = intersect(recs[i].y1, recs[i].y2, recs[j].y1, recs[j].y2);
	return x && y;
}

void dfs(int v, int c, vector<int> &comps) {
	comps[v] = c;
	for (int i = 0; i < recs.size(); ++i) {
		if (comps[i] == -1 && intersect(v, i)) {
			dfs(i, c, comps);
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int r;
		cin >> r;
		recs.resize(r);
		F = vector<int>(r, -1);
		for (int i = 0; i < r; ++i) {
			cin >> recs[i].x1 >> recs[i].y1 >> recs[i].x2 >> recs[i].y2;
			recs[i].x1--;
			recs[i].y1--;
		}

		vector<int> comps(r, -1);
		int cc = 0;
		for (int i = 0; i < r; ++i) {
			if (comps[i] == -1) {
				dfs(i, cc++, comps);
			}
		}

		vector<int> cx(cc, -1);
		vector<int> cy(cc, -1);

		for (int i = 0; i < r; ++i) {
			cx[comps[i]] = max(cx[comps[i]], recs[i].x2);
			cy[comps[i]] = max(cy[comps[i]], recs[i].y2);
		}

		int res = 0;
		for (int i = 0; i < r; ++i) {
			int t = f(i) + cx[comps[i]] - recs[i].x1 + cy[comps[i]] - recs[i].y1 - 1;
			res = max(res, t);
		}

		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}
