#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <math.h>

using namespace std;

char buffer[1024];
int dir[][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int map[102][102], move[102][102];
char basin[102][102];
bool ch;
bool valpos(int i, int j , int n, int m) {
	return i >= 0 && i < n && j >= 0 && j < m;
}
char dfs(int i, int j, char ba) {
	if(basin[i][j] != -1)
		return basin[i][j];
	if(move[i][j] == -1) {
		basin[i][j] = ba;
		ch = true;
	}
	else
		basin[i][j] = dfs(i + dir[move[i][j]][0], j + dir[move[i][j]][1], ba);
	return basin[i][j];
}
int main() {
	int numtests, h, w, ni, nj, lower;
	char ba;
	scanf("%d\n",&numtests);
	for(int t = 1; t <= numtests; ++t) {
		scanf("%d %d\n",&h,&w);
		for(int i = 0; i < h; ++i)
			for(int j = 0; j < w; ++j)
				scanf("%d",&map[i][j]);
		for(int i = 0; i < h; ++i)
			for(int j = 0; j < w; ++j) {
				move[i][j] = -1;
				lower = INT_MAX;
				for(int k = 0; k < 4; ++k) {
					ni = i + dir[k][0];
					nj = j + dir[k][1];
					if(valpos(ni,nj,h,w) && map[ni][nj] < map[i][j] && map[ni][nj] < lower) {
						move[i][j] = k;
						lower = map[ni][nj];
					}
				}
			}
		memset(basin,-1,sizeof(basin));
		ba = 'a';
		for(int i = 0; i < h; ++i)
			for(int j = 0; j < w; ++j) {
				if(basin[i][j] == -1) {
					ch = false;
					dfs(i,j,ba);
					if(ch == true)
						++ba;
				}
			}
		cout << "Case #" << t << ": " << endl;
		for(int i = 0; i < h; ++i) {
			for(int j = 0; j < w - 1; ++j)
				cout << basin[i][j] << ' ';
			cout << basin[i][w - 1] << endl;
		}
	}
	return 0;
}
