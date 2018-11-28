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

struct ST{ int P, V; };
bool operator<(ST a, ST b){
  return a.P<b.P;
}
double ret;
int C, D, n;
vector<ST> st;

bool calc(double t){
  vector<double> test;
  double now = st[st.size()-1].P+t+D;
  for(int i=st.size()-1; i>=0; i--){
    rep(j,st[i].V){
      double newpos;
      if(st[i].P<now-D){
        newpos = min(now-D, st[i].P+t);
      }else{
        newpos = max(now-D, st[i].P-t);
      }
      if(fabs(newpos-now)<(double)D) return false;
      now = newpos;
    }
  }
  return true;
}

void solve(){
  sort(ALLOF(st));
  double l = 0.0, u = 1000000000.0;
  for(int i=0; i<1000000; i++){
    double m = (u+l)/2;
    if(calc(m)) u=m;
    else l=m;
  }
  ret = (u+l)/2.0;
}

int main(){
  int T;
  cin >> T;
  rep(t,T){
    ret = 0.0;
    st.clear();
    cin >> C >> D;
    int p, v;
    n = 0;
    rep(i,C){
      cin >> p >> v;
      n += v;
      st.push_back((ST){p,v});
    }

    solve();
    
    cout << "Case #" << t+1 << ": ";
    printf("%.12lf\n", ret);
  }
  return 0;
}
