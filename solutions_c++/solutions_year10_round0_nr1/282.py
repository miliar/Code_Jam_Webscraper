#include <string.h>
#include <stdio.h>

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    long long n,k,x,bit; 
    scanf("%lld%lld",&n,&k);
    x = 1<<(n-1);
    bit=(1<<n)-1;
    printf("Case #%d: %s\n", ti, (k&bit)==bit ? "ON" : "OFF");
  }

}
