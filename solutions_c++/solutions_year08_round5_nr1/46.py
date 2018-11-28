#include <cstdio>
#include <algorithm>
#include <vector>
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

const int DX[]={0,+1,0,-1},DY[]={+1,0,-1,0};

void run(int casenr) {
	int parts; scanf("%d",&parts);
	vector<int> xpass[7001]; //ypass[7001];
	int x=3000,y=3000,d=0;
	REP(i,parts) {
		char s[33]; int times; scanf("%s%d",&s,&times); int n=strlen(s);
		REP(j,times) REP(k,n) {
			int nx,ny;
			switch(s[k]) {
				case 'F':
					nx=x+DX[d],ny=y+DY[d];
					if(nx!=x) xpass[min(x,nx)].PB(y);
//					if(ny!=y) ypass[min(y,ny)].PB(x);
					x=nx,y=ny;
//					printf("%d %d\n",nx-3000,ny-3000);
					break;
				case 'R':
					if(++d==4) d=0;
					break;
				case 'L':
					if(--d==-1) d=3;
					break;
				default:
					assert(false);
			}
		}
	}
	REPE(x,7000) sort(xpass[x].begin(),xpass[x].end());
//	REPE(y,7000) sort(ypass[y].begin(),ypass[y].end());
//	REPE(x,7000) REPSZ(j,xpass[x]) printf("pass x=%d at y=%d\n",x-3000,xpass[x][j]-3000);
//	REPE(y,7000) REPSZ(j,ypass[y]) printf("pass y=%d at x=%d\n",y-3000,ypass[y][j]-3000);

	pair<int,int> left[7001],right[7001];
	left[0]=MP(INT_MAX,INT_MIN);
	REP(x,7000) {
		left[x+1]=left[x];
		if(SZ(xpass[x])>0) left[x+1].first<?=xpass[x][0],left[x+1].second>?=xpass[x].back();
	}
	right[7000]=MP(INT_MAX,INT_MIN);
	for(int x=7000;x>0;--x) {
		right[x-1]=right[x];
		if(SZ(xpass[x])>0) right[x-1].first<?=xpass[x][0],right[x-1].second>?=xpass[x].back();
	}
	
	int ret=0;
	REPE(x,7000) if(SZ(xpass[x])>0) {
		int a=max(left[x].first,right[x].first),b=xpass[x][0];
		if(a<b) ret+=b-a;
		int c=xpass[x].back(),d=min(left[x].second,right[x].second);
		if(c<d) ret+=d-c;
		for(int i=1;i+1<SZ(xpass[x]);i+=2) ret+=xpass[x][i+1]-xpass[x][i];
	}
	printf("Case #%d: %d\n",casenr,ret);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}
