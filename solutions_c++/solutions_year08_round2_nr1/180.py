#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define PROBLEM "a"

typedef long long i64;
typedef unsigned long long u64;

#define MAX 100100

int x[MAX],y[MAX];

long long cnt[3][3][3][MAX];

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    int n,A,B,C,D,x0,y0,M;
    scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&x0,&y0,&M);
    int X,Y;
    X=x0; Y=y0;
    int k=0;
    do {
      x[k]=X; y[k++]=Y;
      X=((long long)A*(long long)X+B)%M;
      Y=((long long)C*(long long)Y+D)%M;
    } while(k<n);
    int i,j;
    memset(cnt,0,sizeof(cnt));
    cnt[0][x[0]%3][y[0]%3][0]=1;
    for(k=1;k<n;++k) {
      for(int z=0;z<3;++z)
        for(int zz=0;zz<3;++zz) {
          cnt[0][z][zz][k]=cnt[0][z][zz][k-1];
        }
      ++cnt[0][x[k]%3][y[k]%3][k];
    }
    cnt[1][(x[0]+x[1])%3][(y[0]+y[1])%3][1]=1;
    for(k=2;k<n;++k) {
      for(int z=0;z<3;++z)
        for(int zz=0;zz<3;++zz) {
          cnt[1][z][zz][k]=cnt[1][z][zz][k-1];
        }
      for(int z=0;z<3;++z)
        for(int zz=0;zz<3;++zz) {
          cnt[1][z][zz][k]+=cnt[0][(z-(x[k]%3)+3)%3][(zz-(y[k]%3)+3)%3][k-1];
        }
    }
    cnt[2][(x[0]+x[1]+x[2])%3][(y[0]+y[1]+y[2])%3][2]=1;
    for(k=3;k<n;++k) {
      for(int z=0;z<3;++z)
        for(int zz=0;zz<3;++zz) {
          cnt[2][z][zz][k]=cnt[2][z][zz][k-1];
        }
      for(int z=0;z<3;++z)
        for(int zz=0;zz<3;++zz) {
          cnt[2][z][zz][k]+=cnt[1][(z-(x[k]%3)+3)%3][(zz-(y[k]%3)+3)%3][k-1];
        }
    }
#ifdef __GNUC__
    printf("Case #%d: %lld\n",tst,cnt[2][0][0][n-1]);
#else
    printf("Case #%d: %I64d\n",tst,cnt[2][0][0][n-1]);
#endif
  }

  return 0;
}
