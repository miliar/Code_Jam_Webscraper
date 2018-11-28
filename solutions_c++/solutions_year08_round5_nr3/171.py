#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, a) for(int i = 0; i < a.size(); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORC( it, V ) for( __typeof( (V).begin() ) it = (V).begin(); it != (V).end(); ++it )
#define SZ(a) a.size()

#define two(i) (1<<(i))
#define contain(set, i) (set&two(i))

vector<string> board;
int row, col;
int ans;

int count(int set) {
	int ret = 0;
	FOR(i, 0, col - 1)
		if (contain(set, i)) ret++;
	return ret;
}

bool checkValidInRow(int row, int set) {
	FOR(i, 0, col - 1)
		if (contain(set, i) && board[row][i] == 'x') return false;
	FOR(i, 0, col - 2)
		if (contain(set, i) && contain(set, i + 1)) return false;
	return true;
}

bool checkValidTwoRow(int rowa, int rowb) {
	FOR(i, 0, col - 2)
		if (contain(rowa, i) && contain(rowb, i + 1)) return false;
		
	FOR(i, 1, col - 1) {
		if (contain(rowa, i) && contain(rowb, i - 1)) return false;
	}
	
	return true;
}


void solve() {
	ans = 0;
	
	int f[row][two(col)];
	FOR(i, 0, two(col) - 1) {
		if (checkValidInRow(0, i)) {
			f[0][i] = count(i);
		} else f[0][i] = -1;
	}
	
	FOR(i, 1, row - 1) {
		FOR(set, 0, two(col) - 1) {
			if (checkValidInRow(i, set)) {
				int c = count(set);				
				f[i][set] = c;
				FOR(prev_row, 0, two(col) - 1)
					if ((f[i - 1][prev_row] != -1) && checkValidTwoRow(prev_row, set)) {
						f[i][set] = max(f[i][set], c + f[i - 1][prev_row]);
					}
			} else f[i][set] = -1;
		}
	}
	
	ans = 0;
	FOR(set, 0, two(col) - 1)
		ans = max(ans, f[row - 1][set]);
}

int main() {
	int test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ": ";
		cin >> row >> col;
		board.clear();
		FOR(j, 1, row) {
			string st;
			cin >> st;
			board.push_back(st);
		}
		solve();
		cout << ans << endl;
	}
	
	return 0;
}
