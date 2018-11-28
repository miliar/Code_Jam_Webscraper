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

int R, C;
vector<string> in, out;

void solve(){
  out = in;
  rep(i,R) rep(j,C){
    if(out[i][j]=='#'){
      if(i+1<R && j+1<C){
        if(out[i+1][j]=='#' && out[i][j+1]=='#' && out[i+1][j+1]=='#'){
          out[i][j] = '/';
          out[i+1][j] = '\\';
          out[i][j+1] = '\\';
          out[i+1][j+1] = '/';
        }else{
          out.clear();
          return;
        }
      }else{
        out.clear();
        return;
      }
    }
  }
}

int main(){
  int T;
  cin >> T;
  rep(t,T){
    cin >> R >> C;
    in.clear();
    rep(i,R){
      string tmp;
      cin >> tmp;
      in.push_back(tmp);
    }
    
    solve();
    
    cout << "Case #" << t+1 << ":" << endl;
    if(out.size()==0) cout << "Impossible" << endl;
    else{
      rep(i,R){
        rep(j,C){
          cout << out[i][j];
        }
        cout << endl;
      }
    }
  }
  return 0;
}
