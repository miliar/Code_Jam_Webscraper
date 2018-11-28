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

int X,Y;
char g[17][17];

typedef struct S { int x,y,px,py,pd,cost; } S;
bool operator<(const S &a,const S &b) { return a.cost>b.cost; }
int best[17][17][17][17][4];
int move[17][17][17][17];

const int DX[]={0,+1,0,-1},DY[]={+1,0,-1,0};

void calcmove() {
	REP(sx,X) REP(sy,Y) {
		REP(xx,X) REP(yy,Y) move[sx][sy][xx][yy]=INT_MAX;
		if(g[sx][sy]=='#') continue;
		queue<pair<int,int> > q;
		#define ADD1(x,y,cost) if(cost<move[sx][sy][x][y]) move[sx][sy][x][y]=cost,q.push(MP(x,y));
		ADD1(sx,sy,0);
		while(!q.empty()) {
			int x=q.front().first,y=q.front().second; q.pop(); int cost=move[sx][sy][x][y];
			REP(d,4) {
				int nx=x+DX[d],ny=y+DY[d];
				if(g[nx][ny]=='#') continue;
				ADD1(nx,ny,cost+1);
			}
		}
	}
}

void run(int casenr) {
	scanf("%d%d",&X,&Y);
	memset(g,'#',sizeof(g));
	FORE(x,1,X) FORE(y,1,Y) do { scanf("%c",&g[x][y]); } while(g[x][y]!='.'&&g[x][y]!='#'&&g[x][y]!='X'&&g[x][y]!='O');
	X+=2,Y+=2;
//	REP(x,X) { REP(y,Y) printf("%c",g[x][y]); puts(""); }
	int sx=-1,sy=-1; REP(x,X) REP(y,Y) if(g[x][y]=='O') sx=x,sy=y,g[x][y]='.'; assert(sx!=-1&&sy!=-1);
	int tx=-1,ty=-1; REP(x,X) REP(y,Y) if(g[x][y]=='X') tx=x,ty=y,g[x][y]='.'; assert(tx!=-1&&ty!=-1);
	int spx=sx,spy=sy; while(g[spx][spy]=='.') spx+=DX[0],spy+=DY[0];
	
	calcmove();
	
	memset(best,-1,sizeof(best));
	priority_queue<S> q;
	#define ADD2(x,y,px,py,pd,cost) if(best[x][y][px][py][pd]==-1||cost<best[x][y][px][py][pd]) best[x][y][px][py][pd]=cost,q.push((S){x,y,px,py,pd,cost});
	ADD2(sx,sy,spx,spy,0,0);
	while(!q.empty()) {
		int x=q.top().x,y=q.top().y,px=q.top().px,py=q.top().py,pd=q.top().pd,cost=q.top().cost; q.pop();
		if(cost>best[x][y][px][py][pd]) continue;
//		printf("%d %d %d %d %d = %d\n",x,y,px,py,pd,cost);
		if(x==tx&&y==ty) {
			printf("Case #%d: %d\n",casenr,cost);
			return;
		}
		REP(d,4) {
			//move
			int nx=x+DX[d],ny=y+DY[d];
			if(g[nx][ny]!='#') ADD2(nx,ny,px,py,pd,cost+1);
				
			//shoot
			int npx=x,npy=y;
			while(g[npx][npy]=='.') npx+=DX[d],npy+=DY[d];
			//shoot and replace
			ADD2(x,y,npx,npy,d,cost);
			//shoot and move to new and portal
			assert(move[x][y][npx-DX[d]][npy-DY[d]]!=INT_MAX);
			ADD2(px-DX[pd],py-DY[pd],npx,npy,d,cost+move[x][y][npx-DX[d]][npy-DY[d]]+1);
			//shoot and move to old and portal
			assert(move[x][y][px-DX[pd]][py-DY[pd]]!=INT_MAX);
			ADD2(npx-DX[d],npy-DY[d],px,py,pd,cost+move[x][y][px-DX[pd]][py-DY[pd]]+1);
		}
	}
	printf("Case #%d: THE CAKE IS A LIE\n",casenr);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}
