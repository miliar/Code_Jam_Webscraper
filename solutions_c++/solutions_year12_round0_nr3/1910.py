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

using namespace std;

int T;
long long A,B;
set<pair<long long,long long> > S;

int main(void) {
  cin >> T;
  REP(t,T) {
    S.clear();
    cin >> A >> B;
    for(long long n=A;n<=B;++n) {
      long long desat = 1;
      long long x=n;
      while(x>9) { desat*=10; x/=10; }
      x = n;
      do {
        int d = x%10;
        x = x/10 + d*desat;
        if (d!=0 && A <= x && x <= B) S.insert(make_pair(min(n,x),max(n,x)));
      } while(x!=n);
      S.erase(make_pair(n,n));
    }
    cout << "Case #" << t+1 << ": " << SIZE(S) << endl;
  }
  return 0;
}
