#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <cstdio>
using namespace std;

const int inf = (int)1e9;

int a[4][4];

bool wan(int p)
{
	for (int i = 0; i < 4; ++i) {
		int sum = 0;
		for (int j = 0; j < 4; ++j) {
			if (a[i][j] == p || a[i][j] == 3) ++sum;
		}
		if (sum == 4) return true;
	}
	for (int i = 0; i < 4; ++i) {
		int sum = 0;
		for (int j = 0; j < 4; ++j) {
			if (a[j][i] == p || a[j][i] == 3) ++sum;
		}
		if (sum == 4) return true;
	}
	int sum = 0;
	for (int i = 0; i < 4; ++i) {
		if (a[i][i] == p || a[i][i] == 3) ++sum;
	}
	if (sum == 4) return true;
	sum = 0;
	for (int i = 0; i < 4; ++i) {
		if (a[i][3 - i] == p || a[i][3 - i] == 3) ++sum;
	}
	if (sum == 4) return true;
	
	return false;
}

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int t = 0; t < T; ++t) {
		string s;
		bool has_empty = false;
		for (int i = 0; i < 4; ++i) {
			getline(cin, s);
			for (int j = 0; j < 4; ++j) {
				a[i][j] = 0;
				if (s[j] == 'X') a[i][j] = 1;
				else if (s[j] == 'O') a[i][j] = 2;
				else if (s[j] == 'T') a[i][j] = 3;
				if (a[i][j] == 0) has_empty = true;
			}
		}
		getline(cin, s);
		printf("Case #%d: ", t + 1);
		if (wan(1)) printf("X won");
		else if (wan(2)) printf("O won");
		else if (has_empty) printf("Game has not completed");
		else printf("Draw");
		printf("\n");
	}
	
	return 0;
}
