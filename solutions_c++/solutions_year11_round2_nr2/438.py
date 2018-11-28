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

#define EPS 1e-9

using namespace std;

int T,C;
long long D;
vector<long long> P;

bool check(long double t) {
  long double last = P[0]-t+D;
  for(int i=1;i<SIZE(P);++i) {
    if (last-EPS > P[i]+t) return false;
    last = max(last, P[i]-t) + D;
  }
  return true;
}

int main() {
  scanf("%d",&T);
  REP(t,T) {
    scanf("%d",&C);
    scanf("%lld",&D);

    P.resize(0);

    REP(i,C) {
      long long p; 
      int v;
      scanf("%lld",&p); scanf("%d",&v);
      REP(j,v) P.push_back(p);
    }

    long double lo=0;
    long double hi=1e19;

    REP(it,1000) {
      long double mid = (lo+hi)/2.0;
      if (check(mid)) hi=mid;
      else lo=mid;
    }

    printf("Case #%d: %Lf\n",t+1,hi);
  }
  return 0;
}
