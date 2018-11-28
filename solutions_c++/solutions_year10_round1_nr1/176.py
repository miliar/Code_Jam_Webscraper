#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int TT;
int N,K;
char board[64][64];
char aux[64][64];
void rotate() {
	for(int i=0;i<N;i++) {
		for(int j=0;j<N;j++)
			aux[i][j]=board[N-j-1][i];
	}
	memcpy(board,aux,sizeof(board));

}
void gravidade() {
	for(int i=N-1;i>=0;i--) {
		for(int j=0;j<N;j++) if(board[i][j]=='.') {
			for(int k=i-1;k>=0;k--) {
				if(board[k][j]!='.') {
					swap(board[k][j],board[i][j]);
					break;
				}
			}
		}
	}
}
int dx[]={1,0,1,-1};
int dy[]={0,1,1,1};

int checa(int i,int j) {
	int ans=0;
	for(int k=0;k<4;k++) {
		char ult='.';
		int seq=0;

		for(int y=i,x=j;y>=0 and y<N and x>=0 and x<N;y+=dy[k],x+=dx[k]) {
			if(board[y][x]!=ult) {
				ult=board[y][x];
				seq=1;
			}
			else {
				seq++;
				if(ult=='R' and seq>=K)
					ans|=1;
				if(ult=='B' and seq>=K)
					ans|=2;
			}
		}
	}
	return ans;
}
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		scanf("%d %d",&N,&K);
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++) {
				scanf(" %c",&board[i][j]);
			}
		rotate();
		gravidade();
		int ans=0;
		for(int i=0;i<N;i++) {
			ans |=checa(i,0);
			ans |= checa(0,i);
			ans |= checa(i,N-1);
			ans |= checa(N-1,i);
		}
		printf("Case #%d: ",T);
		if(ans==0)
			printf("Neither");
		else if(ans==1)
			printf("Red");
		else if(ans==2)
			printf("Blue");
		else if(ans==3)
			printf("Both");
		printf("\n");
	}
	return 0;
}
