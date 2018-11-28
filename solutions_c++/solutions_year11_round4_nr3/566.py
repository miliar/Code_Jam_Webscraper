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
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

#define MAX 1000010LL
using namespace std;

vector<long long> P;
long long N;
int T;

int main(void) {
  for(int i=2;i<MAX;++i) {
    bool ok = true;
    REP(j,SIZE(P)) if (i%P[j]==0) { ok=false; break; }
    if (ok) P.push_back(i);
  }

  cin >> T;
  REP(t,T) {
    cin >> N;
    long long res = 1;
    long long top = sqrt(N);
    REP(i,SIZE(P)) {
      if (P[i] > top) break;
      long long x = N;
      int cnt = 0;
      while(x>=P[i]) {
        x/=P[i];
        ++cnt;
      }
      res+= cnt-1;
    }

    if (N==1) res=0;
    cout << "Case #" << t+1 << ": " << res << endl;
  }
  
  return 0;
}
