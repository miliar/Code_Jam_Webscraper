#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

#define X first
#define Y second

char a[4][4];

bool is4(int x0, int y0, int xs, int ys, char c) {
	for (int i = 0; i < 4; ++i, x0 += xs, y0 += ys) {
		if (a[x0][y0] != c && a[x0][y0] != 'T')
			return 0;
	}
	return 1;
}

int main() {
	int T;
	scanf("%d\n", &T);
	int tid = 0;
	while (T--) {
		++tid;
		int cnt = 0;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j)
				scanf("%c", &a[i][j]), cnt += a[i][j] == '.' ? 1 : 0;
			scanf("\n");
		}
		scanf("\n");

		bool X = 0, O = 0;
		for (int i = 0; i < 4; ++i) {
			if (is4(i, 0, 0, 1, 'X'))
				X = 1;
			if (is4(i, 0, 0, 1, 'O'))
				O = 1;
			if (is4(0, i, 1, 0, 'X'))
				X = 1;
			if (is4(0, i, 1, 0, 'O'))
				O = 1;
		}
		if (is4(0, 0, 1, 1, 'X'))
			X = 1;
		if (is4(0, 0, 1, 1, 'O'))
			O = 1;
		if (is4(3, 0, -1, 1, 'X'))
			X = 1;
		if (is4(3, 0, -1, 1, 'O'))
			O = 1;

		printf("Case #%d: ", tid);

		if (X)
			printf("X won\n");
		else if (O)
			printf("O won\n");
		else if (cnt > 0)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
		
	}
}