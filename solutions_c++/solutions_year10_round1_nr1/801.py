#include <assert.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <climits>
#include <cmath>
#include <time.h>
#include <iomanip>

using namespace std;

int T, K, N;
char board[55][55];
char tmpboard[55][55];

int movex[8] = {-1, -1, -1, 0, 1, 1,  1, 0};
int movey[8] = {-1,  0,  1, 1, 1, 0, -1,-1};

bool isvalid(int nx, int ny, char cur) {
	if (tmpboard[nx][ny] != cur)
		return false;
	return (nx >= 1 && nx <= N && ny >= 1 && ny <= N);
}

bool judge(int x, int y) {
	char cur = tmpboard[x][y];	// 当前字符
	bool flag;
	// 八个方向
	for (int mv = 0; mv < 8; mv++) {
		flag = true;
		for (int i = 1; i < K; i++) {
			int nextx = x + i * movex[mv];
			int nexty = y + i * movey[mv];
			if (!isvalid(nextx, nexty, cur)) {
				flag = false;
				break;
			}
		}
		if (flag == true)
			return flag;
	}
	return false;
}

void gravity() {
	// 将每一列向下紧凑
	for (int col = 1; col <= N; col++) {
		queue<char> que;
		for (int row = N; row >= 1; row--) {
			if (tmpboard[row][col] != '.') {
				que.push(tmpboard[row][col]);
				tmpboard[row][col] = '.';
			}
		}

		int pt = N;
		while (!que.empty()) {
			tmpboard[pt][col] = que.front();
			que.pop();
			pt--;
		}
	}
}

void rotateBoard() {
	for (int i = 1; i <= N; i++)
		for (int  j = 1; j <= N; j++)
			tmpboard[j][N - i + 1] = board[i][j];

}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("large.out","w", stdout);
	cin >> T;
	for (int caseid = 1; caseid <= T; caseid++) {
		cin >> N >> K;
		for (int i = 1; i <= N; i++)
			for (int  j = 1; j <= N; j++)
				cin >> board[i][j];

		rotateBoard();


		gravity();

		// 判断是否满足条件
		bool red = false, blue = false;
		for (int i = 1; i <= N; i++) {
			for (int  j = 1; j <= N; j++) {
				if (tmpboard[i][j] != '.' && judge(i, j)) {
					if (tmpboard[i][j] == 'R') {
						red = true;
					} else {
						blue = true;
					}
				}
			}
		}

		// 输出结果
		string resstr;
		if (red && blue) {
			resstr = "Both";
		} else if (red) {
			resstr = "Red";
		} else if (blue) {
			resstr = "Blue";
		} else {
			resstr = "Neither";
		}
		cout << "Case #" << caseid << ": " << resstr << endl;
	}
}
