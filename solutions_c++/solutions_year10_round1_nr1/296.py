/**********************************************************************
Author: LiuLixiang
Created Time:  2010/5/22 8:50:05
File Name: \TopCoder\gcj2010\Round1A\A.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;

const int maxint=0x7FFFFFFF;

const int MAXN = 50;

int n, k;
char table[MAXN+5][MAXN+5];
char plat[MAXN+5][MAXN+5];

void get_input() {
	scanf("%d %d", &n, &k);
	for (int i = 1; i <= n; i++) {
		scanf("%s", plat[i]+1);
	}
}

void rotate() {
	for (int r = 1; r <= n; r++) {
		for (int c = 1; c <= n; c++) {
			table[r][c] = plat[n-c+1][r];//clockwise
//			printf("%c", table[r][c]); ///
		}
//		printf("\n"); ///
	}
//	printf(" ============ \n"); ///
}

void down() {
	int cnt = 0;
	char cur[MAXN+5];
	for (int c = 1; c <= n; c++) {
		cnt = 0;
		for (int r = n; r >= 1; r--) {
			if (table[r][c] != '.') {
				cur[cnt++] = table[r][c];
				table[r][c] = '.';
			}
		}
		for (int i = 0; i < cnt; i++) {
			table[n-i][c] = cur[i];
		}
	}
}

bool check_win(char color) {
	for (int r = 1; r <= n; r++) {
		for (int c = 1; c <= n; c++) {
			if (table[r][c] == color) {
	//row
				if (n-c >= k-1) {
					bool flag = true;
					for (int i = 0; i < k; i++) {
						if (table[r][c+i] != color) {
							flag = false;
							break;
						}
					}
					if (flag) return true;
				}
	//dia 1
				if (n-c >= k-1 && n-r >= k-1) {
					bool flag = true;
					for (int i = 0; i < k; i++) {
						if (table[r+i][c+i] != color) {
							flag = false;
							break;
						}
					}
					if (flag) return true;
				}
	
	//colomn
				if (n-r >= k-1) {
					bool flag = true;
					for (int i = 0; i < k; i++) {
						if (table[r+i][c] != color) {
							flag = false;
							break;
						}
					}
					if (flag) return true;
				}
	
	//dia 2
				if (n-r >= k-1 && c >= k) {
					bool flag = true;
					for (int i = 0; i < k; i++) {
						if (table[r+i][c-i] != color) {
							flag = false;
							break;
						}
					}
					if (flag) return true;
				}
			}
		}
	}
	return false;
}

int main() {
	freopen("A_oo.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for (int ca = 1; ca <= T; ca++) {
		get_input();
		rotate();
		down();
		bool red = check_win('R'), blue = check_win('B');
		printf("Case #%d: ", ca);
		if (red && blue) {
			printf("Both");
		} else if (red) {
			printf("Red");
		} else if (blue) {
			printf("Blue");
		} else {
			printf("Neither");
		}
		printf("\n");
	}
	
	
	fclose(stdout);
    return 0;
}

