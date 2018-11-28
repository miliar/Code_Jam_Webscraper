#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

bool red, blue;
char board[100][100];
int N, K;

bool is_valid(int x, int y) {
	return 0 <= x && x < N && 0 <= y && y < N;
}

bool win(int x, int y) {
	int dx[] = {-1, 0, 1, 1, 1, 0,-1,-1};
	int dy[] = {-1,-1,-1, 0, 1, 1, 1, 0};
	for(int i = 0; i < 8; ++i) {
		int j = 0;
		for(; j < K; ++j) {
			if (is_valid(x + dx[i] * j, y + dy[i] * j) != true || board[y][x] != board[y + dy[i] * j][x + dx[i] * j]) {
				break;
			}
		}
		if (j == K)
			return true;
	}
	return false;
}

void determine() {
	for(int i = 0; i < N; ++i) {
		for(int j = 0; j < N; ++j) {
			if (board[i][j] != '.' && win(j, i) == true) {
				if (board[i][j] == 'B')
					blue = true;
				else
					red = true;
			}
		}
	}
}

void solve() {
	for(int i = 0; i < N; ++i) {
		int right = N-1;
		for(int j = N-1; j >= 0; --j) {
			if (board[i][j] != '.') {
				if (j != right) {
					board[i][right] = board[i][j];
					board[i][j] = '.';
				}
				--right;
			}
		}
	}
	determine();
}

int main() {
	freopen("f:/downloads/A-small-attempt4.in", "r", stdin);
	freopen("f:/downloads/output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int z = 0; z < T; ++z) {
		scanf("%d%d", &N, &K);

		for(int i = 0; i < N; ++i) {
			scanf("%s", board[i]);
		}

		red = blue = false;
		solve();

		printf("Case #%d: ", z + 1);
		if (red == true && blue == true)
			printf("Both\n");
		else if (red == true && blue == false)
			printf("Red\n");
		else if (red == false && blue == true)
			printf("Blue\n");
		else if (red == false && blue == false)
			printf("Neither\n");
	}
}
