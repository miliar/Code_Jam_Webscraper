#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>

#define PROBLEM "b"

typedef long long i64;
typedef unsigned long long u64;

#define MAX 100

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    int n,m,i,j,k,l,A;
    scanf("%d%d%d",&n,&m,&A);
    int ok=0;
    int x1,y1,x2,y2,x3,y3;
    x1=0;
    for(x2=0;x2<=n;++x2)
      for(x3=x2;x3<=n;++x3)
        for(y1=0;y1<=m;++y1)
          for(y2=0;y2<=m;++y2) {
            int a=x2-x1;
            int b=A+(y2-y1)*(x3-x1)+y1*(x2-x1);
            if(!a) {
              if(!b) {
                y3=0;
                ok=1;
                goto zzz;
              }
              else continue;
            }
            if(b%a) continue;
            y3=b/a;
            if(y3>=0 && y3<=m) {
              ok=1;
              goto zzz;
            }
          }
zzz:;
    printf("Case #%d: ",tst);
    if(ok) {
      printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
    }
    else {
      printf("IMPOSSIBLE\n");
    }

  }

  return 0;
}
