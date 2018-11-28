
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <deque>
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

char bo[5][5];

int dir[4][2] = {0,1, -1,0, 1,1, 1,-1};

bool check(char ch) {
	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
			for(int in=0;in<4;in++) {
				int num = 0;
				for(int d=0;d<4;d++) {
					int ti = i+dir[in][0] * d;
					int tj = j+dir[in][1] * d;
					if(ti<0 || ti>=4 || tj<0 || tj>=4) continue;
					if(bo[ti][tj] == ch || bo[ti][tj] == 'T') num++;
				}
				if(num == 4) return true; 
			}
		}
	}
	return false;
}

int main() {
	freopen("E:/TDDOWNLOAD/A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, Te=1;
	scanf("%d", &T);
	while(T--) {
		for(int i=0;i<4;i++) scanf(" %s", bo[i]);

		printf("Case #%d: ", Te++);
		if(check('X')) {
			puts("X won");
			continue;
		}
		if(check('O')) {
			puts("O won");
			continue;
		}
		bool em = false;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(bo[i][j]=='.') em = true;
		if(em) puts("Game has not completed");
		else puts("Draw");
	}
}