#include <stdio.h>

int N, S, P, Ti[100];

int Solve() {
  int count = 0;
  int Tb[100], Ta[100], Tm[100];

  //  printf("##################\n");
  //  printf("# N=%d, S=%d, P=%d\n", N, S, P);

  // prepare
  for (int i=0; i!=N; ++i) {
    Ta[i] = Ti[i] % 3;
    Tb[i] = (Ti[i] - Ta[i])/3;
    if (Ta[i] > 0) {
      Tm[i] = Tb[i] + 1;
    } else {
      Tm[i] = Tb[i];
    }
    //    printf("%d, %d, %d\n", Tb[i], Ta[i], Tm[i]);
  }

  // Search near P
  for (int i=0; i!=N; ++i) {
    if (Tm[i] == P-1 && (Ta[i] == 0 || Ta[i] == 2) && S>0 && Tb[i] != 0) {
      S--;
      Tm[i]++;
      //      printf("! S=%d i=%d\n", i);
    }
  }

  for (int i=0; i!=N; ++i) {
    if (Tm[i]>=P)
      count++;
  }

  return count;
}

int main() {
  // read
  int T;
  scanf("%d", &T);

  // loop
  int i, j, k;
  for (i = 1; i <= T; ++i) {
    scanf("%d", &N);
    scanf("%d", &S);
    scanf("%d", &P);
    for (j = 0; j != N; ++j) {
      scanf("%d", &Ti[j]);
    }

    printf("Case #%d: %d\n", i, Solve());
  }
  return 0;
}
