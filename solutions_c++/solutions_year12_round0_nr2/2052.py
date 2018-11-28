#include <cstdio>

int ti[1000];

int main() {
  int T;
  scanf("%d", &T);

  for(int tc = 1; tc <= T; ++tc) {
    printf("Case #%d: ", tc);

    int N, S, p, res = 0;
    scanf("%d%d%d", &N, &S, &p);

    for(int i = 0; i < N; ++i) {
      int t, bis, bins;
      scanf("%d", &t);

      switch(t % 3) {
        case 0:
          bins = t / 3;
          bis = t == 0 || t == 30 ? -1000000 : t / 3 + 1;
          break;
        case 1:
          bins = t / 3 + 1;
          bis = t / 3 + 1;
          break;
        case 2:
          bins = t / 3 + 1;
          bis = t == 29 ? -1000000 : t / 3 + 2;
      }

      if(bins >= p)
        ++res;
      else if(bis >= p && S)
        --S, ++res;
    }

    printf("%d\n", res);
  }
}
