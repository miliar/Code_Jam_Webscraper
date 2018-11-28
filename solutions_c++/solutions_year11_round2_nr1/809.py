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

vector<double> WP, OWP, OOWP;
vector<string> in;

void solve(){
  int n = in.size();
  rep(i,n){
    int win=0, all=0;
    rep(j,n){
      if(in[i][j]!='.'){
        all++;
        if(in[i][j]=='1') win++;
      }
    }
    WP.push_back(win/(double)all);
  }

  rep(i,n){
    int all = 0;
    double owp = 0.0;
    rep(j,n){
      if(in[i][j]!='.'){
        int win=0, wpall=0;
        rep(k,n){
          if(i!=k && in[j][k]!='.'){
            wpall++;
            if(in[j][k]=='1') win++;
          }
        }
        all++;
        owp += win/(double)wpall;
      }
    }
    OWP.push_back(owp/(double)all);
  }
  

  
  rep(i,n){
    int all = 0;
    double oowp = 0.0;
    rep(j,n){
      if(in[i][j]!='.'){
        all++;
        oowp += OWP[j];
      }
    }
    OOWP.push_back(oowp/(double)all);
  }
}


int main(){
  int T, n;
  cin >> T;
  rep(t,T){
    WP.clear();
    OWP.clear();
    OOWP.clear();
    in.clear();
    cin >> n;
    rep(i,n){
      string tmp;
      cin >> tmp;
      in.push_back(tmp);
    }

    solve();

    cout << "Case #" << t+1 << ":" << endl;
    rep(i,WP.size()){
      double ret = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
      //cout << ret << endl;
      printf("%.12lf\n", ret);
    }
  }
  return 0;
}
