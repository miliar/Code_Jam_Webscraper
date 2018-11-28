#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define REP(var,ar)  for(int var=0,lim=(ar).size();var<lim;var++)
#define FOR(var,from,to) for(int var=(from),till=(to);var<=till;var++)
#define all(c)  (c).begin(),(c).end()
#define rall(c)  (c).rbegin(),(c).rend()

#define found(s,e)  ((s).find(e)!=(s).end())


//#include "cout.h"

int main(){
  int C; cin >> C; // 100
  rep(c,C){
    cout << "Case #" << (c+1) << ": ";
    
    int N,K,B,T; cin >> N >> K >> B >> T;
    // N:1-10/50 K:0-3/N B:1-1e9 T:1-1000
    vector<int> x(N), v(N);
    rep(i,N) cin >> x[i];
    rep(i,N) cin >> v[i];

    vector<double> ar(N); int cn=0;
    rep(i,N){
      ar[i] = ((double)(B - x[i]))/v[i];
      if (ar[i]<=T) cn++;
    }
    if (cn < K) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    vector<int> swa(N,987654321);
    rep(i,N) {
      if (ar[i]>T) continue;
      int sw=0;
      rep(j,N){
        if (i==j) continue;
        if(ar[j]<=T) continue;
        double mx = (double)(x[j]-x[i])/(v[i]-v[j]);
        if (0 <= mx && mx <= T) sw++;
      }
      swa[i] = sw;
    }
    sort(all(swa));
    int S=0; rep(i,K) S+=swa[i];
    cout << S << endl;
  }
  return 0;
}
