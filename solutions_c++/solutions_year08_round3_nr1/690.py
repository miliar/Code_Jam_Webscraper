#include <stdio.h>
#include <stdlib.h>

int main()
{
  int N,P,K,L,a;
  int b[1024];

  scanf("%d\n",&N);
  for (int i=0;i<N;i++) {
    scanf("%d%d%d\n",&P,&K,&L);
    for (int j=0;j<L;j++) {
      scanf("%d",&a);
      int k;
      for (k=j;k>0;k--) {
        if (a>b[k-1]) b[k]=b[k-1];
        else break;
      }
      b[k]=a;
    }
    scanf("\n");
    int sum=0;
    for (int j=0;j<L;j++) {
      sum += b[j] * ((j/K)+1);
    }
    printf("Case #%d: %d\n",i+1,sum);
  }
  
  return 0;
}
