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


int n,want;
VI canchange,typeorval;

VVI mem;
int go(int at,int want) {
	int &ret=mem[at][want];
	if(ret==-1) {
		ret=INT_MAX;
		if(at<(n-1)/2) {
			REP(type,2) {
				if(type!=typeorval[at]&&!canchange[at]) continue;
				REP(a,2) REP(b,2) {
					int c=type==0?(a!=0||b!=0?1:0):(a!=0&&b!=0?1:0);
					if(c!=want) continue;
					int cur1=go(2*at+1,a),cur2=go(2*at+2,b);
					if(cur1==INT_MAX||cur2==INT_MAX) continue;
					ret<?=cur1+cur2+(type!=typeorval[at]?1:0);
				}
			}
		} else {
			if(want==typeorval[at]) ret=0;
		}
	}
	return ret;
}

void run(int casenr) {
	scanf("%d%d",&n,&want);
	canchange=VI(n,0);
	typeorval=VI(n);
	REP(i,n) {
		if(i<(n-1)/2) scanf("%d%d",&typeorval[i],&canchange[i]); else scanf("%d",&typeorval[i]);
	}
	mem=VVI(n,VI(2,-1));
	int ret=go(0,want);
	
	if(ret==INT_MAX) printf("Case #%d: IMPOSSIBLE\n",casenr); else	printf("Case #%d: %d\n",casenr,ret);	
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}
