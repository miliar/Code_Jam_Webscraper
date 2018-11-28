#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(x,v) FOR(x,(v).begin(),(v).end())
#define sz size()
#define pb push_back
#define DBG(x) cout<< #x << " --> "<< x << "\t"
#define DBE(x) cout<< #x << " --> "<< x << "\n"
#define GI ({int t; scanf(" %d", &t); t;})
typedef pair<int,int> PII;
typedef long long LL;

using namespace std;

int main() {
  int T = GI;
  REP(kase, T) {
    int R = GI, K = GI, N = GI;
    vector<LL> V;
    REP(i, N)
      V.pb(GI);
    vector<int> next;
    vector<LL> value;
    REP(i, N) {
      LL sum = V[i], j;      
      for(j = (i+1)%N; j != i and sum + V[j] <= K; j = (j+1)%N)
	sum += V[j];
      value.pb(sum);
      next.pb(j);
    }
    //REP(i, next.sz) DBG(value[i]); cout << endl;
    set<int> seen;
    vector<int> seq;
    int cur = 0;
    while(seen.count(cur) == 0) {
      seen.insert(cur);
      seq.pb(cur);
      cur = next[cur];
    }
    //REP(i,seq.sz) DBG(seq[i]); cout << endl;
    LL ans = 0;
    int x = 0;
    for(int i=0; R>0 and seq[i] != cur; i++, R--)
      ans += value[seq[i]], x = i+1;

    int cyc_len = seq.sz - x;
    //DBE(cyc_len);
    LL cyc_val = 0;
    FOR(i, x, seq.sz) cyc_val += value[seq[i]];    
    //DBE(cyc_val);
    if (cyc_len > 0) ans += (R/cyc_len)*cyc_val;
    
    REP(i, R%cyc_len)
      ans += value[seq[i+x]];
    
    cout << "Case #" << kase+1 << ": " << ans << endl;
  }
  return 0;
}
