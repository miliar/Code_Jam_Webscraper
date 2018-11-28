#include <iostream>
using namespace std;
#define rep(var,n)  for(int var=0;var<(n);var++)

main(){
  int T;cin >> T; //1-10000
  rep(t,T){
    int N,K; cin >> N >> K; // 1-10, 0-1e8
    int b,m;
    for(m=1,b=0;b<=30;b++,m<<=1){
      if ((K & m)==0) break;
    }
    int rec = (1 << (b+1))-1;
    int on = (K & rec) & (1 << (N-1));
    printf("Case #%d: %s\n", 1+t, on?"ON":"OFF");
  }
}
