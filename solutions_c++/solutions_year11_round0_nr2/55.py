#include <stdio.h>
#include <string.h>
using namespace std;

char C[128], D[64], I[128];
int Cn, Dn, In;

int cnt[256];

int main() {
  int i, j, k;
  int tests; scanf("%d",&tests);
  for (int t=1;t<=tests;++t) {
    scanf("%d",&Cn); for (i=0;i<Cn;++i) scanf("%s",C+3*i);
    scanf("%d",&Dn); for (i=0;i<Dn;++i) scanf("%s",D+2*i);
    scanf("%d %s",&In,I);
    i = j = 0; memset(cnt,0,sizeof(cnt));
    ++cnt[I[0]];
    for (i=j=1;j<In;++j) {
      I[i]=I[j];
      for (k=0;k<Cn;++k) {
        if ((I[i-1]==C[3*k]&&I[i]==C[3*k+1])||(I[i]==C[3*k]&&I[i-1]==C[3*k+1])){
//printf("%c%c->%c\n",I[i-1],I[i],C[3*k+2]);
          --cnt[I[i-1]];
          I[i-1]=C[3*k+2];
          goto next;
        }
      }
      for (k=0;k<Dn;++k) {
        if ((I[i]==D[2*k]&&cnt[D[2*k+1]])||(I[i]==D[2*k+1]&&cnt[D[2*k]])){
//printf("%c%c->*\n",I[i-1],I[i]);
          i=0;
          memset(cnt,0,sizeof(cnt));
          goto next;
        }
      }
//printf("%c\n",I[i]);
      ++cnt[I[i++]];
next:;
    }
    printf("Case #%d: [",t);
    for (k=0;k<i;++k) {
      if (k) printf(", ");
      printf("%c",I[k]);
    }
    printf("]\n");
  }
}

