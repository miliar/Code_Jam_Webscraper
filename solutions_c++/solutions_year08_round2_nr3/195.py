#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>

int lf[1000008];
int lb[1000008];
int nb[1000008];

int main() {
  int i, I, c, l, L, N, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &N);
    for (i=0; i<N; i++) {
      lf[i]=i+1;
      lb[i]=i-1;
    }
    lf[N-1]=1;
    lb[1]=N-1;
    c=1;
    L=N-1;
    nb[0]=0;
    for (i=1; i<N; i++) {
      l=i%(L--);
      while (l--)
	c=lf[c];
      nb[c]=i;
      lf[lb[c]]=lf[c];
      lb[lf[c]]=lb[c];
      c=lf[c];
    }
    scanf("%d", &I);
    printf("Case #%d:", t);
    while (I--) {
      scanf("%d", &i);
      printf(" %d", nb[i-1]+1);
    }
    printf("\n");
  }
  return 0;
}
