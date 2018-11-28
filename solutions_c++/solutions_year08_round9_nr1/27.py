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
#define FOR(i,a,b) for(int i=(a);i<int(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=int(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) FORSZ(i,0,v) 
#define VAR(a,b) __typeof(b) a=b 
#define FORIT(it,v) for(VAR(it,(v).begin());it!=(v).end();++(it)) 
#define DIST(a,b) ABS((a)-(b)) 
#define BETWEEN(i,a,b) ((a)<=(i)&&(i)<(b)) 
#define SQR(a) ((a)*(a)) 
#define ALL(v) (v).begin(),(v).end() 
#define SORT(v) sort(ALL(v)) 
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end()) 
typedef long long ll; 
typedef vector<string> VS; 
typedef vector<VS> VVS; 
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef vector<double> VD; 
typedef vector<VD> VVD; 
typedef vector<ll> VLL; 
typedef vector<VLL> VVLL; 
typedef pair<int,int> PII; 
typedef vector<PII> VPII;

int n;
int needa[5000],needb[5000],needc[5000];

void run(int casenr) {
	scanf("%d",&n);
	REP(i,n) scanf("%d%d%d",&needa[i],&needb[i],&needc[i]);
	int ret=0;
	FORE(a,0,10000) {
		int left=10000-a;
		vector<int> cnt(left+2,0);
		REP(i,n) {
			if(needa[i]>a) continue;
			if(needb[i]+needc[i]>left) continue;
			cnt[needb[i]]++;
			cnt[left-needc[i]+1]--;
		}
		REP(i,left) cnt[i+1]+=cnt[i];
		REPE(i,left) ret>?=cnt[i];
	}
	printf("Case #%d: %d\n",casenr,ret);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}
