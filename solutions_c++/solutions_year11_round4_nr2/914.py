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

#define EPS 1.0e-10
#define ZEROP(x) (abs(x)<EPS)
#define EQ(x,y) ZEROP((x)-(y))
#define LT(x,y) ((x)+EPS<(y))
#define LE(x,y) ((x)-(y)<+EPS)

int R, C, D;
vector<string> grid;
int ret;

bool check(){
  //RxCのグリッドでretxretの四角形を取り出して、その重心が真ん中だったらtrue
  //すべてダメだったらfalse
  for(int i=0; i<R-ret+1; i++){
    for(int j=0; j<C-ret+1; j++){
      double sumX = 0, sumY = 0, psum = 0;
      for(int y=0; y<ret; y++){
        for(int x=0; x<ret; x++){
          if(x==0 && y==0) continue;
          if(x==0 && y==ret-1) continue;
          if(x==ret-1 && y==0) continue;
          if(x==ret-1 && y==ret-1) continue;
          
          psum += (grid[i+y][j+x]-'0') + D;
          if(ret%2!=0){
            sumX += (x) * ((grid[i+y][j+x]-'0') + D);
            sumY += (y) * ((grid[i+y][j+x]-'0') + D);
          }else{
            sumX += (x+0.5) * ((grid[i+y][j+x]-'0') + D);
            sumY += (y+0.5) * ((grid[i+y][j+x]-'0') + D);
          }
        }
      }
      if(ret%2!=0){
        if(EQ(sumX/psum,(ret-1)/2.0) && EQ(sumY/psum,(ret-1)/2.0)) return true;
      }else{
        if(EQ(sumX/psum,ret/2.0) && EQ(sumY/psum,ret/2.0)) return true;
      }
    }
  }
  return false;
}

void solve(){
  ret = min(R, C);
  for(; ret>2; ret--){
    if(check()){
      return;
    }
  }
}

int main(){
  int T = 0;
  cin >> T;
  rep(step,T){
    cin >> R >> C >> D;
    grid.clear();
    rep(i,R){
      string tmp;
      cin >> tmp;
      grid.push_back(tmp);
    }

    solve();
    
    if(ret>2){
      printf("Case #%d: %d\n", step+1, ret);
    }else{
      printf("Case #%d: IMPOSSIBLE\n", step+1);
    }
  }
  return 0;
}
