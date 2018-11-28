#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define i64 __int64
#define INF 1e10
#define EPS 1e-11
#define SIZE 105
#define MOD 10007

char f[SIZE][SIZE];
int nway[SIZE][SIZE];

int moves[][2] = {
	{2,1},{1,2}
};

int main() {
	int T,kase=1;
	scanf("%d",&T);
	int H,W,R;
	int i,j,k;
	int x,y;
	int nx,ny;

	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d %d %d",&H,&W,&R);
		memset(f,0,sizeof(f));
		memset(nway,0,sizeof(nway));

		rep(i,R) {
			scanf(" %d %d",&x,&y);
			f[x][y] = 1;
		}
		nway[1][1] = 1;

		for(i=1;i<=H;i++) {
			for(j=1;j<=W;j++) {
				rep(k,2) {
					nx = i + moves[k][0], ny = j + moves[k][1];
					if(nx < 1 || ny < 1 || nx > H || ny > W || f[nx][ny]) continue;
					nway[nx][ny] = (nway[nx][ny] + nway[i][j]) % MOD;
				}
			}
		}
		printf("%d\n",nway[H][W]);
	}
	return 0;
}