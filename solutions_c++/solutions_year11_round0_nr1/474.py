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
int r[MAXN], p[MAXN], n;
int t[2], pos[2];

int zrob(){
  scanf("%d", &n);
  REP(i,n) {
    char c;
    scanf(" %c %d", &c, &p[i]);
    r[i] = (c=='B');
  }
  REP(i,2) {
    t[i]=0;
    pos[i]=1;
  }
  int curtime = 0;
  REP(i,n){
    //wykonujemy polecenie i
    int movetime = max(0,abs(pos[r[i]] - p[i]) - (curtime - t[r[i]]));
    curtime += 1 + movetime;
    t[r[i]] = curtime;
    pos[r[i]] = p[i];
  }
  return curtime;
}

int main() {
	int T; scanf("%d", &T); FOR(i,1,T) printf("Case #%d: %d\n", i, zrob());
	return 0;
}

