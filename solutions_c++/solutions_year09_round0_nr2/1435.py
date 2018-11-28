#include<stdio.h>
#include<string.h>
#include<assert.h>

#define rep(i,n) for(i=0;i<(n);i++)
#define MAXR 100
#define MAXC 100

int g[MAXR+5][MAXC+5];
int R,C;
char color[MAXR+5][MAXC+5];
char ch;
int moves[][2] = { {-1,0}, {0,-1}, {0,1}, {1,0} };

char go(int r,int c) {
	int i,nr,nc,mn=100000,mnr,mnc;
	char ret;
	rep(i,4) {
		nr = r + moves[i][0];
		nc = c + moves[i][1];
		if(nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
		if(g[nr][nc] < mn) {
			mn = g[nr][nc];
			mnr = nr;
			mnc = nc;
		}
	}
	if(mn >= g[r][c]) return ch++;
	if(color[mnr][mnc] == 0) {
		ret = go(mnr,mnc);
		color[mnr][mnc] = ret;
		return ret;
	}
	else return color[mnr][mnc];
}

int main() {
	int i,j,T,kase=1,ret;
	scanf("%d",&T);
	while(T--) {
		scanf(" %d %d",&R,&C);
		rep(i,R) rep(j,C) scanf(" %d",&g[i][j]);
		printf("Case #%d:\n",kase++);
		memset(color,0,sizeof(color));
		ch = 'a';
		rep(i,R) rep(j,C) if(color[i][j] == 0) {
			ret = go(i,j);
			color[i][j] = ret;
		}
		rep(i,R) {
			rep(j,C) {
				if(j > 0) printf(" ");
				printf("%c",color[i][j]);
			}printf("\n");
		}
		assert(ch <= 'z'+1);

	}
	return 0;
}