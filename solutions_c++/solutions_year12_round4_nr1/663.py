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

struct ST{
  int d, l;
};

bool ret;
vector<ST> v;

void dfs(int now, int prev, int D){
  if(ret) return;
  int w = v[now].l;
  if(prev!=-1) w = min(w, v[now].d-v[prev].d);
  else w = min(w, v[now].d);
  
  //cout << "now:" << now << endl;
  //cout << "w:" << w << endl;
  if(v[now].d + w >= D){
    ret = true;
    return;
  }
  
  REP(i,now+1,v.size()){
    if(v[i].d <= v[now].d + w){
      dfs(i, now, D);
    }else{
      break;
    }
  }
  
}

bool solve(int D){
  ret = false;
  dfs(0, -1, D);
  return ret;
}


int main(){
  int T;
  cin >> T;

  int N, d, l, Dis;
  rep(t,T){
    cin >> N;
    v.clear();
    rep(i,N){
      cin >> d >> l;
      v.push_back((ST){d,l});
    }
    cin >> Dis;
    printf("Case #%d: %s\n", t+1, solve(Dis)?"YES":"NO");
  }
  
  return 0;
}
