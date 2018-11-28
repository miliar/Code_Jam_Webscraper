#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define maxn 58

char map[maxn][maxn],ch;
int flag[maxn][maxn];
int T,zu,R,C;

int process(){
	int i,j,tem;
	memset(flag,0,sizeof(flag));
	for (i = 1; i <= R; i++)
		for (j = 1; j <= C; j++){
			if (map[i][j] == '#' && flag[i][j] == 0){
				if (i >= R || j >= C || (map[i][j+1] != '#' || map[i+1][j] != '#' || map[i+1][j+1] != '#')) return 0;
				flag[i][j] = 1; flag[i][j+1] = 2; flag[i+1][j] = 3; flag[i+1][j+1] = 4;
			}
		}
	return 1;
}

void print(){
	int i,j,tem;
	printf("Case #%d:\n",zu);
	for (i = 1; i <= R; i++){
		for (j = 1; j <= C; j++){
			if (flag[i][j] == 0) printf(".");
			if (flag[i][j] == 1) printf("/");
			if (flag[i][j] == 2) printf("\\");
			if (flag[i][j] == 3) printf("\\");
			if (flag[i][j] == 4) printf("/");
		}
		printf("\n");
	}
}

int main(){
	int i,j,tem,ans;
	char st[5];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for (zu = 1; zu <= T; zu++){
		scanf("%d%d",&R,&C);
		scanf("%c",&ch);
		for (i = 1; i <= R; i++){
			for (j = 1; j <= C; j++)
				scanf("%c",&map[i][j]);
			gets(st);
		}
		ans = process();
		if (ans == 0) printf("Case #%d:\nImpossible\n",zu);
		else print();
	}
	return 0;
}