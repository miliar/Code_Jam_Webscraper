#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int TESTS, CASE;

string T[4];

bool check(char c) {
	int x = -1, y = -1;
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(T[i][j] == 'T') {
				T[i][j] = c;
				x = i;
				y = j;
			}
		}
	}
	
	bool res = false;
	if(T[0][0]==c&&T[1][1]==c&&T[2][2]==c&&T[3][3]==c) res = true;
	if(T[0][3]==c&&T[1][2]==c&&T[2][1]==c&&T[3][0]==c) res = true;
	for(int i = 0; i < 4; i++) {
		if(T[i][0]==c&&T[i][1]==c&&T[i][2]==c&&T[i][3]==c) res = true;
		if(T[0][i]==c&&T[1][i]==c&&T[2][i]==c&&T[3][i]==c) res = true;
	}
	
	if(x != -1) {
		T[x][y] = 'T';
	}
	return res;
}

bool going() {
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(T[i][j] == '.') {
				return true;
			}
		}
	}
	return false;
}

void solve() {
	cout << "Case #" << CASE << ": ";
	if(check('X')) {
		cout << "X won";
	} else if(check('O')) {
		cout << "O won";
	} else if(going()) {
		cout << "Game has not completed";
	} else {
		cout << "Draw";
	}
	cout << endl;
}

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	cin.sync_with_stdio(false);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		for(int i = 0; i < 4; i++) {
			cin >> T[i];
		}
		solve();
	}
}
