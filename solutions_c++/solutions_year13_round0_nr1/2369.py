#include      <algorithm>
#include      <cmath>
#include      <cstdarg>
#include      <cstdio>
#include      <cstdlib>
#include      <iomanip>
#include      <iostream>
#include      <iterator>
#include      <limits>
#include      <list>
#include      <map>
#include      <set>
#include      <vector>
#define endl '\n'
#define each(c, e) for (typeof(c.begin()) e = c.begin(); e != c.end(); ++e)
typedef long long ll;
using namespace std;

bool inLineChar(char aLine[4], char ch) {
	bool bGood = true;
	for (int i = 0; i < 4; i += 1) {
		bGood = bGood && (aLine[i] == ch || aLine[i] == 'T');
	}
	return bGood;
}
bool inColChar(char aState[4][4], int nCol, char ch) {
	bool bGood = true;
	for (int i = 0; i < 4; i += 1) {
		bGood = bGood && (aState[i][nCol] == ch || aState[i][nCol] == 'T');
	}
	return bGood;
}
bool inDiagChar(char aState[4][4], char ch) {
	bool bGood[2] = {true, true};
	for (int i = 0; i < 4; i += 1) {
		bGood[0] = bGood[0] && (aState[i][i] == ch || aState[i][i] == 'T');
		bGood[1] = bGood[1] && (aState[i][3 - i] == ch || aState[i][3 - i] == 'T');
	}
	return bGood[0] || bGood[1];
}
void solve() {
	char aState[4][4];
	for (int i = 0; i < 4; i += 1) for (int j = 0; j < 4; j += 1) cin >> aState[i][j];

	bool bIsFull = true, bXWon = false, bOWon = false;
	for (int i = 0; i < 4; i += 1) for (int j = 0; j < 4; j += 1) bIsFull = bIsFull && aState[i][j] != '.';

	for (int i = 0; i < 4; i += 1) {
		bXWon = bXWon || inLineChar(aState[i], 'X') || inColChar(aState, i, 'X');
		bOWon = bOWon || inLineChar(aState[i], 'O') || inColChar(aState, i, 'O');
	}
	bXWon = bXWon || inDiagChar(aState, 'X');
	bOWon = bOWon || inDiagChar(aState, 'O');

	if (bXWon) cout << "X won" << endl;
	else if (bOWon) cout << "O won" << endl;
	else if (bIsFull) cout << "Draw" << endl;
	else cout << "Game has not completed" << endl;
}

int main(int argc, char **argv) {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t += 1) {
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
