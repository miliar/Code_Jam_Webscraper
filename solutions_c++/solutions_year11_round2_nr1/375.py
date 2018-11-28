// By mirosuaf and rogrog v.3.1
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=200;
int n;

char row[150];
VPII opp[MAXN];

double wp[MAXN], op[MAXN], oop[MAXN];
int matches[MAXN];

int zrob(){
  scanf("%d", &n);
  REP(i,n) {
    opp[i].clear();
    wp[i]=0;
    op[i]=0;
    oop[i]=0;
    matches[i]=0;
  }
  REP(i,n){
    scanf("%s", row);
    REP(j,n){
        if(row[j]!='.'){
            matches[i]++;
            int wi=0;
            if(row[j]=='1') { wp[i]++; wi=1; }
            opp[i].PB(MP(j, wi));
        }
    }
    wp[i];
  }
  REP(i,n){
    REP(j,SIZE(opp[i])){
        int o = opp[i][j].ST;
        int win = 1-opp[i][j].ND;
        op[i] += (wp[o]-win)/(matches[o]-1);
    }
    op[i]/=matches[i];
  }

  REP(i,n){
    REP(j,SIZE(opp[i])){
        oop[i] += op[opp[i][j].ST];
    }
    oop[i]/=matches[i];
  }
  REP(i,n){
    printf("%.12lf\n", (wp[i]/matches[i]+op[i]*2+oop[i])/4);
  }
}

int main() {
	int T; scanf("%d", &T); FOR(i,1,T) {
	    printf("Case #%d:\n", i);
	    zrob(); }
	return 0;
}

