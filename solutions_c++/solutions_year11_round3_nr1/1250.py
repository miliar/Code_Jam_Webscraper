#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

char tiles[50][50];

void solve(int t, int row, int col) {
	char buf[128];
	for(int i = 0; i < row; i++) {
		gets(buf);
		for(int j = 0; j < col; j++) {
			tiles[i][j] = buf[j];
		}
	}
	
	for(int i = 0; i < row; i++) {
		for(int j = 0; j < col; j++) {
			if(tiles[i][j] == '#') {
				if(i == row-1 || j == col-1) {
					printf("Case #%d:\nImpossible\n", t+1);
					return;
				}
				else if(tiles[i][j+1] == '#' && tiles[i+1][j+1] == '#' && tiles[i+1][j] == '#') {
					tiles[i][j] = '/';
					tiles[i][j+1] = '\\';
					tiles[i+1][j] = '\\';
					tiles[i+1][j+1] = '/';
				}
				else {
					printf("Case #%d:\nImpossible\n", t+1);
					return;
				}
			}
		}
	}
	
	printf("Case #%d:\n", t+1);
	for(int i = 0; i < row; i++) {
		for(int j = 0; j < col; j++) {
			printf("%c", tiles[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		int row, col;
		scanf("%d %d\n", &row, &col);
		//printf("%d %d\n", row,col);
		solve(i, row, col);
	}
	return 0;
}