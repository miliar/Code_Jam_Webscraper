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
  int R; cin >> R;

  typedef set<pair<int,int> > spii;
  set<pair<int,int> > st, next;
  
  REP(r, R) {
    int x1, x2, y1, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    if( x1 > x2 ) swap(x1, x2);
    if( y1 > y2 ) swap(y1, y2);
    
    for(int x = x1; x <= x2; x++)
      for(int y = y1; y <= y2; y++)
        st.insert( make_pair(x,y) );
  }

  int res = 0;
  while( st.size() > 0 ) {
//     for( spii::iterator it = st.begin(); it != st.end(); it++) {
//       cout << it->first << ' ' << it->second << endl;
//     }
//     cout << endl;
    
//     res.insert( ALL(st) );    
    next.clear();

    for( spii::iterator it = st.begin(); it != st.end(); it++) {
      if( st.count( make_pair( it->first - 1, it->second ) ) > 0 ||
          st.count( make_pair( it->first, it->second - 1 ) ) > 0 )      
        next.insert( *it );

      if( st.count( make_pair( it->first, it->second + 1) ) == 0 &&
          st.count( make_pair( it->first - 1, it->second + 1) ) > 0 )
        next.insert( make_pair(it->first, it->second + 1) );
    }
    
    next.swap( st );
    res++;    
  }  
  cout << res << endl;
  return;
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {

    printf("Case #%d: ", tno);
    run();
  }
  return 0;
}
