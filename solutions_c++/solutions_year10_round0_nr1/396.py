#include<iostream>
using namespace std;
int main(){
  int t;
  scanf("%d", &t);
  for(int i = 0; i < t; ++i){
    int n,k;
    scanf("%d%d", &n, &k);
    int cycle = 1<<n;
    if(k-cycle>0)k%=cycle;
    printf("Case #%d: %s\n", i+1, (k==cycle-1)?"ON":"OFF");
  }
  return 0;
}
