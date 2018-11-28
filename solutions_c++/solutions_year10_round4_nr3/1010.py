#include <string>
#include <cstring>
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
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

const int MAXN = 110;

int T;
int ret, R;
int A[MAXN][MAXN];

void paint(int x1, int y1, int x2, int y2) {
	for (int i = x1; i <= x2; ++i) 
		for (int j = y1; j <= y2; ++j) 
			A[i][j] |= 1;
}

int nN(int x, int y) {
	return A[x][y - 1] == 1;
}

int nW(int x, int y) {
	return A[x - 1][y] == 1;
}

void play() {
	int total = 0;
	for (int i = 1; i <= 100; ++i)
		for (int j = 1; j <= 100; ++j) total += A[i][j];
	if (total == 0) return;

	while (true) {

		int B[MAXN][MAXN];
		memset(B, 0, sizeof B);

		for (int i = 1; i <= 100; ++i)
			for (int j = 1; j <= 100; ++j) {
				if (!nN(i, j) && !nW(i ,j)) {
					B[i][j] = 0;
					continue;
				}
				else if (A[i][j] == 0 && nN(i, j) && nW(i, j)) {
					B[i][j] = 1;
				}
				else B[i][j] = A[i][j];

			}

		memcpy(A, B, sizeof A);
		++ret;

		int total = 0;
		for (int i = 1; i <= 100; ++i)
			for (int j = 1; j <= 100; ++j) total += A[i][j];
		if (total == 0) return;
	}
}

int main(void) 
{
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		ret = 0;
		scanf("%d", &R);
		for (int i = 0; i < R; ++i) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			paint(x1, y1, x2, y2);
		}
		play();
		printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}