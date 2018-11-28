#include <stdio.h>
#include <string.h>

#include <iostream>

using namespace std;

int H, W;

int g[111][111];
int d[111][111];
int visit[111][111];

int dr[] = {-1,  0, 0, 1};
int dc[] = { 0, -1, 1, 0};

int cc='a';

void dfs(int r, int c) {
	if(visit[r][c]) return;

	visit[r][c] = cc;
	for(int i=0;i<4;i++) {
		int nr = dr[i] + r;
		int nc = dc[i] + c;

		if( !(0<=nr && nr < H && 0<=nc && nc<W) ) continue;

		int dir = d[nr][nc];
		if(dir==-1) continue;
		int ddr = nr + dr[ dir ] ;
		int ddc = nc + dc[ dir ] ;
		if( ddr == r && ddc == c) dfs(nr, nc);

	}

	int dir = d[r][c];
	if(dir!=-1) {
		int nnr = r + dr[dir];
		int nnc = c + dc[dir];

		dfs(nnr, nnc);
	}
}

int main(void) {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t=1;

	int T; cin >> T;
	while(T--) {
		cc='a';
		memset(g, 0, sizeof(g));
		memset(d, -1, sizeof(d));
		memset(visit, 0, sizeof(visit));
		
		cin >> H >> W;

		for(int i=0;i<H;i++) for(int j=0;j<W;j++) cin >> g[i][j];

		for(int i=0;i<H;i++) for(int j=0;j<W;j++) {
			int mk=-1;
			int mv=INT_MAX;
			for(int k=0;k<4;k++) {
				int nr = dr[k] + i;
				int nc = dc[k] + j;

				if( !(0<=nr && nr < H && 0<=nc && nc<W) ) continue;

				if(g[nr][nc]<g[i][j] && g[nr][nc]<mv) {
					mk = k;
					mv = g[nr][nc];
				}
			}
			d[i][j] = mk;
		}

		for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(!visit[i][j]) { dfs(i, j); cc++; }

		printf("Case #%d:\n", t++);

		for(int i=0;i<H;i++) {
			for(int j=0;j<W;j++) {
				if(j) printf(" ");
				printf("%c", visit[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}