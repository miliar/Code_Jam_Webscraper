#include <cstdio>
#include <cstdlib>

using namespace std;


int T, H, W;
int A[10000];
char literka[10000];
int gdzie[10000];
char tl;

int niuchaj(int v) {
  if (literka[v]==' ') {
    if (gdzie[v]==v) literka[v]=tl++;
    else literka[v]=niuchaj(gdzie[v]);
  }
  return literka[v];
}

int main() {
  scanf("%d", &T);
  for (int t=1; t<=T; t++) {
  scanf("%d", &H);
  scanf("%d", &W);
  for (int i=0; i<H*W; i++) {
    scanf("%d", &(A[i]));
    gdzie[i]=i;
    literka[i]=' ';
  }
  tl='a';
  for (int i=0; i<H*W; i++) {
    if (i-W>=0 && A[i-W]<A[gdzie[i]]) gdzie[i]=i-W;
    if (i%W>0 && A[i-1]<A[gdzie[i]]) gdzie[i]=i-1;
    if (i%W<W-1 && A[i+1]<A[gdzie[i]]) gdzie[i]=i+1;
    if (i+W<H*W && A[i+W]<A[gdzie[i]]) gdzie[i]=i+W;
//    if (gdzie[i]==i) literka[i]=tl++;
  }

  for (int i=0; i<H*W; i++) {
    niuchaj(i);
  }

  printf ("Case #%d:\n", t);
  for (int i=0; i<H; i++) {
    printf("%c", literka[i*W]);
    for (int j=1; j<W; j++) {
      printf(" %c", literka[i*W+j]);
    }
    printf("\n");
  }
  }
  return 0;
}
