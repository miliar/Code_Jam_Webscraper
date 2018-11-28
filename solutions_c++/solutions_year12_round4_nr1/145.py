#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 10000;
int len[MAXN], poss[MAXN], dst[MAXN];

int main() {
  int T;
  scanf("%d", &T);
  for(int tc = 1; tc <= T; ++tc) {
    int N, D;

    scanf("%d", &N);
    for(int i = 0; i < N; ++i)
      scanf("%d%d", dst + i, len + i);

    scanf("%d", &D);

    for(int i = 0; i < N; ++i)
      poss[i] = -1;

    poss[0] = dst[0];
    int cx = 1;

    bool possible = false;
    for(int i = 0; i < N; ++i) {
      while(cx < N && poss[cx] == -1 && dst[cx] <= dst[i] + poss[i]) {
        poss[cx] = min(len[cx], dst[cx] - dst[i]);
        ++cx;
      }

//      printf("Line %d: %d + %d\n", i, dst[i], poss[i]);
      possible |= dst[i] + poss[i] >= D;
    }

    printf("Case #%d: %s\n", tc, possible?"YES":"NO");
  }
}
