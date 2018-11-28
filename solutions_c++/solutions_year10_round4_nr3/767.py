#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int C;
int tt = 1;
int R;

int rc[2][220][220];
int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int x1, y1, x2, y2;
	scanf("%d", &C);
	while(C--) {
		scanf("%d", &R);
		memset(rc, 0, sizeof(rc));
		for(int i = 0; i < R; ++i) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int i = y1 - 1; i < y2; ++i) {
				for(int j = x1 - 1; j < x2; ++j) {
					rc[0][i][j] = 1;
				}
			}
		}
	/*	for(int i = 0; i < 6; ++i) {
			for(int j = 0; j < 6; ++j) {
				printf("%d ", rc[0][i][j]);
			}
			printf("\n");
		}*/
		int start = 0, next = 1;
		int cnt = 1;
		int TT = 1;
		while(cnt) {
			cnt = 0;
			for(int i = 0; i < 220; ++i) {
				for(int j = 0; j < 220; ++j) {
					rc[next][i][j] = 0;
				}
			}
			for(int i = 0; i < 220; ++i) {
				for(int j = 0; j < 220; ++j) {
					if(rc[start][i][j] == 0) {
						if(i - 1 >= 0 && j - 1 >= 0) {
							if(rc[start][i - 1][j] == 1 && rc[start][i][j - 1] == 1) {
								rc[next][i][j] = 1;
								++cnt;
							}
						}
					} else {
						bool flag = false;
						if(i - 1 >= 0 && rc[start][i - 1][j] == 1) {
							flag = true;
						}
						if(j - 1 >= 0 && rc[start][i][j - 1] == 1) {
							flag = true;
						}
						if(flag) {rc[next][i][j] = 1; ++cnt;}
					}
				}
			}
			start = (start + 1) % 2;
			next = (next + 1) % 2;
			/*for(int i = 0; i < 6; ++i) {
				for(int j = 0; j < 6; ++j) {
					printf("%d ", rc[start][i][j]);
				}
				printf("\n");
			}*/
			++TT;
		}
		printf("Case #%d: %d\n", tt++, TT - 1);
		
	}
	return 0;
}