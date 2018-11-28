#include <stdio.h>
#include <stdlib.h>

#define FOR(i, m, n) for (int i=m; i<n; i++)

int ok[1200];
int dalsi[1200];
int N;

int main() {
  int vstupy; scanf("%d", &vstupy);
  FOR (qq, 0, vstupy) {
    int sum=0;
    scanf("%d", &N);
    FOR (i, 0, N+5) ok[i] = 0;
    FOR (i, 1, N+1) {
      scanf("%d", &dalsi[i]);
    }
    FOR (i, 1, N+1) {
      int d=0; int k=i;
      while(ok[k]==0) {
        d++; ok[k] = 1; k = dalsi[k];
      }
      if (d>1)
        sum+=d;
    }
    printf("Case #%d: %f\n", qq+1, (float)sum);
  }
  return 0;
}
