#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
string maze[4];
bool same(char a,char b) {
	if (a == '.' || b == '.') return false;
	if (a == 'T' || b == 'T') return true;
	return a == b;
}
int same(char a,char b,char c,char d) {
	if (same(a,b) && same(b,c) && same(c,d) && same(d,a)) {
		if (a == 'T') {
			return b == 'X' ? 1 : 2;
		} else {
			return a == 'X' ? 1 : 2;
		}
	}
	return 0;
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T; 
	cin >> T;
	for (int cas = 1 ; cas <= T ; cas ++) {
		for (int i = 0 ; i < 4 ; i ++) {
			cin >> maze[i];
		}
		bool complete = true;
		for (int i = 0 ; i < 4 ; i ++) {
			for (int j = 0 ; j < 4 ; j ++) {
				if (maze[i][j]  == '.') {
					complete = false;
				}
			}
		}
		int ret = 0;
		for (int i = 0 ; i < 4 ; i ++) {
			int temp = same(maze[i][0] , maze[i][1] , maze[i][2] , maze[i][3]);
			if (temp) ret = temp;
		}
		for (int i = 0 ; i < 4 ; i ++) {
			int temp = same(maze[0][i] , maze[1][i] , maze[2][i] , maze[3][i]);
			if (temp) ret = temp;
		}
		int temp = same(maze[0][0] , maze[1][1] , maze[2][2] , maze[3][3]);
		if (temp) ret = temp;
		temp = same(maze[0][3] , maze[1][2] , maze[2][1] , maze[3][0]);
		if (temp) ret = temp;
		cout << "Case #" << cas << ": ";
		if (ret == 1) {
			cout << "X won" << endl;
		} else if (ret == 2) {
			cout << "O won" << endl;
		} else if (complete) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
	}
	return 0;
}