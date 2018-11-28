#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define PROBLEM "b"

typedef long long i64;
typedef unsigned long long u64;

#define MAX 1010

int col[MAX];

int primes[MAX][MAX];
int cnt[MAX];

void find_primes(int ind,int z) {
  for(int r=2;r*r<=z;++r) {
    if(!(z%r)) {
      primes[ind][cnt[ind]++]=r;
      while(!(z%r)) z/=r;
    }
  }
  if(z>1) {
    primes[ind][cnt[ind]++]=z;
  }
}

char was[MAX];

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    int A,B,P;
    scanf("%d%d%d",&A,&B,&P);
    memset(cnt,0,sizeof(cnt));
    for(int z=A;z<=B;++z) {
      find_primes(z-A,z);
      col[z-A]=z-A;
    }
    for(;;) {
      int x,y,i,j;
      int end=1;
      for(x=A;x<=B;++x)
        for(y=x+1;y<=B;++y) {
          if(col[x-A]!=col[y-A]) {
            for(i=0;i<cnt[x-A];++i)
              if(primes[x-A][i]>=P)
                for(j=0;j<cnt[y-A];++j)
                  if(primes[x-A][i]==primes[y-A][j]) {
                    int c=col[y-A];
                    for(int z=A;z<=B;++z)
                      if(col[z-A]==c)
                        col[z-A]=col[x-A];
                    end=0;
                    goto zzz;
                  }

          }
          zzz:;
        }
      if(end) break;
    }
    int ans=0;
    memset(was,0,sizeof(was));
    for(int x=A;x<=B;++x)
      if(!was[col[x-A]]) {
        was[col[x-A]]=1;
        ++ans;
      }
    printf("Case #%d: %d\n",tst,ans);
  }

  return 0;
}
