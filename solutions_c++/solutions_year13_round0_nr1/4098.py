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
#include <cstring>
using namespace std;

int ntest;
string s[4];

bool check(char c) {
	int cnt;
	for (int i = 0; i < 4; i++) {
		cnt = 0;
		for (int j = 0; j < 4; j++)
			cnt += s[i][j] == c || s[i][j] == 'T';
		if (cnt == 4) return true;
		cnt = 0;
		for (int j = 0; j < 4; j++)
			cnt += s[j][i] == c || s[j][i] == 'T';
		if (cnt == 4) return true;	
	}
	cnt = 0;
	for (int i = 0; i < 4; i++) cnt += s[i][i] == c || s[i][i] == 'T';
	if (cnt == 4) return true;
	cnt = 0;
	for (int i = 0; i < 4; i++) cnt += s[i][4 - i - 1] == c || s[i][4 - i - 1] == 'T';
	if (cnt == 4) return true;
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> ntest;
	for (int test = 0; test < ntest; test++) {
		bool hasDot = false;
		for (int i = 0; i < 4; i++) {
			cin >> s[i];
			for (int j = 0; j < 4; j++)
				hasDot |= s[i][j] == '.';
		}
		bool XWin = check('X');
		bool OWin = check('O');
		cout << "Case #" << test + 1 << ": ";
		if (XWin) cout << "X won";
		else 
		if (OWin) cout << "O won";
		else 
		if (hasDot) cout << "Game has not completed";
		else cout << "Draw";
		cout << endl;
	}
}
