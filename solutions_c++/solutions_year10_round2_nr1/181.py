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

char buff[1000];

void run(int casenr) {
	int nexist,nadd; scanf("%d%d",&nexist,&nadd);
	set<string> have;
	REP(i,nexist) { scanf("%s",buff); have.insert(buff); }
	int ret=0;
	REP(i,nadd) {
		scanf("%s",buff); string s=buff;
		while(SZ(s)>0&&!have.count(s)) {
			++ret;
			have.insert(s);
			int pos=-1; for(int j=SZ(s)-1;j>=0;--j) if(s[j]=='/') { pos=j; break; } assert(pos!=-1);
			s=s.substr(0,pos);
		}
	}
	printf("Case #%d: %d\n",casenr,ret);
}

int main() {
	int ncases; scanf("%d",&ncases); FORE(i,1,ncases) run(i);
	return 0;
}

