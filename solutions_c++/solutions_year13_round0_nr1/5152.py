#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;



bool check(vector<string>& b, char c1, char c2) {
	for(int i = 0;i < 4; ++i) {
		bool row = true, col = true;
		for(int j = 0;j < 4;++j) {
			row = row && (b[i][j] == c1 || b[i][j] == c2);
			col = col && (b[j][i] == c1 || b[j][i] == c2);
		}
		if(row || col) return true;
	}
	bool diag1 = true, diag2 = true;
	for(int i = 0;i < 4; ++i) {
		diag1 = diag1 && (b[i][  i] == c1 || b[i][  i] == c2);
		diag2 = diag2 && (b[i][3-i] == c1 || b[i][3-i] == c2);
	}
	return diag1 || diag2;
}

bool full(vector<string>& b) {
	for(int i = 0;i < 4; ++i) for(int j = 0; j < 4; ++j) {
		if(b[i][j] == '.') return false;
	}
	return true;
}

void solve(int t) {
	vector<string> b(4);
	for(int i = 0;i < 4; ++i) cin >> b[i];
	if(check(b, 'T', 'X')) { //X winner
		printf("Case #%d: X won\n", t);
	} else if(check(b, 'T', 'O')) { //O winner
		printf("Case #%d: O won\n", t);
	} else if(full(b)) {
		printf("Case #%d: Draw\n", t);
	} else {
		printf("Case #%d: Game has not completed\n", t);
	}
	
}

int main() {
	int T;
	cin >> T;
	for(int i = 1;i <= T; ++i) {
		solve(i);
	}
}