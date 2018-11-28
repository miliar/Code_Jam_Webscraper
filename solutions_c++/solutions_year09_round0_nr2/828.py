#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)

inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

#define EMPTY -1
#define SINK 0
#define FULL 1

int area[128][128];
int value[128][128];
int answer[128][128];
int H,W;
int basin;

int doit(int i,int j) {
	if( value[i][j] != EMPTY )
		return answer[i][j];

	int x = area[i][j]-1;
	if(i-1>=0 && area[i-1][j] <= x) x = area[i-1][j];
	if(j-1>=0 && area[i][j-1] <= x) x = area[i][j-1];
	if(j+1<W && area[i][j+1] <= x) x = area[i][j+1];
	if(i+1<H && area[i+1][j] <= x) x = area[i+1][j];

	int z = 0;
	if(i-1>=0 && area[i-1][j] == x) z = doit(i-1,j);
	else if(j-1>=0 && area[i][j-1] == x) z = doit(i,j-1);
	else if(j+1<W && area[i][j+1] == x) z = doit(i,j+1);
	else if(i+1<H && area[i+1][j] == x) z = doit(i+1,j);
	else {
		value[i][j] = SINK;
		answer[i][j] = basin++;
		return answer[i][j];
	}

	value[i][j] = FULL;
	answer[i][j] = z;
	return answer[i][j];
}

int main() {
	OPEN("B");
	REP(ncase,getint()) {
		H = getint();
		W = getint();
		REP(i,H) REP(j,W) {
			area[i][j]=getint();
			value[i][j]=EMPTY;
		}
		basin = 0;
		REP(i,H) REP(j,W) doit(i,j);
		printf("Case #%d:\n",ncase+1);
		REP(i,H) {
			REP(j,W) printf("%c ",answer[i][j] + 'a');
			puts("");
		}
	}
	return 0;
}
