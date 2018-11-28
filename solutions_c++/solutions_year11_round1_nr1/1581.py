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

string solve(ll N, ll Pd, ll Pg){
  if(Pd==0){
    if(Pg==0) return "Possible";
    return "Broken";
  }
  if(Pg==0) return "Broken";
  
  ll D, winD, G, winG;
  for(ll wind=0; ; wind++){
    winD = wind;
    double dD = winD*100/(double)Pd;
    if(dD>N) break;
    if((winD*100)%Pd==0){
      D = (winD*100)/Pd;
      //cout << winD << " " << D << endl;
      if(0<D && D<=N){
        if(Pd!=100){
          if(Pg==100) return "Broken";
        }
        return "Possible";
      }
    }
  }
  return "Broken";
}

int main(){
  int T;
  int N, Pd, Pg;
  cin >> T;
  rep(t,T){
    cin >> N >> Pd >> Pg;
    cout << "Case #" << t+1 << ": " << solve(N, Pd, Pg) << endl;
  }
  return 0;
}
