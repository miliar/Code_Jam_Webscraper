#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <fstream>
#define MAX 110

using namespace std;

bool arr[2][MAX][MAX];
int n = 0;
int toggle = 0;

bool allDie();
bool next(int i, int j);
bool isIn(int i, int j) { return i >= 0 && j >= 0 && i < MAX && j < MAX; }

int main() {
	ofstream out("c.out");
	int T = 0;
	cin >> T;
	for (int nth = 0; nth < T; nth++) {
		int ret = 0;
		toggle = 0;
		n = 0;
		out << "Case #" << nth+1 << ": ";
		memset(arr, false, sizeof(arr));
		cin >> n;
		for (int i = 0; i < n; i++) {
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int j = x1-1; j <= x2-1; j++) {
				for (int k = y1-1; k <= y2-1; k++) {
					arr[0][k][j] = true;
				}
			}
		}
		while (!allDie()) {
			int nexttoggle = -toggle + 1;
			for (int i = 0; i < MAX; i++) {
				for (int j = 0; j < MAX; j++) {
					arr[nexttoggle][i][j] = next(i, j);
				}
			}
			ret++;
			/*for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 10; j++) {
					cout << arr[nexttoggle][i][j] << ',';
				}
				cout << endl;
			}*/
			toggle = nexttoggle; 
	/*		int tmp;
			cin >> tmp;*/
		}
		out << ret;
		out << endl;
	}
	out.close();
	return 0;
}

bool allDie() {
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			if (arr[toggle][i][j] != 0) return false;
		}
	}
	return true;
}

bool next(int i, int j) {
	if (arr[toggle][i][j]) {	// 살아있으면
		if (!(isIn(i-1, j) && arr[toggle][i-1][j])
				&& !(isIn(i, j-1) && arr[toggle][i][j-1]))
			return false;
		else
			return true;
	}
	else {		// 죽어있으면
		if (isIn(i-1, j) && isIn(i, j-1)) {	// 북쪽 && 서쪽
			if (arr[toggle][i-1][j] && arr[toggle][i][j-1])
			{
				return true;
			}
			else {
				return false;
			}
		}
		return false;
	}
}
