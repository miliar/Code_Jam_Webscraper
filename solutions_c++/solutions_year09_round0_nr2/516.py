/*
 * GCJ_B.cpp
 *
 *  Created on: 2009-9-3
 *      Author: yaoman
 */

#include <stdio.h>
#include <string.h>

const int step[4][2] = { {-1,0},{0,-1},{0,1},{1,0} };

int map[101][101],h,w;
char str[110][110],ch;

char DFS(int x, int y){
	int hight,i,xx,yy,nx,ny;
	if (str[x][y]!=' ') return str[x][y];
	hight = map[x][y];
	for (i=0; i<4; i++){
		xx = x+step[i][0]; yy = y+step[i][1];
		if (xx<0 || xx>=h || yy<0 || yy>=w) continue;
		if (map[xx][yy]<hight){
			hight = map[xx][yy];
			nx = xx; ny = yy;
		}
	}
	if (hight<map[x][y]) return str[x][y] = DFS(nx,ny);
	else return str[x][y] = ch++;
}

int main(){
	int t,k,i,j;
	freopen("B-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	scanf("%d",&t);
	for (k=1; k<=t; k++){
		scanf("%d%d",&h,&w);
		for (i=0; i<h; i++){
			for (j=0; j<w; j++){
				scanf("%d",&map[i][j]);
			}
		}
		ch = 'a';
		memset(str,' ',sizeof(str));
		for (i=0; i<h; i++){
			for (j=0; j<w; j++){
				DFS(i,j);
			}
		}
		printf("Case #%d:\n",k);
		for (i=0; i<h; i++){
			for (j=0; j<w; j++){
				if (j) printf(" ");
				printf("%c",str[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
