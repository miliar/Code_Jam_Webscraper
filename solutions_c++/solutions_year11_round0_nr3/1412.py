#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  int T; scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int N; scanf("%d", &N);

    int S = 0;
    int SS = 0;
    int mn = 1000000;
    for(int i = 0; i < N; i++) {
      int x;
      scanf("%d", &x);
      S ^= x;
      SS += x;
      mn = min(mn, x);
    }
    printf("Case #%d: ", t);
    if(S) {
      printf("NO\n");
    } else {
      printf("%d\n", SS - mn);
    }
  }
}
