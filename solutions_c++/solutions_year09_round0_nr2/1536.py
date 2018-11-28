#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 

int nrcases;
int h,w;
int val[100][100];
char res[100][100];

int DX[]={-1,0,0,1};
int DY[]={0,-1,1,0};

int main() {
	scanf("%d",&nrcases);
	FORE(casenr,1,nrcases) {
		scanf("%d%d",&h,&w);
		REP(i,h) REP(j,w) scanf("%d",&val[i][j]);
		
		memset(res,'?',sizeof(res));
		char nextchar='a';
		REP(sx,h) REP(sy,w) {
			if(res[sx][sy]!='?') continue;
			vector<pair<int,int> > q;
			int x=sx,y=sy;
			while(res[x][y]=='?') {
				q.PB(MP(x,y));
				int nx=x,ny=y;
				REP(k,4) {
						int cx=x+DX[k],cy=y+DY[k];
						if(cx<0||cx>=h||cy<0||cy>=w) continue;
						if(val[cx][cy]>=val[nx][ny]) continue;
						nx=cx,ny=cy;
				}
				if(x==nx&&y==ny) break;
				x=nx,y=ny;
			}
			if(res[x][y]=='?') res[x][y]=nextchar++;
			REPSZ(i,q) res[q[i].first][q[i].second]=res[x][y];
		}
		printf("Case #%d:\n",casenr);
		REP(x,h) { REP(y,w) { if(y>0) printf(" "); printf("%c",res[x][y]); } puts(""); }
	}
	return 0;
}
