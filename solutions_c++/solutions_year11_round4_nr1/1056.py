#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

ll X, S, R, t;
int N;
int cnt[200];
double ret;

void solve(){
  double now = t;
  rep(i,200) if(cnt[i]!=0){
    if(cnt[i]<(R+i)*now){//‘S•”‘–‚ê‚é
      double a = cnt[i]/(double)(R+i);
      ret += a;
      now -= a;
    }else{//“r’†‚Ü‚Å‚µ‚©‘–‚ê‚È‚¢
      double a = (R+i) * now; //m‚¾‚¯‘–‚é
      ret += a/(double)(R+i);
      double b = cnt[i]-a;
      ret += b/(double)(S+i);
      now = 0.0;
    }
  }
}

int main(){
  int T = 0;
  cin >> T;
  rep(step,T){
    cin >> X >> S >> R >> t >> N;
    rep(i,200) cnt[i] = 0;
    cnt[0] = X;
    rep(i,N){
      int B, E, w;
      cin >> B >> E >> w;
      cnt[w] += E-B;
      cnt[0] -= E-B;
    }
    ret = 0.0;
    solve();

    printf("Case #%d: %.9lf\n", step+1, ret);
  }
  return 0;
}
