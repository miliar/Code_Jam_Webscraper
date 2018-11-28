#include <cstdio>

int main(int argc, const char *argv[]) {
  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; i++) {
    int N, S, p;
    int sum = 0;
    scanf("%d%d%d", &N, &S, &p);
    for(int j = 0; j < N; j++) {
      int t;
      scanf("%d", &t);
      if(t == 0) {
        if(p == 0) sum++;
      } else if(t == 1) {
        if(p <= 1) sum++;
      } else if(t == 2) {
        if(p <= 1) {
          sum++;
        } else if(p == 2 && S > 0) {
          sum++;
          S--;
        }
      } else if(t/3 + (t % 3 == 0 ? 0 : 1) >= p) {
        sum++;
      } else if(t/3 + (t % 3 == 2 ? 2 : 1) >= p && S > 0) {
        sum++;
        S--;
      }
    }
    printf("Case #%d: %d\n", i+1, sum);
  }
  return 0;
}
