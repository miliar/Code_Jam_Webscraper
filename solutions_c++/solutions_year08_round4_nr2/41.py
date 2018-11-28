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
typedef pair<int,int> PII;
typedef vector<PII> VPII;

VI can;
vector<VPII> val;

void run(int casenr) {
	int n,m,want; bool swapped=false; scanf("%d%d%d",&n,&m,&want); if(n<m) swap(n,m),swapped=true;
	int i=0,j=0;
	while(i<SZ(can)) {
		int now=can[i]-can[j];
		if(now<want) { ++i; continue; }
		if(now>want) { ++j; continue; }
		REPSZ(k,val[i]) if(val[i][k].first<=n&&val[i][k].second<=m) {
			REPSZ(l,val[j]) if(val[j][l].first<=n&&val[j][l].second<=m) {
				if(!swapped) printf("Case #%d: 0 0 %d %d %d %d\n",casenr,val[i][k].first,val[j][l].second,val[j][l].first,val[i][k].second);
				else printf("Case #%d: 0 0 %d %d %d %d\n",casenr,val[j][l].second,val[i][k].first,val[i][k].second,val[j][l].first);
				return;
			}
		}
		++i;
	}
	printf("Case #%d: IMPOSSIBLE\n",casenr);
}

const int MAX=10000;

void precalc() {
	int shift=0;
	while((1<<shift)<MAX+2) ++shift;
	int mask=(1<<shift)-1;
	VVI q(1<<shift);
	VI at(MAX+1,1);
	can.clear(); can.PB(0); val.clear(); val.PB(VPII(1,MP(0,0)));
	FORE(i,1,MAX) q[i].PB(i);
	while(true) {
		bool change=false;
		REPSZ(i,q) {
			REPSZ(j,q[i]) {
				int x=q[i][j],y=at[x]++,z=x*y; change=true;
//				printf("%d*%d = %d\n",x,y,z);
				if(can.back()==z) {
					val.back().PB(MP(x,y));
				} else {
					can.PB(z);
					val.PB(VPII(1,MP(x,y)));
				}
				if(at[x]>x) continue;
				int nz=z+x;
				q[nz&mask].PB(x);
			}
			q[i].clear();
		}
		if(!change) break;
	}
}

int main() {
	precalc();
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}
