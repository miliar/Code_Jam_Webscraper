#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}

void run() {
  int N; cin >> N;

  map<int, int> mp;
  REP(i, N) {
    int p, v;
    cin >> p >> v;
    mp[p] = v;
  }

  int ans = 0;
  for(;;) {
    bool change = false;
    for( map<int,int>::iterator it = mp.begin();
         it != mp.end(); it++) {
      if( it->second >= 2 ) {

        ++mp[it->first - 1];
        it->second -= 2;
        ++mp[it->first + 1];
        
        ans++;
        change = true;
        break;
      }
    }
    if( ! change ) break;
  }
  cout << ans << endl;
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {

    printf("Case #%d: ", tno);
    run();
  }
  return 0;
}
