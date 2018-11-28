#include <cstdio>
#include <vector>
#include <list>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;

vector<int> coloring;
bool rec(int pos, int maxPos, int colors, const vector<list<int> > &components) {
	if (pos == maxPos) {
		bool ok = true;
		vector<int> used(colors);
		for (int i = 0; i < components.size(); i ++) {
			fill(used.begin(), used.end(), 0);
			for (list<int> :: const_iterator it = components[i].begin(); it != components[i].end(); it ++) {
				used[coloring[*it]] = 1;
			}
			if (count(used.begin(), used.end(), 0)) {
				ok = false;
				break;
			}
		}
		return ok;
	}
	for (int i = 0; i < colors; i ++) {
		coloring.push_back(i);
		if (rec(pos + 1, maxPos, colors, components)) {
			return true;
		}
		coloring.pop_back();
	}
	return false;
}

int T;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++) {
		int N, M;
		scanf("%d %d", &N, &M);
		vector<list<int> > comps;
		comps.push_back(list<int>());
		vector<set<int> > in(N + 1, set<int>());
		for (int i = 1; i <= N; i ++) {
			comps[0].push_back(i);
			in[i].insert(0);
		}
		vector<int> start(M), end(M);
		for (int i = 0; i < M; i ++) {
			scanf("%d", &start[i]);
		}
		for (int i = 0; i < M; i ++) {
			scanf("%d", &end[i]);
		}
		for (int i = 0; i < M; i ++) {
			int p = start[i], q = end[i];
			int component;
			vector<int> res(in[p].size() + in[q].size());
			vector<int> :: iterator resIt = set_intersection(in[p].begin(), in[p].end(), in[q].begin(), in[q].end(), res.begin());
//			assert (res.size() == 1);
			component = res.front();
			list<int> newComp;
			newComp.push_back(p);
			in[p].insert(comps.size());
			list<int> :: iterator it = comps[component].begin();
			while (*it ++ != p) ;
			list<int> :: iterator first = it;
			while (*it != q) {
				in[*it].erase(component);
				in[*it].insert(comps.size());
				newComp.push_back(*it ++);
			}
			newComp.push_back(q);
			in[q].insert(comps.size());
			comps[component].erase(first, it);
			comps.push_back(newComp);
		}
		int bound = 1000;
		for (int i = 0; i < comps.size(); i ++) {
			if (comps[i].size() < bound) {
				bound = comps[i].size();
			}
		}
		int colors;
		if (bound == N) {
			colors = N;
			coloring.clear();
			coloring.push_back(-1);
			for (int i = 0; i < N; i ++) {
				coloring.push_back(i);
			}
		} else {
			for (colors = bound; colors > 0; colors --) {
				coloring.clear();
				coloring.push_back(-1);
				if (rec(1, N + 1, colors, comps)) {
					break;
				}
			}
		}
		printf("Case #%d: %d\n", t, colors);
		printf("%d", coloring[1] + 1);
		for (int i = 2; i <= N; i ++) {
			printf(" %d", coloring[i] + 1);
		}
		printf("\n");
	}
}