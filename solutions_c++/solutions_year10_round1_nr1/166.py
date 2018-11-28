#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
char grid[52][52], ng[52][52];
int dx[4] = {-1,1,1,0};
int dy[4] = {1,1,0,1};
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int ans = 0;
		int N,K;
		scanf("%d%d",&N,&K);
		for(int x=N-1;x>=0;--x)
			for(int y=0;y<N;++y)
				scanf("	%c",&grid[y][x]);
		memset(ng,'.',sizeof(ng));
		for(int x=0;x<N;++x) {
			int i = N-1;
			for(int y=N-1;y>=0;--y)
				if(grid[y][x] != '.') ng[i--][x] = grid[y][x];
		}
		bool rwin = 0, bwin = 0;
		for(int y=0;y<N;++y)
			for(int x=0;x<N;++x) {
				if(ng[y][x] == '.') continue;
				for(int i=0;i<4;++i) {
					int nx = x, ny = y;
					for(int s=1;s<K;++s) {
						nx += dx[i]; ny += dy[i];
						if((nx >= N || ny >= N || nx < 0 || ny < 0) || ng[ny][nx] != ng[y][x]) {
							goto end;
						}
					}
					if(ng[y][x] == 'R') rwin = 1;
					else bwin = 1;
					end:;
				}
			}
		printf("Case #%d: ",cn);
		if(rwin && bwin) printf("Both\n");
		else if(rwin) printf("Red\n");
		else if(bwin) printf("Blue\n");
		else printf("Neither\n");
	}
}
