#include <stdio.h>

int T,NA,NB;

int A2B[128][2];
int B2A[128][2];

int fromA, fromB;
int readyA, readyB;

void solve()
{
  fromA=0;
  fromB=0;
  readyA=0;
  readyB=0;
  for (int t=0; t<24*60; t++) {
    for (int i=0;i<NA;i++) {
      if (t==A2B[i][1]+T) readyB++;
    }
    for (int i=0;i<NB;i++) {
      if (t==B2A[i][1]+T) readyA++;
    }
    for (int i=0;i<NA;i++) {
      if (t==A2B[i][0]) {
        if (readyA==0) fromA++,readyA++;
        readyA--;
      }
    }
    for (int i=0;i<NB;i++) {
      if (t==B2A[i][0]) {
        if (readyB==0) fromB++,readyB++;
        readyB--;
      }
    }
  }
  printf("%d %d\n",fromA,fromB);
}

int main()
{
  int N;
  
  scanf("%d\n",&N);
  for (int i=0;i<N;i++) {
    scanf("%d\n",&T);
    scanf("%d%d\n",&NA,&NB);
    for (int j=0;j<NA;j++) {
      int a,b,c,d;
      scanf("%d:%d %d:%d\n",&a,&b,&c,&d);
      A2B[j][0]=a*60+b;
      A2B[j][1]=c*60+d;
    }
    for (int j=0;j<NB;j++) {
      int a,b,c,d;
      scanf("%d:%d %d:%d\n",&a,&b,&c,&d);
      B2A[j][0]=a*60+b;
      B2A[j][1]=c*60+d;
    }
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}

