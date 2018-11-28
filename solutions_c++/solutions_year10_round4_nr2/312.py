#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
#include <vector>

map<pair<int, int>, int> ans;
vector<vector<int> > OMIN;
int n;
int p;
vector<int> need, cost;

int get(int vert, int left, int right, int delta) {//   [left,right)
//	printf("%d %d %d %d\n", vert, left, right, delta);
	if (ans.count(make_pair(vert, delta)) == 0) {
		if (OMIN[left][right - 1] < delta) {
			return 1000000000;
		}
		if (left == right - 2) {//two elements
			if (need[left] == delta || need[left + 1] == delta) 
				return cost[vert];
			else
				return 0;
		}
		//buy;
		int a1 = cost[vert] + get(vert * 2 + 1, left, (left + right + 1) / 2, delta) + get(vert * 2 + 2, (left + right + 1) / 2, right, delta);
		int a2;
		if (OMIN[left][right - 1] == delta)
			a2 = 1000000000;
		else {
		a2 = get(vert * 2 + 1, left, (left + right + 1) / 2, delta + 1) + get(vert * 2 + 2, (left + right + 1) / 2, right, delta + 1);
		}
//		printf("%d %d %d %d: %d %d\n", vert, left, right, delta, a1, a2);

		ans[make_pair(vert, delta)] = min(a1, a2);
		return min(a1, a2);
	}
	return ans[make_pair(vert, delta)];
}

void solve() {
	scanf("%d", &p);
	n = 1 << p;
	need.resize(n);
	for (int i = 0; i < need.size(); ++i)
		scanf("%d", &need[i]);
	vector<vector<int> > tmp(p);
	for (int i = 0; i < p; ++i) {
		tmp[i].resize(1 << (p - i - 1));
		for (int j = 0; j < (1 << (p - i - 1)); ++j)
			scanf("%d", &tmp[i][j]);
	}
	cost.clear();
	for (int i = p - 1; i >= 0; --i)
		for (int j = 0; j < tmp[i].size(); ++j)
			cost.push_back(tmp[i][j]);
	OMIN.resize(n);
	for (int i = 0; i < n; ++i) {
		OMIN[i].resize(n);
		OMIN[i][i] = need[i];
		for (int j = i + 1; j < n; ++j)
			OMIN[i][j] = min(OMIN[i][j - 1], need[j]);
	}
	ans.clear();
//	for (int i = 0; i < need.size(); ++i) printf("%d ", need[i]);printf("\n");
//	for (int i = 0; i < cost.size(); ++i) printf("%d ", cost[i]);printf("\n");
	printf("%d\n", get(0, 0, n, 0));
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		cerr << i << endl;
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
