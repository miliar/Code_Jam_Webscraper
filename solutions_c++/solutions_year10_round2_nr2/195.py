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

void run(int casenr) {
	int nchicks,need,barn,maxtime; scanf("%d%d%d%d",&nchicks,&need,&barn,&maxtime);
	vector<int> start(nchicks),speed(nchicks);
	REP(i,nchicks) scanf("%d",&start[i]);
	REP(i,nchicks) scanf("%d",&speed[i]);
	vector<bool> ok(nchicks);
	REP(i,nchicks) ok[i]=start[i]+maxtime*speed[i]>=barn;
	
	int have=0,stall=0,ret=0;
	for(int at=nchicks-1;have<need&&at>=0;--at) {
		if(!ok[at]) ++stall; else ret+=stall,++have;
	}
	
	if(have>=need) printf("Case #%d: %d\n",casenr,ret);
	else printf("Case #%d: IMPOSSIBLE\n",casenr);
}

int main() {
	int ncases; scanf("%d",&ncases); FORE(i,1,ncases) run(i);
	return 0;
}

