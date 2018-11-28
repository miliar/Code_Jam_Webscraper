#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>

#define PROBLEM "d"

typedef long long i64;
typedef unsigned long long u64;

#define MAX 20
#define LEN 1010

char str[LEN];
char ztr[LEN];
int l;
int ans;

inline void relax() {
  int res=0;
  for(int i=1;i<=l;++i) {
    if(ztr[i]!=ztr[i-1])
      ++res;
  }
  if(res<ans) ans=res;
}

char used[MAX];
int p[MAX];
int n;

void gen(int k) {
  if(k>=n) {
    for(int i=0;i<l/n;++i) {
      for(int j=0;j<n;++j) {
        ztr[i*n+j]=str[i*n+p[j]];
      }
    }
    ztr[l]=0;
    relax();
    return;
  }
  for(int i=0;i<n;++i) {
    if(!used[i]) {
      p[k]=i;
      used[i]=1;
      gen(k+1);
      used[i]=0;
    }
  }
}

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    scanf("%d%s",&n,&str);
    l=strlen(str);
    memset(used,0,sizeof(used));
    ans=1000000000;
    gen(0);
    printf("Case #%d: %d\n",tst,ans);
  }

  return 0;
}
