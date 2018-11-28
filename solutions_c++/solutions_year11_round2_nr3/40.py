#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <utility>

using namespace std;

struct Comparator {
	int origin;

	Comparator(int origin): origin(origin) {}

	bool operator()(int p, int q) {
		assert(p != origin);
		assert(q != origin);
		if (p < origin && q < origin) return p > q;
		if (p > origin && q > origin) return p > q;
		return p < origin;
	}
};

void dfs(const vector<vector<int> > &faces, int node, int numColors, int &best, vector<int> &how, vector<int> &curColoring, int n) {
	if (node == n) {
		bool ok = true;
		for (int i = 0; i < (int)faces.size(); i++) {
			set<int> clr;
			for (int j = 0; j < (int)faces[i].size(); j++) {
				clr.insert(curColoring[faces[i][j]]);
			}
			if ((int)clr.size() != numColors) {
				ok = false;
				break;
			}
		}
		if (!ok) return;
		if (numColors > best) {
			best = numColors;
			how = curColoring;
		}
		return;
	}
	for (int i = 1; i <= numColors + 1; i++) {
		curColoring[node] = i;
		dfs(faces, node + 1, max(numColors, i), best, how, curColoring, n);
	}
}

void solve(int it) {
	int n, m;
	cin >> n >> m;
	vector<vector<int> > e(n);
	vector<int> u(m), v(m);
	for (int i = 0; i < m; i++) {
		cin >> u[i];
		u[i]--;
	}
	for (int i = 0; i < m; i++) {
		cin >> v[i];
		v[i]--;
	}
	for (int i = 0; i < m; i++) {
		e[u[i]].push_back(v[i]);
		e[v[i]].push_back(u[i]);
	}
	for (int i = 0; i < n; i++) {
		int u = i, v = (i + 1) % n;
		e[u].push_back(v);
		e[v].push_back(u);
	}
	for (int i = 0; i < n; i++) {
		sort(e[i].begin(), e[i].end(), Comparator(i));
	}
	set<pair<int, int> > was;
	vector<vector<int> > faces;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < (int)e[i].size(); j++) {
			pair<int, int> sp(i, e[i][j]);
			if (was.count(sp)) continue;
			pair<int, int> cp(sp);
			vector<int> face;
			do {
				face.push_back(cp.first);
				was.insert(cp);
				int pos = int(lower_bound(e[cp.second].begin(), e[cp.second].end(), cp.first, Comparator(cp.second)) - e[cp.second].begin());
				cp = make_pair(cp.second, e[cp.second][(pos + 1) % (int)e[cp.second].size()]);
			} while (cp != sp);
			faces.push_back(face);
		}
	}
	int best = 0;
	vector<int> how, curColoring(n);
	dfs(faces, 0, 0, best, how, curColoring, n);
	printf("%d\n", best);
	for (int i = 0; i < n; i++) {
		printf("%d ", how[i]);
	}
}

int main() {
	int nt;
	scanf("%d", &nt);
	for (int it = 1; it <= nt; it++) {
		printf("Case #%d: ", it);
		solve(it);
		printf("\n");
	}
	return 0;
}
