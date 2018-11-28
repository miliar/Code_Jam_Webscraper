#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define PROBLEM "c"

typedef long long i64;
typedef unsigned long long u64;

#define MAX 10010

int perm[MAX];

void build_perm(int n) {
  memset(perm,0,sizeof(perm));
  perm[0]=1;
  for(int k=2,i=0;k<=n;++k) {
    for(int j=0;j<k;) {
      i=(i+1)%n;
      if(!perm[i]) ++j;
    }
    perm[i]=k;
  }
}

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=100;++tst) {
    int n,m,k,l,i,j;
    scanf("%d",&n);
    build_perm(n);
    printf("Case #%d: ",tst);
    scanf("%d",&k);
    for(i=0;i<k;++i) {
      scanf("%d",&j);
      printf("%d ",perm[j-1]);
    }
    printf("\n");
  }

  return 0;
}
