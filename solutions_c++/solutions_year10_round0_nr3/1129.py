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

void run(int casenr) {
	int nrides,nspots,ngroups; scanf("%d%d%d",&nrides,&nspots,&ngroups);
	vector<int> group(ngroups); REP(i,ngroups) scanf("%d",&group[i]);
	vector<int> now(ngroups),next(ngroups);
	REP(i,ngroups) {
		ll sum=group[i]; int at=i; if(++at==ngroups) at=0;
		while(at!=i&&sum+group[at]<=nspots) { sum+=group[at]; if(++at==ngroups) at=0; }
		now[i]=sum; next[i]=at;
	}
	vector<bool> been(ngroups,false); vector<pair<ll,int> > had(ngroups);
	int at=0; ll ret=0; int left=nrides;
	while(left>0) {
		if(been[at]) {
			int cyclelen=had[at].second-left;
			if(left>=cyclelen) {
				int ncycles=left/cyclelen;
				ll got=ret-had[at].first;
				ret+=ncycles*got; left-=ncycles*cyclelen;
				continue;
			}
		} else {
			been[at]=true; had[at]=MP(ret,left);
		}
		ret+=now[at]; at=next[at]; --left; 
	}
	printf("Case #%d: %lld\n",casenr,ret);
}

int main() {
	int ncases; scanf("%d",&ncases); FORE(i,1,ncases) run(i);
	return 0;
}
