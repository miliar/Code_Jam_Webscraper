#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long int64;

int R, C, D;

const int MAX_N = 509;
int N;
char buf[MAX_N];
int64 board[2][2][MAX_N+8][MAX_N+8];
int64 BIT[2][2][MAX_N+8][MAX_N+8];

//1-originの場合。0-originの場合はindexをincする(下参照)。
int64 sum(int x, int y, int pat, int which){
	int64 ret = 0;
	for(int a=x;a;a-=a&-a){
		for(int b=y;b;b-=b&-b){
			ret += BIT[pat][which][a][b];
		}
	}
	return ret;
}

int64 sum(int x1, int y1, int x2, int y2, int pat, int which){
	return sum(x2,y2,pat,which) - sum(x2,y1-1,pat,which) - sum(x1-1,y2,pat,which) + sum(x1-1,y1-1, pat, which);
}

void add(int x, int y, int64 val, int pat, int which){
	for(int a=x;a<=MAX_N;a+=a&-a){
		for(int b=y;b<=MAX_N;b+=b&-b){
			BIT[pat][which][a][b] += val;
		}
	}
}

int solve(){
	for(int k=min(R,C); k>=3; k--){
		for(int i=1; i+k-1<=R; i++){
			for(int j=1; j+k-1<=C; j++){
				int64 x1 = 2*(sum(i,j,i+k-1,j+k-1,0,0) - board[0][0][i][j] - board[0][0][i][j+k-1] - board[0][0][i+k-1][j] - board[0][0][i+k-1][j+k-1]),
						y1 = 2*(sum(i,j,i+k-1,j+k-1,0,1) - board[0][1][i][j] - board[0][1][i][j+k-1] - board[0][1][i+k-1][j] - board[0][1][i+k-1][j+k-1]);
				int64 x2 = (2*i+k-1)*(sum(i,j,i+k-1,j+k-1,1,0) - board[1][0][i][j] - board[1][0][i][j+k-1] - board[1][0][i+k-1][j] - board[1][0][i+k-1][j+k-1]),
						y2 = (2*j+k-1)*(sum(i,j,i+k-1,j+k-1,1,1) - board[1][1][i][j] - board[1][1][i][j+k-1] - board[1][1][i+k-1][j] - board[1][1][i+k-1][j+k-1]);
				if(x1==x2 && y1==y2){
					return k;
				}
			}
		}
	}
	return 0;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){
		for(int i=0; i<=MAX_N; i++)for(int j=0; j<=MAX_N; j++)for(int k=0; k<2; k++)for(int l=0; l<2; l++){
			BIT[k][l][i][j] = 0;
			board[k][l][i][j] = 0;
		}
		scanf("%d%d%d ",&R,&C,&D);
		fflush(stdout);
		for(int i=0; i<R; i++){
			scanf(" %s ",buf);
			for(int j=0; j<C; j++){
				board[0][0][i+1][j+1] = (i+1)*((int64)D+buf[j]-'0');
				add(i+1, j+1, (i+1)*((int64)D+buf[j]-'0'), 0, 0);
				board[0][1][i+1][j+1] = (j+1)*((int64)D+buf[j]-'0');
				add(i+1, j+1, (j+1)*((int64)D+buf[j]-'0'), 0, 1);
				board[1][0][i+1][j+1] = ((int64)D+buf[j]-'0');
				add(i+1, j+1, D+buf[j]-'0', 1, 0);
				board[1][1][i+1][j+1] = ((int64)D+buf[j]-'0');
				add(i+1, j+1, D+buf[j]-'0', 1, 1);
			}
		}
		printf("Case #%d: ",c);
		int ans = solve();
		if(ans){
			printf("%d\n",ans);
		}
		else{
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
