#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <cstdio>

using namespace std;
typedef long long LL;

bool isWon(const vector<string> &pol, char c) {
	for (int i = 0; i < 4; ++i) {
		bool flag = true;
		for (int j = 0; j < 4; ++j) {
			if (pol[i][j] != c && pol[i][j] != 'T') {
				flag = false;
			}
		}
		if (flag) {
			return true;
		}
	}
	for (int i = 0; i < 4; ++i) {
		bool flag = true;
		for (int j = 0; j < 4; ++j) {
			if (pol[j][i] != c && pol[j][i] != 'T') {
				flag = false;
			}
		}
		if (flag) {
			return true;
		}
	}									  
	bool flag = true;
	for (int j = 0; j < 4; ++j) {
		if (pol[j][j] != c && pol[j][j] != 'T') {
			flag = false;
		}
	}
	if (flag) {
		return true;
	}
	flag = true;
	for (int j = 0; j < 4; ++j) {
		if (pol[j][3-j] != c && pol[j][3-j] != 'T') {
			flag = false;
		}
	}
	if (flag) {
		return true;
	}
	
	return false;
}
bool isFull(const vector<string> &pol) {
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (pol[i][j] == '.') {
				return false;
			}
		}
	}
	return true;
}


int main() {						   
	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		vector<string> pol(4);
		for (int i = 0; i < 4; ++i) {
			cin >> pol[i];
		}
													   
		if (isWon(pol, 'X')) {
			cout << "Case #" << t << ": X won" << endl;
		}
		else if (isWon(pol, 'O')) {
			cout << "Case #" << t << ": O won" << endl;
		}
		else if (isFull(pol)) {
			cout << "Case #" << t << ": Draw" << endl;
		}
		else {
			cout << "Case #" << t << ": Game has not completed" << endl;
		}
	}


	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	return 0;
}
