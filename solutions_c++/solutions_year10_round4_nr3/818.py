#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define CLEAR(x) memset(x,0,sizeof(x))

inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

int peta[128][128];
int temp[128][128];

bool ok() {
	FOR(i,1,100) FOR(j,1,100) if(peta[i][j]) return false;
	return true;
}

void simulate() {
	FOR(i,1,100) FOR(j,1,100) {
		temp[i][j] = peta[i][j];
		if(peta[i][j]==1) {
			if(peta[i-1][j]+peta[i][j-1]==0)
				temp[i][j] = 0;
		}
		else {
			if(peta[i-1][j]+peta[i][j-1]==2)
				temp[i][j] = 1;
		}
	}
	FOR(i,1,100) FOR(j,1,100)
		peta[i][j]=temp[i][j];
}

int main() {
	OPEN("c");
	REP(ncase,getint()) {
		CLEAR(peta);
		REP(r,getint()) {
			int x1 = getint();
			int y1 = getint();
			int x2 = getint();
			int y2 = getint();
			FOR(y,y1,y2) FOR(x,x1,x2) peta[y][x] = 1;
		}
		int ans = 0;
		while(!ok()) {
			simulate();
			ans++;
		}
		printf("Case #%d: %d\n",ncase+1,ans);
	}
	return 0;
}
