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
typedef unsigned long long ll;

#define EPS 1.0e-10
#define ZEROP(x) (abs(x)<EPS)
#define EQ(x,y) ZEROP((x)-(y))
#define LT(x,y) ((x)+EPS<(y))

struct ST{
  int idx;
  ll dist;
  double tm;
};
bool operator<(ST a, ST b){
  double aa = a.dist*2LL-a.tm, bb = b.dist*2LL-b.tm;
  if(EQ(aa,bb)) return a.idx>b.idx;
  return LT(bb,aa);
}


ll L, Lt, N, C;
vector<ll> in;
vector<ST> Ca;
vector<ST> Ca2;
ll ret;

void solve(){
  if(L==0){
    ll sum = 0;
    rep(i,Ca.size()){
      sum += Ca[i].dist*2;
    }
    ret = sum;
    return;
  }
  ll sum = 0, sa = 0;
  int canUseIdx = -1;
  rep(i,Ca.size()){
    if(sum<=Lt && Lt<sum+Ca[i].dist*2LL){
      canUseIdx = i;
      sa = Lt-sum;
      break;
    }
    sum += Ca[i].dist*2LL;
  }

  REP(i,canUseIdx,Ca.size()){
    if(i==canUseIdx){
      ST tmp;
      tmp.idx = Ca[i].idx;
      tmp.dist = Ca[i].dist;
      tmp.tm = sa+(tmp.dist-sa/2.0);
      Ca2.push_back(tmp);
    }else{
      ST tmp;
      tmp.idx = Ca[i].idx;
      tmp.dist = Ca[i].dist;
      tmp.tm = Ca[i].dist;
      Ca2.push_back(tmp);
    }
  }

  sort(ALLOF(Ca2));


  
  rep(i,Ca2.size()){
    if(i<L){
      sum += (ll)Ca2[i].tm;
    }else{
      sum += Ca2[i].dist*2LL;
    }
  }
  ret = sum;
}


int main(){
  int T;
  cin >> T;
  rep(t,T){
    cin >> L >> Lt >> N >> C;
    in.clear();
    Ca.clear();
    Ca2.clear();
    rep(i,C){
      ll tmp;
      cin >> tmp;
      in.push_back(tmp);
    }
    rep(i,N){
      ll tmp = in[i%C];
      Ca.push_back((ST){i,tmp,tmp*2LL});
    }
    ret = 1000000000000000000LL;
    solve();

    cout << "Case #" << t+1 << ": " << ret << endl;
  }
  return 0;
}
