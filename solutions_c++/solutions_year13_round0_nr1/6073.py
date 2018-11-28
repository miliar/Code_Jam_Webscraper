#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
//#include <map>
#include <algorithm>
#define NOT_COMPLETED -1
#define DRAW 0
#define X_WON 1
#define O_WON 2
using namespace std;
char map[5][5];
int dx[4]={-1,-1,0,1},dy[4]={0,-1,-1,-1};
int I,T;
int check() {
	int i,j,k;
	int empty=0;
	for (i=0;i<4;i++) {
		for (j=0;j<4;j++) {
			if (map[i][j]=='.') {empty++;continue;}
			for (k=0;k<4;k++) {
				int y=i+dy[k],x=j+dx[k],c=1;
				while (y>=0&&x>=0&&map[y][x]!='.' && ((map[i][j]=='T')?(map[y][x]==map[i+dy[k]][j+dx[k]]):(map[y][x]==map[i][j])) ) {
					c++;
					y+=dy[k],x+=dx[k];
				}
				if (c==4) {
					if (map[i][j]=='T') {
						if (map[i+dy[k]][j+dx[k]]=='X') return X_WON;
						else return O_WON;
					} else {
						if (map[i][j]=='X') return X_WON;
						else return O_WON;
					}
				}
			}
		}
	}
	if (empty==0) return DRAW;
	else return NOT_COMPLETED;
}
int main() {
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	for (cin >> T,I=1;I<=T;I++) {
		scanf("%s%s%s%s",map[0],map[1],map[2],map[3]);
		int ans=check();
		printf("Case #%d: ",I);
		if (ans==X_WON) printf("X won\n");
		else if (ans==O_WON) printf("O won\n");
		else if (ans==DRAW) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}
