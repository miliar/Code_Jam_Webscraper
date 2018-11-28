#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
  int t;
  scanf("%d", &t);
  int w=t;
  while(t--){
    int n, k;
    scanf("%d%d", &n, &k);
    int j=0;
    bool error=false;
    while(k%2 && j<n){
      j++;
      k/=2;
    }
    if(j==n){
      printf("Case #%d: ON\n", w-t);
    }else{
      printf("Case #%d: OFF\n", w-t);
    }
  }
  return 0;
}
