#include<cstdio>
#include<iostream>

using namespace std;
#define FOR(a, b, c) for(int a=b; a<=c; a++)

int main(void){
  int T;
  int N , K;
  cin >> T;
  FOR(i, 1, T){
    cin >> N >> K;
    int tmp = (1 << N);
    K %= tmp;
    if(tmp - 1 == K){
      printf("Case #%d: ON\n", i);
    } else{
      printf("Case #%d: OFF\n", i);
    }
  }
  return 0;  
}
