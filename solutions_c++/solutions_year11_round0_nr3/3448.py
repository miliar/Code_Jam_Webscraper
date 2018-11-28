#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <climits>
using namespace std;

#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define DEB 0
#define all(x) x.begin(), x.end()

int main(){
  int T;
  scanf("%d",&T);

  rep(x,T){
    int n,c,ok=0;
    long long sum=0;
    int mi = INT_MAX;
    
    scanf("%d",&n);
    rep(i,n){
      scanf("%d",&c);
      sum += (long long)c;
      ok ^= c;
      mi = min(mi, c);
    }
    if( ok!=0 ){
      printf("Case #%d: NO\n",x+1);
    }else{
      printf("Case #%d: %lld\n",x+1,sum-(long long)mi);
    }
  }
  return 0;
}
