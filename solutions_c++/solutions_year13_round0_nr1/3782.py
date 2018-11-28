/*
 * a.cpp
 *
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {}

string getState(const string &board) {
	string symbols = "OX";
	foreach(c, symbols) {
		string victory = string(1, *c) + " won";
		forn(i, 4) {
			int j = 0;
			for(; j < 4; ++j)
				if (board[i*4+j] != *c && board[i*4+j] != 'T') break;
			if (j == 4) return victory;
		}
		forn(j, 4) {
			int i = 0;
			for(; i < 4; ++i)
				if (board[i*4+j] != *c && board[i*4+j] != 'T') break;
			if (i == 4) return victory;
		}
		int k;
		for(k = 0; k < 4; ++k)
			if (board[k*4+k] != *c && board[k*4+k] != 'T') break;
		if (k == 4) return victory;
		for(k = 0; k < 4; ++k)
			if (board[k*4+3-k] != *c && board[k*4+3-k] != 'T') break;
		if (k == 4) return victory;
	}
	foreach(c, board)
		if (*c == '.')
			return "Game has not completed";
	return "Draw";
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		string board(16, ' ');
		forn(i, 4)
			forn(j, 4)
				cin >> board[i*4+j];
		string ans = getState(board);
		cout << "Case #" << (k+1) << ": " << ans << endl;
	}
	return 0;
}
