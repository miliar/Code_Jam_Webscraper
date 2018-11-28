#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

char board[10][10];

bool isWin(char c) {
	for(int i = 0; i < 4; i ++) {
		bool win = true;
		for(int j = 0; j < 4; j ++) {
			if(board[i][j]!=c && board[i][j]!='T') {
				win = false;
				break;
			}
		}
		if(win) {
			return true;
		}
	}
	for(int j = 0; j < 4; j ++) {
		bool win = true;
		for(int i = 0; i < 4; i ++) {
			if(board[i][j]!=c && board[i][j]!='T') {
				win = false;
				break;
			}
		}
		if(win) {
			return true;
		}
	}
	{
		bool win = true;
		for(int i = 0; i < 4; i ++) {
			if(board[i][i]!=c && board[i][i]!='T') {
				win = false;
				break;
			}
		}
		if(win) {
			return true;
		}
	}
	{
		bool win = true;
		for(int i = 0; i < 4; i ++) {
			if(board[i][4-1-i]!=c && board[i][4-1-i]!='T') {
				win = false;
				break;
			}
		}
		if(win) {
			return true;
		}
	}
	return false;
}

bool containDot() {
	for(int i = 0; i < 4; i ++) {
		for(int j = 0; j < 4; j ++) {
			if(board[i][j] == '.') {
				return true;
			}
		}
	}
	return false;
}

int main() {
	freopen("D:\\Downloads\\A-large.in", "r", stdin);
	freopen("sample.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i ++) {
		for(int i = 0; i < 4; i ++) {
			scanf("%s", board[i]);
		}
		printf("Case #%d: ", i);
		if(isWin('X')) {
			printf("X won\n");
		} else if(isWin('O')) {
			printf("O won\n");
		} else if(containDot()) {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}
	}
	return 0;
}
