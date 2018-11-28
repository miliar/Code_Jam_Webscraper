#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

int N,M,P;
char board[5][5];
int tot[5][5];

void solve(int t) {
	int i,j,x,y,p,ans=0;
	scanf("%d %d",&N,&M);
	for(i=0;i<N;i++) scanf("%s",board[i]);
	P = N*M;
	for(p=0;p<(1<<P);p++) {
		for(i=0;i<N;i++) {
			for(j=0;j<M;j++) {
				tot[i][j] = 0;
			}
		}
		int ok = 1;
		for(i=0;i<N;i++) {
			for(j=0;j<M;j++) {
				int dir = (p>>(i*M+j))&1;
				if(board[i][j] == '-') {
					x = i;
					y = dir?j-1:j+1;
				}
				if(board[i][j] == '|') {
					x = dir?i-1:i+1;
					y = j;
				}
				if(board[i][j] == '\\') {
					x = dir?i-1:i+1;
					y = dir?j-1:j+1;
				}
				if(board[i][j] == '/') {
					x = dir?i-1:i+1;
					y = dir?j+1:j-1;
				}
				if(x<0 ) x+=N;
				if(y<0 ) y+=M;
				if(x>=N) x-=N;
				if(y>=M) y-=M;
				tot[x][y]++;
				if(tot[x][y] > 1) ok = 0;
			}
		}
		ans+=ok;
	}
	
	
	printf("Case #%d: %d\n",t,ans%1000003);
}

int main() {
	int t,T;
	double sec, tot;
	scanf("%d",&T);
	for(t=1;t<=T;t++) solve(t);
	return 0;
}
