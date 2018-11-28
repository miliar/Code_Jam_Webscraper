#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <cmath>

//#include "cout.h"
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define rep1(var,n)  for(int var=1;var<=(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

vector<int> X,Y,R;

double dist(int a, int b) {
  return hypot(X[b] - X[a], Y[b] - Y[a]);
}
main(){
  int C; cin >> C; // 10/30
  rep(c,C){
    int N; cin >> N; // 3/40
    X.resize(N);
    Y.resize(N);
    R.resize(N);
    rep(n,N){
      cin >> X[n] >> Y[n] >> R[n]; // 1000,1000,100
    }
    double d, dmax = 0;
    int dmax_a, dmax_b;
    rep(a,N) {
      rep(b,N) {
        if (a<b) {
          d = dist(a,b);
          if (d > dmax) { dmax = d; dmax_a = a; dmax_b = b; }
        }
      }
    }
    double amax=R[dmax_a]*2, bmax=R[dmax_b]*2;
    int amax_n, bmax_n;
    rep(n,N){
      if (n==dmax_a || n==dmax_b) continue;
      double da = dist(dmax_a,n) + R[dmax_a] + R[n],
          db = dist(dmax_b,n) + R[dmax_b] + R[n];
      if (da<=db) { // a陣営
        if (da > amax) { amax=da; amax_n = n; }
      } else {
        if (db > bmax) { bmax=db; bmax_n = n; }
      }
      
    }
    printf("Case #%d: %8.6f\n", 1+c, max(amax, bmax)/2);
  }
}
