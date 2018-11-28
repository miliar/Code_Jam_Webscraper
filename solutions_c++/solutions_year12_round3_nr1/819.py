#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>
using namespace std;

bool dfs(const vector<vector<int> >& neigh, vector<bool> & visited, int v) {
	if (visited[v])
		return false;
	visited[v] = true;

	bool ans = true;
	for (size_t i = 0; i < neigh[v].size(); ++i)
		ans &= dfs(neigh, visited, neigh[v][i]);

	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	size_t test_cnt;
	cin >> test_cnt;
	for (size_t tst_num = 1; tst_num <= test_cnt; ++tst_num) {
		size_t n;
		cin >> n;
		vector<bool> has_parents(n);
		vector<vector<int> > sons(n);
		for (size_t i = 0; i < n; ++i) {
			size_t cnt;
			cin >> cnt;
			for (size_t j = 0; j < cnt; ++j) {
				int son;
				cin >> son;
				--son;
				has_parents[son] = true;
				sons[i].push_back(son);
			}
		}

		bool ok = true;
		for (size_t v = 0; v < n; ++v){
			vector<bool> visited(n);
			if (!has_parents[v])
				ok &= dfs(sons, visited, v);
		}
		cout << "Case #" << tst_num << ": " << (ok ? "No" : "Yes") << endl;
	}

	return 0;
}
