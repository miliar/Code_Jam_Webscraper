//C++ Template: http://pastebin.com/dGrr0CpX

#pragma comment(linker,"/STACK:256000000")

#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <ctime>
#include <set>
#include <map>

using namespace std;

#define all(a) a.begin(), a.end()
#define PI 3.14159265358979
#define sz(a) (int)a.size()
#define ppb push_back
#define mp make_pair
#define scnd second
#define fst first

template <class T> T sqr(T n) {
	return n*n;
}

template <class T> T gcd(T a, T b) {
	while (b) {
		a %= b;
		cout << a << " " << b << endl;
		swap(a, b);
	}
    return a;
}

const int SZ = 1010;
const int INF = 1000*1000*1000;

double start, finish;
/****************************************************************************/
void prepare(string s) {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	if (sz(s) != 0) {
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

void startTimer() {
#ifdef _DEBUG
	start = clock();
#endif
}

void stopTimer() {
#ifdef _DEBUG
	finish = clock();
    cout << "\n*** Total time ***\n" << (finish - start)/CLOCKS_PER_SEC << endl;
#endif
}
/****************************************************************************/

const int X = 100;
const int O = -100;
const int DRAW = 0;
const int FAIL = INF;

int n;
int board[4][4];
bool point = false;

void getBoard() {
	point = false;
	char ch;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> ch;
			board[i][j] = ch;
			if (board[i][j] == '.') {
				point = true;
			}
		}
	}
}

bool checkRow(char ch) {
	bool fl;
	for (int i = 0; i < 4; ++i) {
		fl = true;
		for (int j = 0; j < 4; ++j) {
			if ( !(board[i][j] == ch || board[i][j] == 'T') ) {
				fl = false;
				break;
			}
		}
		if (fl) {
			return true;
		}
	}

	return false;
}

bool checkCol(char ch) {
	bool fl;
	for (int j = 0; j < 4; ++j) {
		fl = true;
		for (int i = 0; i < 4; ++i) {
			if ( !(board[i][j] == ch || board[i][j] == 'T') ) {
				fl = false;
				break;
			}
		}
		if (fl) {
			return true;
		}
	}

	return false;
}

bool checkMainCross(char ch) {
	bool fl = true;
	for (int i = 0; i < 4; ++i) {
		if ( !(board[i][i] == ch || board[i][i] == 'T') ) {
			fl = false;
			break;
		}
	}

	return fl;
}

bool checkSideCross(char ch) {
	bool fl = true;
	for (int i = 0; i < 4; ++i) {
		if ( !(board[i][3 - i] == ch || board[i][3 - i] == 'T') ) {
			fl = false;
			break;
		}
	}

	return fl;
}


int getAns() {
	if (checkRow('X') || checkCol('X') || checkSideCross('X') || checkMainCross('X')) {
		return X;
	}
	if (checkRow('O') || checkCol('O') || checkSideCross('O') || checkMainCross('O')) {
		return O;
	}
	if (point) {
		return FAIL;
	}

	return DRAW;
}

int main() {

prepare("A-large");
ios::sync_with_stdio(false);

startTimer();

	cin >> n;
	for (int i = 0; i < n; ++i) {
		getBoard();
		int ans = getAns();
		cout << "Case #" << i + 1 << ": ";
		switch (ans) {
			case X: cout << "X won" << endl; break;
			case O: cout << "O won" << endl; break;
			case FAIL: cout << "Game has not completed" << endl; break;
			case DRAW: cout << "Draw" << endl; break;
		}
	}

stopTimer();
	return 0;
}