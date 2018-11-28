#include <iostream>
#include <inttypes.h>

typedef int64_t i64;

using namespace std;

int main() {

  int c; cin >> c;

  for (int T=1; c>0; --c,++T) {

    i64 R, k, N; cin >> R >> k >> N;
    i64 group[N], next[N], earn[N];

    for (int i=0;i<N;++i) cin >> group[i];

    for (int i=0;i<N;++i) {

      i64 e = 0, j;
      for (j=0; (j<=N) && (e<=k); j++)
        e += group[(i+j) % N];

      next[i] = (i+j-1) % N;
      earn[i] = e - group[next[i]];
    }

    i64 e = 0, n = 0;
    for (i64 i=0;i<R;++i) {
      e += earn[n];
      n = next[n];
    }

    cout << "Case #" << T << ": " << e << "\n";
  }
}
