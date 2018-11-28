#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

const int MAX = 110;
int H, W;
int alt[MAX][MAX];
bool g[MAX][MAX][4];
char color[MAX][MAX];

int dr[4]={-1,0,0,1};
int dc[4]={0,-1,1,0};
int rev[4]={3,2,1,0};

bool valid( int r, int c ){	return (r>=0 && r<H && c>=0 && c<W);	}

void dfs(int r, int c, char cc ){
	int i, lr, lc;
	color[r][c] = cc;
	for(i=0;i<4;++i){
		if( g[r][c][i]==0 )	continue;
		lr = r + dr[i];
		lc = c + dc[i];
		if( !valid(lr,lc) || color[lr][lc]!=0 ){
			assert( color[lr][lc]==cc );
			continue;
		}
		dfs( lr, lc, cc );
	}
}

int main(){
	//freopen("B-large.in","r",stdin);
	
	int turn, T;
	scanf("%d",&T);
	for(turn=0;turn<T;++turn){
		scanf("%d%d",&H,&W);
		int i, j, k, lr, lc;
		for(i=0;i<H;++i)	for(j=0;j<W;++j)	scanf("%d",&alt[i][j]);
		memset( g, 0, sizeof(g) );
		for(i=0;i<H;++i)	for(j=0;j<W;++j){
			int dir = -1, min = alt[i][j];
			for(k=0;k<4;++k){
				lr = i + dr[k];
				lc = j + dc[k];
				if( !valid(lr,lc) )	continue;
				if(	min > alt[lr][lc] ){
					dir = k;
					min = alt[lr][lc];
				}
			}
			if( dir==-1 )	continue;
			g[i][j][dir] = 1;
			lr = i + dr[dir];
			lc = j + dc[dir];
			g[lr][lc][ rev[dir] ] = 1;
		}
		memset( color, 0, sizeof(color) );
		char cc = 'a';
		for(i=0;i<H;++i)	for(j=0;j<W;++j){
			if( color[i][j]!=0 )	continue;
			dfs( i, j, cc ); 
			++cc;
		}
		printf("Case #%d:\n",1+turn);
		for(i=0;i<H;++i){
			putchar(color[i][0]);
			for(j=1;j<W;++j)	printf(" %c",color[i][j]);
			putchar('\n');
		}
	}
	return 0;
}
