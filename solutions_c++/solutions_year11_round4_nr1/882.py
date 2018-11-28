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
#define popcount  __builtin_popcount
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(__typeof__((c).begin()) i=(c).begin(),till=(c).end(); i!=till; i++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#include "cout.h"

int main(){
  int T;cin>>T;//40
  rep(t,T){
    int X,S,R,J,N;cin>>X>>S>>R>>J>>N; //1e6 100 100 1e6 1000
    double L0 = (double)X, LP = 0.0;
    double D=(double)(R-S);
    vector<int> L(N);
    priority_queue<vector<double> > pq;
    rep(n,N){int B,E,W;cin>>B>>E>>W;
      double L = (double)(E-B); L0 -= L;
      vector<double> z(3);
      z[0] = D / (double)(W+S); // k
      z[1] = L / (double)(W+R); // m
      z[2] = L;
      LP += L / (double)(W+S);
      pq.push(z);
    }
    vector<double> z0(3);
    z0[0] = D/(double)S;
    z0[1] = L0/(double)R;
    z0[2] = L0;
    LP += L0 / (double)S;
    pq.push(z0);

    double rest = (double)J;
    while(!pq.empty()){
      vector<double> to = pq.top(); pq.pop();
      // cout << "   " << to << endl;
      double k = to[0], m = to[1], l = to[2];
      double us = rest; if (us > m) us = m;
      LP -= us * k;
      // printf("   LP -= %g * %g = %g\n", us, k, LP);
      rest -= us; if (rest <= 0) rest = 0;
    }
    printf("Case #%d: %9.7f\n", 1+t, LP);
  }
  return 0;
}
