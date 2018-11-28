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

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<VPII> VVPII;
typedef vector<ll> VLL;
typedef vector<VLL> VVLL;


void run(int casenr) {
	int R,C,exp; scanf("%d%d%d",&R,&C,&exp);
	VVI w(R,VI(C));
	REP(i,R) REP(j,C) { char c; scanf(" %c",&c); w[i][j]=exp+c-'0'; }

	VVI x(R,VI(C)); REP(i,R) REP(j,C) x[i][j]=w[i][j]*i;
	VVI y(R,VI(C)); REP(i,R) REP(j,C) y[i][j]=w[i][j]*j;

	VVLL sumw(R+1,VLL(C+1,0));
	VVLL sumx(R+1,VLL(C+1,0));
	VVLL sumy(R+1,VLL(C+1,0));
	REP(i,R) REP(j,C) {
		sumw[i+1][j+1]=sumw[i][j+1]+sumw[i+1][j]-sumw[i][j]+w[i][j];
		sumx[i+1][j+1]=sumx[i][j+1]+sumx[i+1][j]-sumx[i][j]+x[i][j];
		sumy[i+1][j+1]=sumy[i][j+1]+sumy[i+1][j]-sumy[i][j]+y[i][j];
	}

	for(int ret=min(R,C);ret>=3;--ret) {
		REPE(i,R-ret) REPE(j,C-ret) {
			ll ww=sumw[i+ret][j+ret]-sumw[i][j+ret]-sumw[i+ret][j]+sumw[i][j]-w[i][j]-w[i+ret-1][j]-w[i][j+ret-1]-w[i+ret-1][j+ret-1];
			ll xx=sumx[i+ret][j+ret]-sumx[i][j+ret]-sumx[i+ret][j]+sumx[i][j]-x[i][j]-x[i+ret-1][j]-x[i][j+ret-1]-x[i+ret-1][j+ret-1];
			ll yy=sumy[i+ret][j+ret]-sumy[i][j+ret]-sumy[i+ret][j]+sumy[i][j]-y[i][j]-y[i+ret-1][j]-y[i][j+ret-1]-y[i+ret-1][j+ret-1];
//			printf("%d (%d,%d) -> w=%lld x=%lld y=%lld (%lf %lf)\n",ret,i,j,ww,xx,yy,1.0*xx/ww,1.0*yy/ww);
			if(2*xx==(2*i+ret-1)*ww&&2*yy==(2*j+ret-1)*ww) { printf("Case #%d: %d\n",casenr,ret); return; }

		}
	}
	printf("Case #%d: IMPOSSIBLE\n",casenr);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 
