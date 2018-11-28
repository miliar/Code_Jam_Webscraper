/**********************************************************************
Author: LiuLixiang
Created Time:  2010/6/5 22:23:52
File Name: \TopCoder\gcj2010\Round2\C.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;

const int MAXN = 100;

typedef struct pos_t {
	int x, y;
};

pos_t pos[MAXN*MAXN+10];
int n, cnt = 0;
int table[2][MAXN+10][MAXN+10];
int cur, pre;
int row0, col0;
int row1, col1;

void set_bac(int x1, int y1, int x2, int y2) {
	for (int r = x1; r <= x2; r++) {
		for (int c = y1; c <= y2; c++) {
			if (!table[0][r][c]) {
				table[0][r][c] = 1;
				++cnt;
			}
		}
	}
}

void get_input() {
	memset(table, 0, sizeof(table));
	cnt = 0; cur = 0, pre = 1;
	row1 = 0, col1 = 0, row0 = 100, col0 = 100;//FIXME
	int R;
	int x1, x2, y1, y2;
	scanf("%d", &R);
	for (int i = 0; i < R; i++) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		set_bac(x1, y1, x2, y2);
		row1 = max(row1, x2);
		col1 = max(col1, y2);
		row0 = min(row0, x1);
		col0 = min(col0, y1);
	}
//	cout << row0 << "," << col0 << " " << row1 << " " << col1 << endl;///
}

void change() {
	cur = 1-cur;
	pre = 1-pre;
//	cout << "======================" << endl;///
	for (int r = row0; r <= row1; r++) {
		for (int c = col0; c <= col1; c++) {
			int flag = table[pre][r-1][c] + table[pre][r][c-1];
			if (table[pre][r][c]) {
				if (flag) {
					table[cur][r][c] = 1;
					cnt++;
				} else {
					table[cur][r][c] = 0;
				}
			} else {
				if (flag == 2) {
					table[cur][r][c] = 1;
					cnt++;
				} else {
					table[cur][r][c] = 0;
				}
			}
//			cout << table[pre][r][c] << " ";////
		}
//		cout << endl;///
	}
}

int solve() {
	int res = 0;
	while (cnt) {
		++res;
		cnt = 0;
		change();
	}
	return res;
}

int main() {
	freopen("C_A.txt", "w", stdout);///
    int C;
	scanf("%d", &C);
	for (int ca = 1; ca <= C; ca++) {
		get_input();
		printf("Case #%d: %d\n", ca, solve());
	}
	fclose(stdout);///
    return 0;
}

