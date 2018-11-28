#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("input");
ofstream fout("output");

void solve() {
	int n;
	fin >> n;
	vector< vector<int> > sequence(2);
	vector<int> order(n);
	for (int i = 0; i < n; i++) {
		string robot;
		int pos;
		fin >> robot >> pos;
		sequence[(robot == "O") ? 0 : 1].push_back(pos);
		order[i] = (robot == "O") ? 0 : 1;
	}
	int curpos[] = {1, 1}, pointer[] = {0, 0};
	int ans, k = 0;
	for (ans = 0; pointer[0] < sequence[0].size() || pointer[1] < sequence[1].size(); ans++) {
		bool pushed = false;
		for (int i = 0; i < 2; i++) {
			if (pointer[i] < sequence[i].size()) {
				if (curpos[i] == sequence[i][pointer[i]] && order[k] == i && !pushed) {
					pointer[i]++, pushed = true, k++;
				}
				else if (curpos[i] != sequence[i][pointer[i]]) {
					curpos[i] += (sequence[i][pointer[i]] > curpos[i]) ? 1 : -1;
				}
			}
		}
	}
	fout << ans << endl;
}

int main() {	
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
