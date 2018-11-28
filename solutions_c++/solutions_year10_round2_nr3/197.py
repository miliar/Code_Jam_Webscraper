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

const int MAXN=500;
const int MOD=100003;

int ways[MAXN+1][MAXN+1];
int choose[MAXN+1][MAXN+1];
int ans[MAXN+1];

void run(int casenr) {
	int n; scanf("%d",&n);
	printf("Case #%d: %d\n",casenr,ans[n]);
}



void precalc() {
	memset(choose,0,sizeof(choose));
	REPE(i,MAXN) { choose[i][0]=choose[i][i]=1; FOR(j,1,i) choose[i][j]=(choose[i-1][j-1]+choose[i-1][j])%MOD; }
	memset(ways,0,sizeof(ways));
	FORE(n,2,MAXN) {
		ways[n][n]=(ways[n][n]+1)%MOD;
		FOR(first,2,n) {
			int remfrom=n-first+1;
			int lowsecond=first;
			FORE(second,lowsecond,remfrom) {
				ways[n][first]=(ways[n][first]+(ll)choose[second+first-1-first-1][first-2]*ways[remfrom][second])%MOD;
			}
		}
	}
	FORE(n,2,MAXN) { ans[n]=0; FORE(first,2,n) ans[n]=(ans[n]+ways[n][first])%MOD; }
//	FORE(n,2,MAXN) { FORE(first,2,n) if(ways[n][first]>0) printf("%d %d: %d\n",n,first,ways[n][first]); }
}

int main() {
	precalc();
	int ncases; scanf("%d",&ncases); FORE(i,1,ncases) run(i);
	return 0;
}

