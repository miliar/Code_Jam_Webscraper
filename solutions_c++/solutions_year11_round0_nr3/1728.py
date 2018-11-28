#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main(){
  int T; cin >> T;
  for(int cs = 1; cs <= T; ++cs){
    int N; cin >> N;
    int sum = 0, mn = 10000000, rich = 0;
    while(N--){
      int tmp; cin >> tmp;
      sum += tmp;
      mn = min(mn, tmp);
      rich ^= tmp;
    }
    if(rich != 0){
      printf("Case #%d: NO\n", cs);
    }
    else{
      printf("Case #%d: %d\n", cs, sum-mn);
    }
  }
}
