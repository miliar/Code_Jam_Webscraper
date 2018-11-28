#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char Buf[10240];

int main()
{ 
  uint testNum = 0;
  fgets(Buf, sizeof(Buf), stdin);
  testNum=atoi(Buf);

  for(uint t=1; t<=testNum; ++t) {
    uint r=0;
    uint k=0;
    uint n=0;
    uint money=0;
    uint g[10000];
    uint gs[10000];
    
    fgets(Buf, sizeof(Buf), stdin);
    sscanf(Buf, "%d %d %d", &r, &k, &n);
    fgets(Buf, sizeof(Buf), stdin);
    char* token=strtok(Buf, " \r\n");
    int gc=0;
    while(NULL!=token) {
      g[gc++]=atoi(token);
      token=strtok(NULL, " \r\n");
    }
        
    int gsc=0;    
    int pg=0;
    while(1) {
      int pc=0;
      for(int i=0; i<n; ++i) {
        if(pc+g[pg]>k) {
          break;
        }
        pc+=g[pg];
        ++pg;
        if(pg==n) {
          pg=0;
        }
      }
      gs[gsc++]=pc;
      if(0==pg)
        break;
    }    
    
    int total=0;
    for(int i=0; i<gsc; ++i) {
      //printf("%u ", gs[i]);
      total+=gs[i];
    }
    //printf("\n");
    
    money=total*(r/gsc);
    int rem=r%gsc;                     
    for(int i=0; i<rem; ++i)
      money+=gs[i];      

    printf("Case #%d: %u\n", t, money);   
  }

  return 0;
}
