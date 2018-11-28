#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

string board[4];
bool over;

bool won(char side) {
	bool horiz[4] = { true, true, true, true };
	bool vert[4] = { true, true, true, true };
    bool diag1 = true, diag2 = true;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            horiz[j] &= board[i][j] == side || board[i][j] == 'T';
            vert[j] &= board[j][i] == side || board[j][i] == 'T';
            over &= board[i][j] != '.';
		}
        diag1 &= board[i][i] == side || board[i][i] == 'T';
        diag2 &= board[3-i][i] == side || board[3-i][i] == 'T';
	}
    if (diag1 || diag2) return true;
    for (int i = 0; i < 4; ++i) if (horiz[i] || vert[i]) return true;
    return false;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cases;
    cin >> cases;
    string line;
    for (int cas = 1; cas <= cases; ++cas) {
        getline(cin, line);
        for (int i = 0; i < 4; ++i) getline(cin, board[i]);
        over = true;
		cout << "Case #" << cas << ": ";
        if (won('X')) cout << "X won\n";
		else if (won('O')) cout << "O won\n";
		else if (over) cout << "Draw\n";
		else cout << "Game has not completed\n";
	}
}
