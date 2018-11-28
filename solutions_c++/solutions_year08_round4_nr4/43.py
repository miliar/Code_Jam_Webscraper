#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;

#define SZ(v) ((int)(v).size())
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define VAR(a,b) __typeof(b) a=b
#define FORIT(i,v) for(VAR(i,(v).begin());i!=(v).end();++i)
#define ALL(v) (v).begin(),v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) (v).erase(UNIQUE(ALL(v)),(v).end())


typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;

int period,n;
char s[50001];

int cost[16][16][16];

int mem[16][16][1<<16];
int go(int pos,int first,int last,int used) {
	if(pos==period) return cost[pos-1][last][first];
	int &ret=mem[first][last][used];
	if(ret==-1) {
		ret=INT_MAX;
		REP(now,period) if((used&(1<<now))==0) {
			ret<?=cost[pos-1][last][now]+go(pos+1,first,now,used|(1<<now));
		}
	}
	return ret;
}

void run(int casenr) {
	scanf("%d%s",&period,s); n=strlen(s);
	memset(cost,0,sizeof(cost));
	FOR(i,1,n) {
		if(i%period==0) {
			int off=0,base=(i-1)/period*period;
			REP(j,period) REP(k,period) if(s[base+j]!=s[base+period+k]) cost[off][j][k]++;
		} else {
			int off=i%period,base=i/period*period;
			REP(j,period) REP(k,period) if(s[base+j]!=s[base+k]) cost[off][j][k]++;
		}
	}
	//REP(i,period) REP(j,period) REP(k,period) printf("%d %d %d = %d\n",i,j,k,cost[i][j][k]);
	int ret=INT_MAX;
	memset(mem,-1,sizeof(mem));
	REP(i,period) {
		ret<?=1+go(1,i,i,1<<i);
	}
	printf("Case #%d: %d\n",casenr,ret);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}
