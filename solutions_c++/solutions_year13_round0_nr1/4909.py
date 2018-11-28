#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
typedef long long LL;

char mat[5][5];
bool check(char ch) {
	//check row
	for (int i = 0; i < 4; i++) {
		bool flag = true;
		for (int j = 0; j < 4 && flag; j++)
			if (mat[i][j] != ch && mat[i][j] != 'T') flag = false;
		if (flag) return true;
	}
	//check col
	for (int j = 0; j < 4; j++) {
		bool flag = true;
		for (int i = 0; i < 4 && flag; i++)
			if (mat[i][j] != ch && mat[i][j] != 'T') flag = false;
		if (flag) return true;
	}
	//diagonal 1
	bool flag = true;
	for (int i = 0, j = 0; i < 4 && j < 4 && flag; i++, j++) 
		if (mat[i][j] != ch && mat[i][j] != 'T') flag = false;
	if (flag) return true;
	//diagonal 2
	flag = true;
	for (int i = 0, j = 3; i < 4 && j >= 0 && flag; i++, j--)
		if (mat[i][j] != ch && mat[i][j] != 'T') flag = false;
	if (flag) return true;
	return false;
}
bool full() {
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) {
			if (mat[i][j] == '.') return false;
		}
	return true;
}
int main(int argc, char const *argv[])
{
	int Test;
	cin >> Test;
	for (int cas = 1; cas <= Test; cas++) {
		for (int i = 0; i < 4; i++) {
			scanf("%s", mat[i]);
		}
		printf("Case #%d: ", cas);
		if (check('X')) {
			cout << "X won" << endl;
		} else if (check('O')) {
			cout << "O won" << endl;
		} else if (full()) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
	}
	return 0;
}