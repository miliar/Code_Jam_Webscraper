#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int t=1; t<=T; t++) {
    int L, Lt, N, C;
    scanf("%d %d %d %d", &L, &Lt, &N, &C);
    long long DD[C];
    for (int i=0; i<C; i++) {
      scanf("%lld", &DD[i]);
    }
    long long S[N];
    memset(S, 0, sizeof(long long) * N);
    long long cur = 0;
    for (int i=0; i<N; i++) {
      long long d = DD[i % C];
      cur += 2 * d;
      if (cur > Lt) {
        S[i] = min(2*d, cur - Lt) / 2;
      }
      //printf("S[%d] = %d\n", i, S[i]);
    }
    sort(S, S+N);
    for (int i=N-1; i >= N-L; i--) {
      cur -= S[i];
    }
    printf("Case #%d: %lld\n", t, cur);
  }
  return 0;
}
