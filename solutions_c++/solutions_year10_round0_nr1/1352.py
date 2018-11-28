#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  int nt;
  scanf("%d",&nt);
  for(int t = 1 ; t<= nt; t++){
    int n,k;
    scanf("%d %d",&n,&k);
    printf("Case #%d: ",t);
    if((k+1) % (1 << n) == 0) printf("ON\n");
    else printf("OFF\n");
  }
  return 0;
}
