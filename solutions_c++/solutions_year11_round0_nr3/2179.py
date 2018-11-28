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

int T,N,S,sum,v,c;

int main(void) {
  cin >> T;
  REP(t,T) {
    cin >> N;

    S = 0;
    sum = 0;
    v = 1000001;
    REP(n,N) {
      cin >> c;
      v = min(c,v);
      S^= c;
      sum+=c;
    }

    cout << "Case #" << (t+1) << ": ";
    if (S!=0) cout << "NO"; 
    else cout << sum-v;
    cout << endl;
  }
  return 0;
}
