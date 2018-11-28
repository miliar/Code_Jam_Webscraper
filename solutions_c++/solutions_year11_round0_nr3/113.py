#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define all(c)  (c).begin(),(c).end()

int main(){
  int T;cin>>T; //1-100
  rep(t,T){
    printf("Case #%d: ", 1+t);
    int N;cin>>N; //2-15:1000
    vector<int> c(N); // 1-1e6 < 2^20
    int s=0,x=0;
    rep(n,N){
      cin>>c[n]; s+=c[n]; x^=c[n];
    }
    if(x){
      printf("NO\n");
    }
    else{
      int pat=*min_element(all(c));
      printf("%d\n", s-pat);
    }
  }
  return 0;
}
