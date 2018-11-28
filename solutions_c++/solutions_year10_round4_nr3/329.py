#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAX 105

char g[2][MAX][MAX];


int main() {
	int T,kase = 1;
	int i,j,k;
	int x1, x2, y1, y2;
	bool flag;
	int x,y;
	int R;
	scanf("%d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf("%d",&R);
		x = 0, y = 1;
		rep(i,101) rep(j,101) g[x][i][j] = g[y][i][j] = 0;
		rep(k,R) {
			scanf(" %d %d %d %d",&x1, &y1, &x2, &y2);
			for(i = x1; i <=x2; i++) for(j=y1;j<=y2;j++) g[x][i][j] = 1;
		}
		k = 0;
		while(1) {
			k++;
			flag = false;
			rep(i,101) rep(j,101) g[y][i][j] = g[x][i][j];
			for(i=1;i<=100;i++) for(j=1;j<=100;j++) {
				if(g[x][i][j] == 1) {
					if(g[x][i-1][j] == 0 && g[x][i][j-1] == 0) g[y][i][j] = 0;
					else flag = 1;
				}
				if(g[x][i][j] == 0) {
					if(g[x][i-1][j] == 1 && g[x][i][j-1] == 1) { g[y][i][j] = 1; flag = 1; }
				}
			}
			swap(x,y);
			if(!flag) break;
		}
		printf("%d\n",k);
	}
	return 0;
}