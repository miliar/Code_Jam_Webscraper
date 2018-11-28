#include <iostream>
#include <vector>
using namespace std;
#define rep(var,n)  for(int var=0;var<(n);var++)
#define all(c)  (c).begin(),(c).end()
//#include "../cout.h"

typedef long long ll;

main(){
  int T; cin >> T; //1-50
  rep(t,T){
    int R, k, N; cin >> R >> k >> N; // 1-1e8, 1-1e9, 1-1000
    vector<int> g(N); rep(i,N) cin >> g[i]; // 1-1e7
    int ans = 0;
    vector<int> gg(all(g)); gg.insert(gg.end(),all(g));
    vector<int> acc(N*2+1,0);
    vector<int> hi(N), len(N);
    rep(i,N*2){
      acc[i+1] = acc[i] + gg[i];
    }
    rep(i,N) {
      int lo=acc[i], lim=lo+k, j;
      for(j=1;j<=N;j++){
        if (acc[i+j] > lim) { j--; break; }
      }
      if (j>N) j=N;
      hi[i] = acc[i+j] - lo; len[i] = j;
    }
    /*
    cout << gg << endl;
    cout << acc << endl;
    cout << hi << endl;
    cout << len << endl;
    */
    int at=0; ll earn=0LL;
    rep(r,R){
      earn += hi[at];
      at = (at + len[at]) % N;
    }
    printf("Case #%d: %lld\n", 1+t, earn);
  }
}
