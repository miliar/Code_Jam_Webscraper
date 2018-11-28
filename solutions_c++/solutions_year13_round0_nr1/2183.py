#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

char a[5][5];

bool diag(int y, int x) {
    char c = a[y][x];
    int i = y, j = x, cnt = 0;
    while (i < 4 && j >= 0) {
        if (a[i][j] == c) cnt++;
        else break;
        i++, j--;
    }
    if (cnt >= 4) return 1;
    i = y, j = x, cnt = 0;
    while (i < 4 && j < 4) {
        if (a[i][j] == c) cnt++;
        else break;
        i++, j++;
    }
    return cnt >= 4;
}
bool col(int y, int x) {
    char c = a[y][x], cnt = 0;
    for (int i=y; i<4; i++) if (a[i][x] == c) cnt++; else break;
    return cnt >= 4;
}
bool row(int y, int x) {
    char c = a[y][x], cnt = 0;
    for (int i=x; i<4; i++) if (a[y][i] == c) cnt++; else break;
    return cnt >= 4;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for (int it = 0; it < test; it++) {
		int yy=-1, xx=-1;
        for (int i = 0; i < 4; i++) {
            scanf("%s\n", &a[i]);
			for (int j = 0; j < 4; j++)
				if (a[i][j] == 'T')
					yy = i, xx = j;
        }
        bool has = 0;
        string ans = "Game has not completed";
		if (xx > -1) a[yy][xx]='X';
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
				if (a[i][j] == '.') {has = 1; continue;}

                if (diag(i, j) || row(i, j) || col(i, j)) {
                    if (a[i][j] == 'X') {
                        ans = "X won";
                    } else {
                        ans = "O won";
                    }
                }
            }
        }
		if (xx>-1) a[yy][xx]='O';
		for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
				if (a[i][j] == '.') {has = 1; continue;}

                if (diag(i, j) || row(i, j) || col(i, j)) {
                    if (a[i][j] == 'X') {
                        ans = "X won";
                    } else {
                        ans = "O won";
                    }
                }
            }
        }
        if (ans[0] != 'X' && ans[0] != 'O' && !has) {
            ans = "Draw";
        }
        printf("Case #%d: %s\n", it + 1, ans.c_str());
    }
    return 0;
}
