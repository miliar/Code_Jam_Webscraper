#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/
#define X first

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))


/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

const int MAX = 17;
int pole[MAX][MAX];
int dx[] = { -1, 0, 1, 0 } , dy[] = { 0, 1, 0, -1 };

unsigned char vis[MAX][MAX][MAX+1][MAX+1][4][MAX+1][MAX+1][4];
int dst[MAX][MAX][MAX][MAX][4][MAX][MAX][4];
int N, M;

struct E{
	char x,y, ax, ay,az, bx,by, bz;
	int d;
	E(char _x, char _y, char _ax, char _ay, char _az, char _bx, char _by, char _bz, int _d) :
		x(_x), y(_y), ax(_ax), ay(_ay), az(_az), bx( _bx), by(_by), bz(_bz), d(_d) {}
	bool operator<(const E &a) const {
		return d > a.d;
	}
};

#define OK(x, y) ( (x) >= 1 && (x) <= N && (y) >= 1 && (y) <= M)
#define ADD(x, y, ax,ay,az, bx,by,bz) do{  \
			if(OK(x,y) && (pole[x][y] == 0) && (vis[(x)][(y)][(ax)][(ay)][(az)][(bx)][(by)][(bz)] != CNT || dst[x][y][ax][ay][az][bx][by][bz]>d+1)) {	\
			   vis[(x)][(y)][(ax)][(ay)][(az)][(bx)][(by)][(bz)] = CNT;\
			   dst[(x)][(y)][(ax)][(ay)][(az)][(bx)][(by)][(bz)] = d + 1; \
			   q.push( E( (x), (y), (ax), (ay), (az), (bx), (by), (bz), d+1 ));\
			} \
			}while(0);


unsigned char CNT = 0;
int bfs(int sx, int sy, int ex, int ey)
{
	priority_queue<E> q;
//	printf("przed reset\n");
	//RESET(vis, -1);
	++CNT;
//	printf("po reset\n");
	
	int d = -1;	
	
	ADD(sx, sy, MAX, MAX, 0, MAX, MAX, 0);

	while(!q.empty()) {
		E e = q.top(); q.pop();
		d = dst[e.x][e.y][e.ax][e.ay][e.az][e.bx][e.by][e.bz];
//		printf("q,  x = %d y = %d ax = %d ay = %d az = %d bx = %d by = %d bz = %d   ex = %d ey = %d d = %d\n",
//	  e.x, e.y, e.ax, e.ay, e.az, e.bx, e.by, e.bz, ex, ey, d);
		if(e.x == ex && e.y == ey) return d;
		//move 
		REP(i, 4) {
			int nx = e.x + dx[i], ny = e.y + dy[i];
			//if(!OK(nx,ny)) continue;
			if(pole[nx][ny] == 0) {  ADD( nx, ny, e.ax, e.ay, e.az, e.bx, e.by, e.bz); continue; }

			if(e.ax == MAX || e.bx == MAX) continue;
			if( (e.ax == nx && e.ay == ny && e.az == (i+2)%4) ) { 
				ADD(e.bx + dx[e.bz], e.by + dy[e.bz],  e.ax, e.ay, e.az, e.bx, e.by, e.bz); }
			else if(e.bx == nx && e.by == ny && e.bz == (i+2)%4) {
				ADD(e.ax + dx[e.az], e.ay + dy[e.az], e.ax, e.ay, e.az, e.bx, e.by, e.bz); }
		}
		//shot
		
		d--;
		REP(dir, 4) {
			int nx = e.x , ny = e.y ;
			while(pole[nx][ny] == 0) nx += dx[dir], ny += dy[dir];

			//if(!OK(nx, ny)) { nx += dx[(dir+2)%4]; ny += dy[(dir+2)%4]; }
			
			ADD(e.x, e.y, nx, ny, (dir+2)%4, e.bx, e.by, e.bz);
			ADD(e.x, e.y, e.ax, e.ay, e.az, nx, ny, (dir+2)%4);
		}
	}

	return -1;
}
void solve(void)
{
	scanf("%d %d\n", &N, &M);
	char buff[1000];
	RESET(pole, 0);
	int sx, sy, ex, ey;

	REP(i, MAX) REP(j,MAX) pole[i][j] = 1;
	FOR(i,1,N) {
		gets(buff);
		FOR(j,1,M) switch(buff[j-1]) {
			case 'O': sx = i; sy = j;pole[i][j] = 0; break;
			case 'X': ex = i; ey = j;pole[i][j] = 0; break;
			case '#': pole[i][j] = 1; break;
			case '.': pole[i][j] = 0; break;
		}
	}
//	printf("\n");
//	REP(i, N) REP(j, M) printf( (j == M-1) ? "%d\n" : "%d", pole[i][j]);
	int dst = bfs(sx, sy, ex, ey);
	if(dst == -1) printf("THE CAKE IS A LIE\n");
	else printf("%d\n", dst);
}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
