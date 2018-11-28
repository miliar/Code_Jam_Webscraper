#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

#define PB push_back
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;


void run(int casenr) {
	int n;
	ll A,B,C,D,x,y,M;
	scanf("%d%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&x,&y,&M);
	vector<vector<ll> > cnt(3,vector<ll>(3));
	REP(i,n) {
		cnt[x%3][y%3]++;
		x=(A*x+B)%M;
		y=(C*y+D)%M;
	}
	ll ret=0;
	REP(x1,3) REP(y1,3) REP(x2,3) REP(y2,3) REP(x3,3) REP(y3,3) {
		if((x1+x2+x3)%3!=0) continue;
		if((y1+y2+y3)%3!=0) continue;
		ll a=cnt[x1][y1];
		ll b=cnt[x2][y2]-(x1==x2&&y1==y2?1:0);
		ll c=cnt[x3][y3]-(x1==x3&&y1==y3?1:0)-(x2==x3&&y2==y3?1:0);
		ret+=a*b*c;
	}
	assert(ret%6==0);
	printf("Case #%d: %lld\n",casenr,ret/6);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
}
