#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define N 60

int t,T;
int n,m;
char board[N][N];

void process(){
	int i,j,flag,done;
	do{
		first:
		done = 1;
		FOR(i,1,n){
			FOR(j,1,m){
				if (board[i][j]=='#'){
					if (board[i+1][j]=='#' && board[i][j+1]=='#' && board[i+1][j+1]=='#'){
						board[i+1][j+1]=board[i][j]='/';
						board[i][j+1]=board[i+1][j]='\\';
						goto first;
					}
					else{
						done = 0;
						goto last;
					}
				}
			}
		}
		last:;
	}while(0);
	printf("Case #%d:\n",t);
	if (done){
		FOR(i,1,n){
			printf("%s\n",board[i]+1);
		}
	}
	else{
		printf("Impossible\n");
	}
}

int main(){
	freopen("a-large.in","rt",stdin);
	freopen("a-large.out","wt",stdout);
	scanf("%d",&T);
	FOR(t,1,T){
		scanf("%d %d",&n,&m);
		int i;
		memset(board,0,sizeof(board));
		FOR(i,1,n) scanf("%s",board[i]+1);
		process();
	}
	return 0;
}