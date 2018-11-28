//============================================================================
// Name        : code.cpp
// Author      : huhao
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <string>
#include <algorithm>
using namespace std;

char maze[101][101];
char buf[101][101];
void Rotate(int n) {
	for (int i = 0 ; i < n ; i ++) {
		for (int j = 0 ; j < n ; j ++) {
			buf[i][j] = maze[n-j-1][i];
		}
	}
	for (int i = 0 ; i < n ; i ++) {
		for (int j = 0 ; j < n ; j ++) {
			maze[i][j] = buf[i][j];
		}
	}
}

void Gravity(int n) {
	for (int i = 0 ; i < n ; i ++) {
		int k = n - 1;
		for (int j = n - 1; j >= 0 ; j --) {
			if(maze[j][i] != '.') {
				maze[k][i] = maze[j][i];
				k --;
			}
		}
		for (int j = 0 ; j <= k; j ++) {
			maze[j][i] = '.';
		}
	}
}

bool vis[101][101][4];

int dx[] = {1,0,1,1};
int dy[] = {0,1,1,-1};

bool In(int x,int y,int n) {
	return (x >= 0 && y >= 0 && x < n && y <n);
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cas = 1;
	while(T --) {
		int K , N;
		scanf("%d%d",&N,&K);
		for (int i = 0 ; i < N ; i ++) {
			scanf("%s",maze[i]);
		}
		Rotate(N);
		Gravity(N);
		memset(vis,false,sizeof(vis));
		bool red = false;
		bool blue = false;
		for (int i = 0 ; i < N ; i ++) {
			for (int j = 0 ; j < N ; j ++) {
				if(maze[i][j] != '.') {
					if(maze[i][j] == 'R' && red) continue;
					if(maze[i][j] == 'B' && blue) continue;
					for (int d = 0 ; d < 4 ;d ++) {
			//			if(vis[i][j][d]) continue;
						int x = i;
						int y = j;
						int cnt = 0;
						while(In(x,y,N) && maze[x][y] == maze[i][j]) {
			//				vis[i][j][d] = true;
							cnt ++;
							x += dx[d];
							y += dy[d];
						}
						if(cnt >= K) {
							if(maze[i][j] == 'R') red = true;
							if(maze[i][j] == 'B') blue = true;
						}
					}
				}
			}
		}
		printf("Case #%d: ",cas++);
		if(red && blue) {
			puts("Both");
		} else if(red) {
			puts("Red");
		} else if(blue){
			puts("Blue");
		} else {
			puts("Neither");

		}
	}
	return 0;
}