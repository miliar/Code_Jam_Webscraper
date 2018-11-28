#include <stdlib.h>
#include <stdio.h>


int main()
{ 
  uint testNum = 0;
  scanf("%d", &testNum);
  for(uint t=1; t<=testNum; ++t) {
    uint n=0;
    uint k=0;
    scanf("%d %d", &n, &k);
    uint on_n = 1<<n;
    uint on_st = on_n-1;
    printf("Case #%d: ", t); 
    if((k%on_n)==on_st)
      printf("ON");
    else 
      printf("OFF");
    printf("\n");  
  }

  return 0;
}
