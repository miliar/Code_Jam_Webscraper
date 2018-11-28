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
#define rall(c)  (c).rbegin(),(c).rend()
#define tr(c,i)  for(__typeof__((c).begin()) i=(c).begin(),till=(c).end(); i!=till; i++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#include "cout.h"

int main(){
  int T;cin>>T;
  rep(t,T){
    int R,C,D; // 500 500 1e6
    cin >>R>>C>>D;
    vector<vector<int> > M(R,vector<int>(C));
    rep(r,R) {
      string s; cin >> s;
      rep(c,C) M[r][c] = s[c]-'0';
    }

    for(int k=min(R,C); k>=3; --k) {
      int _k = k-1;
      for(int y0=0; y0<=R-k; y0++) {
        for(int x0=0; x0<=C-k; x0++) {
          int wx = 0, wy = 0;
          rep(y,k) rep(x,k) {
            if((y==0&&x==0)||(y==0&&x==_k)||(y==_k&&x==0)||(y==_k&&x==_k))continue;
            int v=M[y0+y][x0+x];
            wx += (-_k + x*2)*v;
            wy += (-_k + y*2)*v;
          }
          if (wx==0 && wy==0){
            printf("Case #%d: %d\n", 1+t, k);
            goto next;
          }
        }
      }
    }
   ng:
    printf("Case #%d: IMPOSSIBLE\n", 1+t);
   next:;
  }
  return 0;
}
