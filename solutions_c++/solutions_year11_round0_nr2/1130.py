#include <stdio.h>
#include <string.h>
int g[256][256];
int op[256];
int has[256];
char res[105];
#define clr(x) memset(x,0,sizeof x)

int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<=casn; ++cas) {
    clr(g);
    clr(op);
    clr(has);
    int c,d,n,t;
    
    scanf("%d", &c);
    for(int i=0; i<c; ++i) {
      char buf[5];
      scanf("%s",buf);
      g[buf[0]][buf[1]]=g[buf[1]][buf[0]]=buf[2];
    }
    
    scanf("%d", &d);
    for(int i=0; i<d; ++i) {
      char buf[5];
      scanf("%s", buf);
      op[buf[0]]=buf[1];
      op[buf[1]]=buf[0];
    }
    
    char buf[105];
    scanf("%d%s", &n,buf);
    t=0;
    for(int i=0; i<n; ++i) {
      if(t && g[res[t-1]][buf[i]]) has[res[t-1]]--, has[res[t-1]=g[res[t-1]][buf[i]]]++;
      else if(has[op[buf[i]]]) clr(has),t=0;
      else has[res[t++]=buf[i]]++;
    }
    
    printf("Case #%d: ", cas);
    if(t) {
      printf("[%c", res[0]);
      for(int i=1; i<t; ++i) printf(", %c",res[i]);
      printf("]\n");
    }
    else puts("[]");
  }
  return 0;
}

