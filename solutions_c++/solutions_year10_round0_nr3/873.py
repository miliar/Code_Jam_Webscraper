#include <stdio.h>
#include <string.h>

int k;
int ng;
int g[1000];
long long memo[1000][2];

void runCoaster(long long &offset, long long &profit) {
  if (memo[offset][0] == -1) {
    int loading = 0;
    int no = offset;
    long long np = 0;

    while (true) {
      if (loading + g[no] <= k) {
        loading +=  g[no];
        np += g[no];
        no = (no + 1)%ng;
      } else break;

      if (no == offset) break;
    }

    memo[offset][0] = no;
    memo[offset][1] = np;
  }

  profit += memo[offset][1];
  offset = memo[offset][0];
}

int main() {
  int T, r;
  scanf ("%d", &T);

  for (int cs=1; cs<=T; cs++) {
    long long profit = 0;
    memset(memo, -1, sizeof(memo));

    scanf("%d %d %d", &r, &k, &ng);

    for (int i=0; i<ng; i++)
      scanf("%d", g+i);

    long long offset = 0;
    for (int i=0; i<r; i++)
      runCoaster(offset, profit);

    printf("Case #%d: %lld\n", cs, profit);
  }
}
