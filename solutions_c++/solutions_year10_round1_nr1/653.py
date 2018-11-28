#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>

#define NONE 0
#define RED 1
#define BLUE 2

int N;

inline int EXIST(int x,int y)
{
	return 0<=x && x<N && 0<=y && y<N;
}

int main()
{
	int t;
	int T;
	int i,j,k;
	int Rwin,Bwin;
	scanf("%d\n",&T);
	for (t=0;t<T;t++){
		int K;
		Rwin=Bwin=0;
		scanf("%d %d\n",&N,&K);
		char board[N][N];//x,y
		//読む段階で回しておく
		for (i=N-1;i>=0;i--){
			for (j=0;j<N;j++){
				char c;
				scanf("%c ",&c);
				if (c=='R')board[i][j]=RED;
				else if (c=='B')board[i][j]=BLUE;
				else board[i][j]=NONE;
			}
		}
		/*for (i=0;i<N;i++){
			for (j=0;j<N;j++){
				if (board[j][i]==RED)printf("R");
				else if (board[j][i]==BLUE)printf("B");
				else printf(".");
			}
			printf("\n");
		}
		printf("\n");*/
		//落ちるのを考慮する
		for (i=0;i<N;i++){
			for (j=N-1;j>=0;j--){
				while (1){
					if (board[i][j]!=NONE)break;
					int all_none=1;
					for (k=j;k>=1;k--){
						if (board[i][k-1]!=NONE)all_none=0;
						board[i][k]=board[i][k-1];
					}
					board[i][0]=NONE;
					if (all_none)break;
				}
			}
		}
		/*for (i=0;i<N;i++){
			for (j=0;j<N;j++){
				if (board[j][i]==RED)printf("R");
				else if (board[j][i]==BLUE)printf("B");
				else printf(".");
			}
			printf("\n");
		}*/
		//並んだかどうか確認
		int check;
		int win;
		check=RED;win=0;
		for (i=0;i<N;i++){
			for (j=0;j<N;j++){
				//横並び
				for (k=0;k<K;k++){
					if (!EXIST(j+k,i))break;
					if (board[j+k][i]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok1;
				}
				//縦並び
				for (k=0;k<K;k++){
					if (!EXIST(j,i+k))break;
					if (board[j][i+k]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok1;
				}
				//ななめ1
				for (k=0;k<K;k++){
					if (!EXIST(j+k,i+k))break;
					if (board[j+k][i+k]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok1;
				}
				//ななめ2
				for (k=0;k<K;k++){
					if (!EXIST(j+k,i-k))break;
					if (board[j+k][i-k]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok1;
				}
			}
		}
ok1:
		Rwin=win;
		check=BLUE;win=0;
		for (i=0;i<N;i++){
			for (j=0;j<N;j++){
				//横並び
				for (k=0;k<K;k++){
					if (!EXIST(j+k,i))break;
					if (board[j+k][i]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok2;
				}
				//縦並び
				for (k=0;k<K;k++){
					if (!EXIST(j,i+k))break;
					if (board[j][i+k]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok2;
				}
				//ななめ1
				for (k=0;k<K;k++){
					if (!EXIST(j+k,i+k))break;
					if (board[j+k][i+k]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok2;
				}
				//ななめ2
				for (k=0;k<K;k++){
					if (!EXIST(j+k,i-k))break;
					if (board[j+k][i-k]!=check)break;
				}
				if (k==K){
					win=1;
					goto ok2;
				}
			}
		}
ok2:
		Bwin=win;
		//結果を出す
		if (Rwin && Bwin){
			printf("Case #%d: Both\n",t+1);
		}
		else if (Rwin){
			printf("Case #%d: Red\n",t+1);
		}
		else if (Bwin){
			printf("Case #%d: Blue\n",t+1);
		}
		else{
			printf("Case #%d: Neither\n",t+1);
		}
	}
	return 0;
}
