#include <cstdio>
#include <algorithm>
#define PI pair<int,int>
#define INF 1000000000
#define st first
#define nd second
using namespace std;


int n,m,ntc,c=1;
int T[200][200];
pair<int,int> X[200][200];
bool V[200][200];
char R[200][200];
PI KK[] = { PI(-1,0), PI(0,-1), PI(0,1),PI(1,0) };

PI dfs(int x, int y) {
	if(V[x][y]) return X[x][y];
	int a=x, b=y;
	V[x][y]=1;
	for(int i=0; i<4; ++i)
		if(T[x+KK[i].st][y+KK[i].nd] < T[a][b]) { a = x+KK[i].st; b = y+KK[i].nd; }
    PI res;
	if(a==x && b==y) res=PI(a,b);
	else res=dfs(a,b);
	X[x][y]=res;
	return res;
}




int main() {
	scanf("%d", &ntc);
	for(int xx=1; xx<=ntc; ++xx) {
		scanf("%d %d", &n, &m);
		for(int i=1; i<=n; ++i)
			for(int j=1; j<=m; ++j)
				scanf("%d", &T[i][j]);
		for(int i=0; i<=m+1; ++i) { T[0][i]=INF; T[n+1][i]=INF; }
        for(int i=0; i<=n+1; ++i) { T[i][0]=INF; T[i][m+1]=INF; }
		for(int i=1; i<=n; ++i)
			for(int j=1; j<=m; ++j) {
				if(V[i][j]) continue;
				dfs(i,j);
			}
		printf("Case #%d:\n",xx);
		for(int i=1; i<=n; ++i) {
			for(int j=1; j<=m; ++j) {
				PI q=X[i][j];
				if(!R[q.st][q.nd]) R[q.st][q.nd]=c++;
				printf("%c ", 'a'+R[q.st][q.nd]-1);
			}
			printf("\n");
		}
		c=1;
		for(int i=1; i<=n; ++i)
			for(int j=1; j<=m; ++j) {
				V[i][j]=0; R[i][j]=0;
			}

	}
}
