#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define MAXH 105
#define MAXW 105
#define MAXA 100000


#define Up 1
#define Down 2
#define Left 4
#define Right 8

#define setUp(x) x |= Up
#define setDown(x) x |= Down
#define setLeft(x) x |= Left
#define setRight(x) x |= Right
#define testUp(x) (x)&Up
#define testDown(x) (x)&Down
#define testLeft(x) (x)&Left
#define testRight(x) (x)&Right


int cases, h, w, tab[MAXH][MAXW], dir[MAXH][MAXW], ans[MAXH][MAXW];
int ansnum;

void dfs(int x, int y) {
	ans[x][y] = ansnum;
	if ((dir[x][y] & Up) && (ans[x-1][y]==0)) { dfs(x-1,y); }
	if ((dir[x][y] & Down) && (ans[x+1][y]==0)) { dfs(x+1,y); }
	if ((dir[x][y] & Left) && (ans[x][y-1]==0)) { dfs(x,y-1); }
	if ((dir[x][y] & Right)&& (ans[x][y+1]==0)) { dfs(x,y+1); }
}

int main(int argc, char* argv[]){
	scanf("%d",&cases);
	for(int c = 1; c <= cases; c++) {
		for(int i = 0; i < MAXH; i++) for(int j = 0; j < MAXW; j++) tab[i][j] = MAXA;
		scanf("%d %d",&h,&w);
		for(int i = 1; i <= h; i++)
			for(int j = 1; j <= w; j++){
				scanf("%d",&tab[i][j]);
				dir[i][j] = ans[i][j] = 0;
			}

		for(int i = 1; i <= h; i++) {
			for(int j = 1; j <= w; j++) {
				int d = Up, v = tab[i-1][j];
				if(tab[i][j-1] < v) d = Left, v = tab[i][j-1];
				if(tab[i][j+1] < v) d = Right,v = tab[i][j+1];
				if(tab[i+1][j] < v) d = Down, v = tab[i+1][j];
				if (v < tab[i][j]) {
					if (d == Up) dir[i-1][j] |= Down, dir[i][j] |= Up;
					else if(d == Down) dir[i+1][j] |= Up, dir[i][j] |= Down;
					else if(d == Left) dir[i][j-1] |= Right, dir[i][j] |= Left;
					else if(d == Right)dir[i][j+1] |= Left, dir[i][j] |= Right;
				}
			}
		}

		ansnum = 1;
		for(int i = 1; i <= h; i++){
			for(int j = 1; j <= w; j++){
				if(ans[i][j]==0) {
					dfs(i,j);
					ansnum++;
				}
			}
		}
		printf("Case #%d:\n",c);
		for(int i = 1; i<= h; i++) {
			for(int j = 1; j <= w; j++) {
		//		printf("%d ",ans[i][j]);
				printf("%s%c",j==1?"":" ",'a'+(ans[i][j]-1));
			}
			puts("");
		}
	}
	return 0;
}

