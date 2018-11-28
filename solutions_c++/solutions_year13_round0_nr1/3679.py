#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <set>
#include <utility>

#define rep(i,j,k) for (int i = (int)j; i < (int)k; i++)
#define rep0(i,j) rep(i,0,j)
#define each(a,it) for (typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
#define mp(a,b) make_pair(a,b)
#define INF 999999

using namespace std;

int T, X, O, t, d;
char grid[4][4], r;
bool emptyB = false;

char isHor(int y) {
	X = 0; O = 0; t = 0, d = 0;
	rep0 (i,4) {
		if (grid[y][i] == 'X')
			X++;
		else if (grid[y][i] == 'O')
			O++;
		else if (grid[y][i] == 'T')
			t++;
		else {
			d++;
			emptyB = true;
		}
	}
	if (X == 4 || ( X == 3 && t == 1 ) )
		return 'X';
	else if (O == 4 || ( O == 3 && t == 1 ) )
		return 'O';
	else
		return '.';
}

char isVer(int x) {
	X = 0; O = 0; t = 0; d = 0;
	rep0 (i,4) {
		if (grid[i][x] == 'X')
			X++;
		else if (grid[i][x] == 'O')
			O++;
		else if (grid[i][x] == 'T')
			t++;
		else {
			d++;
			emptyB = true;
		}
	}
	if (X == 4 || ( X == 3 && t == 1 ) )
		return 'X';
	else if (O == 4 || ( O == 3 && t == 1 ) )
		return 'O';
	else
		return '.';
}

char isDiagonal1() {
	X = 0; O = 0; t = 0; d = 0;
	rep0 (i,4) {
		if (grid[i][i] == 'X')
			X++;
		else if (grid[i][i] == 'O')
			O++;
		else if (grid[i][i] == 'T')
			t++;
		else
			d++;
	}
	if (X == 4 || ( X == 3 && t == 1 ) )
		return 'X';
	else if (O == 4 || ( O == 3 && t == 1 ) )
		return 'O';
	else
		return '.';
}

char isDiagonal2() {
	X = 0; O = 0; t = 0; d = 0;
	rep0 (i,4) {
		if (grid[abs(i-3)][i] == 'X')
			X++;
		else if (grid[abs(i-3)][i] == 'O')
			O++;
		else if (grid[abs(i-3)][i] == 'T')
			t++;
		else
			d++;
	}
	if (X == 4 || ( X == 3 && t == 1 ) )
		return 'X';
	else if (O == 4 || ( O == 3 && t == 1 ) )
		return 'O';
	else
		return '.';
}

void solve (int i) {
	
	i += 1;
	
	rep0 (j,4) {
		r = isHor(j);
		if (r == 'X' || r == 'O') {
			cout << "Case #" << i << ": " << r << " won\n";
			emptyB = false;	
			return;
		}
		r = isVer(j);
		if (r == '.') continue;
		else {
			cout << "Case #" << i << ": " << r << " won\n";
			emptyB = false;	
			return;
		}
	}
	
	r = isDiagonal1();
	if (r != '.') {
		cout << "Case #" << i << ": " << r << " won\n";
		emptyB = false;	
		return;
	}
	
	r = isDiagonal2();
	if (r != '.') {
		cout << "Case #" << i << ": " << r << " won\n";
		emptyB = false;	
		return;
	}
	
	if (emptyB) {
		cout <<  "Case #" << i << ": Game has not completed\n";
	} else {
		cout << "Case #" << i << ": Draw\n";
	}

	emptyB = false;		
}

int main(int argc, char *argv[]) {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	cin >> T;
	int i = 0;
	while (T-- && T >= -1) {
		rep0 (j,4) rep0 (k,4) cin >> grid[j][k];
		solve(i);
		i++;
	}
}