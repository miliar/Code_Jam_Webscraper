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
#include <cstring>

using namespace std;

int _t, n, KK;
string res, in[55];
int d[8][2] = {{-1, -1}, {-1, 0}, {-1, +1}, {0, -1}, {0, +1}, {+1, -1}, {+1, 0}, {+1, +1}};

void rotate() {
	string tmp[55];
	for (int i = 0; i < n; i++) tmp[i].resize(n);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) tmp[i][j] = in[n - j - 1][i];
	for (int i = 0; i < n; i++) in[i] = tmp[i];
}

void move_down(int si, int sj) {
	for (int i = n - 1; i > si; i--) {
		if (in[i][sj] == '.') {
			in[i][sj] = in[si][sj];
			in[si][sj] = '.';
			break;
		}
	}
}

void gravity() {
	for (int j = 0; j < n; j++) 
		for (int i = n - 1; i >= 0; i--) 
			if (in[i][j] != '.') move_down(i, j);
}

bool valid(int i, int j, char c) {
	if (i < 0 || i >= n || j < 0 || j >= n) return false;
	return (in[i][j] == c);
}

bool check(int i, int j, int k, char c) {
	for (int z = 2; z <= KK; z++) {
		i += d[k][0]; j += d[k][1];
		if (valid(i, j, c) == false) return false;
	}
	return true;
}

bool win(char c) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (in[i][j] == c)
				for (int k = 0; k < 8; k++)
					if (check(i, j, k, c) == true) return true;
	return false;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &_t);
	for (int cas = 1; cas <= _t; cas++) {
		scanf("%d%d", &n, &KK);
		for (int i = 0; i < n; i++) cin >> in[i];
		rotate();
		gravity();
		bool A = win('B'), B = win('R');
		if (A == false && B == false) res = "Neither";
		if (A == false && B == true) res = "Red";
		if (A == true && B == false) res = "Blue";
		if (A == true && B == true) res = "Both";
		printf("Case #%d: %s\n", cas, res.c_str());
	}
	return 0;
}