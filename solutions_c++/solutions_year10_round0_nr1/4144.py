#include<stdio.h>

int tests;

int main() {
  scanf("%d",&tests);
  for(int tnum=1;tnum<=tests;tnum++) {
    int k, n;
    scanf("%d %d",&n,&k);
    bool ok = 1;    
    for(int i=0;i<n;i++) {
      if(k%2 == 0)
        ok = 0;
      k /= 2;
    }
    if(ok)
      printf("Case #%d: ON\n",tnum);
    else
      printf("Case #%d: OFF\n",tnum);
  }
  return 0;
}
