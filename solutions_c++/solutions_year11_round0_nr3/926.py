#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);

  for(int t = 1; t <= T; t++) {
    int N;
    scanf("%d", &N);
    int sum = 0, m = 1<<25, x = 0;
    for(int i = 0; i < N; i++) {
      int v;
      scanf("%d", &v);
      sum += v;
      m = min(m, v);
      x ^= v;
    }

    if(x == 0)
      printf("Case #%d: %d\n", t, sum-m);
    else
      printf("Case #%d: NO\n", t);
  }

}
