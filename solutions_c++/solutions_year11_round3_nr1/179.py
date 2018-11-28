#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve(vector<string>& data, int R, int C) {
	for(int r = 0; r < R; ++r) {
		for(int c = 0; c < C; ++c) {
			if(data[r][c] != '#') { continue; }

			if(r == R-1 || c == C-1) { return 1; }

			if(data[r][c+1] != '#') { return 1; }
			if(data[r+1][c] != '#') { return 1; }
			if(data[r+1][c+1] != '#') { return 1; }
			data[r][c] = '/';
			data[r][c+1] = '\\';
			data[r+1][c] = '\\';
			data[r+1][c+1] = '/';
		}
	}
	return 0;
}

int main(void) {
	int T; cin >> T;
	for(int t = 0; t < T; ++t) {
		int R, C; cin >> R >> C;
		vector<string> data;
		for(int r = 0; r < R; ++r) {
			string s; cin >> s;
			data.push_back(s);
		}
		int ret = solve(data, R, C);
		cout << "Case #" << (t+1) << ":" << endl;
		if(ret) {
			cout << "Impossible" << endl;
		}
		else {
			for(int i = 0; i < R; ++i) {
				cout << data[i] << endl;
			}
		}
	}
	return 0;
}
