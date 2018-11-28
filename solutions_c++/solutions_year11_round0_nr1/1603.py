#include <cstdio>
#include <vector>

using namespace std;

int gao(char x) {
	return x == 'B' ? 0 : 1;
}

int abs(int x) {
	return x > 0 ? x : -x;
}

int main() {
	int Case;
	scanf("%d", &Case);
	int pos[2], p[2];

	char c;
	int x;

	vector<pair<int, int> > vp;
	vector<int> task[2];
	for (int re = 1; re <= Case; ++re) {
		int n;
		scanf("%d", &n);
		vp.clear(), task[0].clear(), task[1].clear();
		for (int i = 0; i < n; ++i) {
			scanf(" %c %d", &c, &x);
			vp.push_back(make_pair(gao(c), x));
			task[gao(c)].push_back(x);
		}
		pos[0] = pos[1] = 1;
		p[0] = p[1] = 0;

		int t = 0;
		for (int i = 0; i < n; ++i) {
			int x = vp[i].first;
			int y = 1 ^ x;
			int need = abs(pos[x] - vp[i].second) + 1;
			t += need;
			if (p[y] < task[y].size()) {
				pos[y] = task[y][p[y]] - max(0, (abs(task[y][p[y]] - pos[y]) - need));
			}
			p[x]++;
			pos[x] = vp[i].second;
		}
		printf("Case #%d: %d\n", re, t);
	}
	return 0;
}
