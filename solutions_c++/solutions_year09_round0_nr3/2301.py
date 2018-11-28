#include <cstdio>
#include <cstdlib>

using namespace std;

int N;
int W[20];
char C;
char S[]="welcome to code jam";

int main() {
  scanf("%d", &N);
//  printf("%d\n", N);
  scanf("%c", &C);
//  printf("%c\n", C);
  for (int i=1; i<=N; i++) {
    for (int j=1; j<=19; j++) W[j]=0;
    W[0]=1;
    while ((C<'a' || C>'z')&& C!=' ') scanf("%c", &C);
    while ((C>='a' && C<='z')|| C==' ') {
      for (int j=18; j>=0; j--) W[j+1]=(W[j+1]+((C==S[j])?W[j]:0)) % 10000;
      if (scanf("%c", &C)==EOF) break;
    }
    printf ("Case #%d: %.4d\n", i, W[19]);
  }
  return 0;
}