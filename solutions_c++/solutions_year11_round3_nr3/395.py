#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int t=0; t<T; t++) {
    printf("Case #%d: ", t+1);
    int N, L, H;
    scanf("%d %d %d\n", &N, &L, &H);
    const int size = 10001;
    int F[size];
    memset(F, 0, sizeof(int) * size);
    for (int n = 0; n < N; n++) {
      int f;
      scanf("%d", &f);
      for (int i = L; i <= H; i ++ ) {
        if (i % f == 0 || f % i == 0) {
          F[i]++;
        }
      }
      //for (int i = max(f, L); i <= H; i += f) {
        //F[i]++;
      //}
    }
    bool found = false;
    for (int i = L; i <= H; i ++ ) {
      //printf("%d ", F[i]);
      if (F[i] == N) { 
        printf("%d\n", i);
        found = true;
        break;
      }
    }
    if (!found) {
      printf("NO\n");
    }
  }
  return 0;
}
