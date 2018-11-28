#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <memory.h>

using namespace std;

string solve() {
	string s[10];
	
	for (int i = 0; i < 4; ++i) {
		cin >> s[i];
	}
	
	for (int i = 0; i < 4; ++i) {
		int x = 0, o = 0;
		
		for (int j = 0; j < 4; ++j) {
			if (s[i][j] == 'X' || s[i][j] == 'T') {
				++x;
			}
			if (s[i][j] == 'O' || s[i][j] == 'T') {
				++o;
			}
		}
		
		if (x == 4) {
			return "X won";
		}
		if (o == 4) {
			return "O won";
		}
	}
	for (int j = 0; j < 4; ++j) {
		int x = 0, o = 0;
		
		for (int i = 0; i < 4; ++i) {
			if (s[i][j] == 'X' || s[i][j] == 'T') {
				++x;
			}
			if (s[i][j] == 'O' || s[i][j] == 'T') {
				++o;
			}
		}
		
		if (x == 4) {
			return "X won";
		}
		if (o == 4) {			
			return "O won";
		}
	}
	
	int x = 0, o = 0;
	
	for (int i = 0; i < 4; ++i) {
		if (s[i][i] == 'X' || s[i][i] == 'T') {
			++x;
		}
		if (s[i][i] == 'O' || s[i][i] == 'T') {
			++o;
		}
	}
	if (x == 4) {
		return "X won";
	}
	if (o == 4) {
		return "O won";
	}
	
	x = 0; o = 0;
		
	for (int i = 0; i < 4; ++i) {
		if (s[i][3 - i] == 'X' || s[i][3 - i] == 'T') {
			++x;
		}
		if (s[i][3 - i] == 'O' || s[i][3 - i] == 'T') {
			++o;
		}
	}
	if (x == 4) {
		return "X won";
	}
	if (o == 4) {
		return "O won";
	}
	
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (s[i][j] == '.') {
				return "Game has not completed";
			}
		}
	}
	
	return "Draw";
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	int t;
	
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		
		cout << solve();
		
		cout << endl;
	}
	
	return 0;
}
