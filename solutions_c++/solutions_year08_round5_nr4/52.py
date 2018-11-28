#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define SZ(v) ((int)(v).size())
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))

const int MOD=10007;
const int DX[]={1,2},DY[]={2,1};
int X,Y,nbad;

bool bad[100][100];
int ways[100][100];

void run(int casenr) {
	scanf("%d%d%d",&X,&Y,&nbad);
	memset(bad,false,sizeof(bad));
	REP(i,nbad) { int x,y; scanf("%d%d",&x,&y); --x,--y; bad[x][y]=true; }
	
	memset(ways,0,sizeof(ways));
	ways[0][0]=1;
	REP(x,X) REP(y,Y) if(ways[x][y]>0) {
		REP(d,2) {
			int nx=x+DX[d],ny=y+DY[d];
			if(nx>=X||ny>=Y||bad[nx][ny]) continue;
			ways[nx][ny]=(ways[nx][ny]+ways[x][y])%MOD;
		}
	}	
	printf("Case #%d: %d\n",casenr,ways[X-1][Y-1]);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}
