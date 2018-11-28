#include<string>
#include<algorithm>
#include<memory>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define cs c_str()
#define sz size()
int H,W;
int dat[128][128];
int chk[128][128];
int cnt;
char mark[128][128];
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
// N, W, E, S
bool valid(int x, int y) {
	return x>=0 && y>=0 && x<H && y<W;
}
int dfs(int x, int y) {
	if(chk[x][y]) return chk[x][y];
	int min1 = dat[x][y], nx, ny;
	FOR(k,0,4) {
		int px = x + dx[k];
		int py = y + dy[k];
		if(valid(px, py) && dat[px][py] < min1) {
			min1 = dat[px][py];
			nx = px;
			ny = py;
		}
	}
	if(min1 == dat[x][y]) { // sink
		return chk[x][y] = ++cnt;
	}
	return chk[x][y] = dfs(nx, ny);
}
void doit() {
	cnt = 0;
	memset(chk, 0, sizeof (chk));
	FOR(i,0,H)
		FOR(j,0,W) {
			if(chk[i][j]==0) {
				dfs(i, j);
			}
		} 
	FOR(i,0,H)
		FOR(j,0,W) 
			mark[i][j] = chk[i][j] + 'a' - 1;
}

int main() {
	freopen("B.in","r",stdin);
	int T, e = 0;
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d",&H,&W);
		FOR(i,0,H)
			FOR(j,0,W)
				scanf("%d",&dat[i][j]);
		doit();
		printf("Case #%d:\n",++e);
		FOR(i,0,H) {
			FOR(j,0,W)
				printf("%c ",mark[i][j]);
			printf("\n");
		}
	}
	return 0;
}
