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

int len,nrknown,nrcases;
char known[5000][16];
char pattern[15*28+1];
int patternmask[15];

int main() {
	scanf("%d%d%d",&len,&nrknown,&nrcases);
	REP(i,nrknown) scanf("%s",known[i]);
	FORE(i,1,nrcases) {
		scanf("%s",pattern);
		int at=0;
//		printf("%s\n",pattern);
		REP(j,len) {
			patternmask[j]=0;
			if(pattern[at]!='(') {
				patternmask[j]|=1<<(pattern[at++]-'a');
			} else {
				++at;
				while(pattern[at]!=')') {
					patternmask[j]|=1<<(pattern[at++]-'a');
				}
				++at;
			}
		}
		assert(pattern[at]=='\0');
		int cnt=0;
		REP(j,nrknown) {
			bool ok=true;
			REP(k,len) if(!(patternmask[k]&(1<<(known[j][k]-'a')))) { ok=false; break; }
//			printf("%s %s -> %d\n",known[j],pattern,ok);
			if(ok) ++cnt;
		}
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}
