#include<stdio.h>

int main(){
  int t,k,n;
  scanf("%d",&t);
  for(int i=1; i<=t; i++){
    scanf("%d %d", &n, &k);
    int r=(1<<n)-1;
    if(r<=k && 0==(k-r)%(1+r)) printf("Case #%d: ON\n", i); else printf("Case #%d: OFF\n", i);
  }
  return 0;
}
