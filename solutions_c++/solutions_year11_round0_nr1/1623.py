/*
 * gcj.cpp
 *
 *  Created on: 2011-5-7
 *      Author: kokopelli
 */

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int robot[105];
int button[105];

char in[105][105][105];
int f[105][105][105];

struct _Q{
	int x, y, z;
	_Q(int _x = 0, int _y = 0, int _z = 0){
		x = _x; y = _y; z = _z;
	}
};

int mymin(int a, int b){
	if (a==-1) return b;
	if (b==-1) return a;
	return (a < b? a: b);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; cin >>T;
	int cas = 1;
	while(T--){
		int N; cin >> N;
		for (int i = 1; i <= N; i++)
		{
			string r;
			int p;
			cin>>r>>p;
			if(r=="O")
				robot[i] = 0;
			else
				robot[i] = 1;
			button[i] = p;
		}
		memset(in, 0, sizeof(in));
		memset(f, -1, sizeof(f));
		f[1][1][0] = 0;
		queue<_Q> Q;
		Q.push(_Q(1, 1, 0));
		while (!Q.empty()){
			_Q now = Q.front(); Q.pop();
			in[now.x][now.y][now.z] = 0;
			if (now.z == N) continue;
			if(robot[now.z + 1] == 0){
				if (button[now.z + 1] == now.x){
					for (int i = -1; i <= 1; i++){
						if (now.y + i >= 1 && now.y + i <= 100 && (f[now.x][now.y + i][now.z + 1] == -1 || f[now.x][now.y + 1][now.z + 1] > f[now.x][now.y][now.z] + 1)){
							f[now.x][now.y + i][now.z + 1] = f[now.x][now.y][now.z] + 1;
							if (!in[now.x][now.y + i][now.z + 1]){
								in[now.x][now.y + i][now.z + 1] = 1;
								Q.push(_Q(now.x, now.y + i, now.z + 1));
							}
						}
					}
				}
			}
			if (robot[now.z + 1] == 1){
				if (button[now.z + 1] == now.y){
					for (int i = -1; i <= 1; i++){
						if (now.x + i >= 1 && now.x + i <= 100 && (f[now.x + i][now.y][now.z + 1] == -1 || f[now.x + i][now.y][now.z + 1] > f[now.x][now.y][now.z] + 1)){
							f[now.x + i][now.y][now.z + 1] = f[now.x][now.y][now.z] + 1;
							if (!in[now.x + i][now.y][now.z + 1]){
								in[now.x + i][now.y][now.z + 1] = 1;
								Q.push(_Q(now.x + i, now.y, now.z + 1));
							}
						}
					}
				}
			}
			for (int i = -1; i <= 1; i++)
				for (int j = -1; j <= 1; j++){
					if (now.x + i >= 1 && now.x + i <= 100 && now.y + j >= 1 && now.y + j <= 100 &&
							(f[now.x + i][now.y + j][now.z] == -1 || f[now.x + i][now.y + j][now.z] > f[now.x][now.y][now.z] + 1)){
						f[now.x + i][now.y + j][now.z] = f[now.x][now.y][now.z] + 1;
						if (!in[now.x + i][now.y + j][now.z]){
							in[now.x + i][now.y + j][now.z] = 1;
							Q.push(_Q(now.x + i, now.y + j, now.z));
						}
					}
				}
		}
		int ans = -1;
		for (int i = 1; i <=100; i++)
			for (int j = 1; j<=100; j++)
				ans = mymin(ans, f[i][j][N]);
		cout <<"Case #" << cas++<<": " << ans <<"\n";
	}
	return 0;
}
