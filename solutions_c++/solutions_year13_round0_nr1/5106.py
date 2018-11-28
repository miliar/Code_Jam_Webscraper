#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define size(S) S.size()
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int T;
string map[6];

bool judge(char c) {
	for (int row = 0; row < 4; row++) {
		bool win = true;
		for (int col = 0; col < 4; col++)
			if (map[row][col] != c && map[row][col] != 'T') {
				win = false;
				break;
			}
		if (win) return true;
	}
	
	for (int col = 0; col < 4; col++) {
		bool win = true;
		for (int row = 0; row < 4; row++)
			if (map[row][col] != c && map[row][col] != 'T') {
				win = false;
				break;
			}
		if (win) return true;
	}
	
	bool win = true;
	for (int i = 0; i < 4; i++)
		if (map[i][i] != c && map[i][i] != 'T') {
			win = false;
			break;
		}
	if (win) return true;
	
	win = true;
	for (int i = 0; i < 4; i++)
		if (map[i][3 - i] != c && map[i][3 - i] != 'T') {
			win = false;
			break;
		}
	if (win) return true;
	
	return false;
}

bool empty() {
	for (int row = 0; row < 4; row++)
		for (int col = 0; col < 4; col++)
			if (map[row][col] == '.') return true;
	return false;
}

int main(){
	cin >> T;
	for (int cases = 1; cases <= T; cases++) {
		for (int row = 0; row < 4; row++) cin >> map[row];
		cout << "Case #" << cases << ": ";
		if (judge('O')) cout << "O won" << endl;
		else if (judge('X')) cout << "X won" << endl;
		else if (empty()) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}
}