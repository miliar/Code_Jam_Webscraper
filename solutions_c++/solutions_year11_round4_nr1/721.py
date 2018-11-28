#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FORZ(i,b) FOR(i,0,(b))
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int main() {
  int tt;
  cin >> tt;
  FOR(t,1,tt+1) {
    printf("Case #%d: ", t);
    
    int X, S, R, t, N;
    cin >> X >> S >> R >> t >> N;
    vector<pii> walks(N+1);
    FORZ(i, N) {
      int b, e, w;
      cin >> b >> e >> w;
      walks[i] = mp(w, e - b);
      X -= (e - b);
    }
    walks[N] = mp(0, X);
    sort(all(walks));
    double time = 0;
    double dt = t;
    FORZ(i, N+1) {
      double speedRun = R + walks[i].first;
      double timeRun = walks[i].second / speedRun;
      if (dt >= timeRun) {
        time += timeRun;
        dt -= timeRun;
        continue;
      }
      double distRun = dt * speedRun;
      double timeWalk = (walks[i].second - distRun) / (S + walks[i].first);
      time += dt;
      time += timeWalk;
      dt = 0;
    }
    printf("%.9f\n", time);
  }
  return 0;
}
