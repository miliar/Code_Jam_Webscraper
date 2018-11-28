#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  int T, N; scanf("%d", &T);

  for(int test = 1; test <= T; test++) {
    scanf("%d", &N);

    int sum=0, zor=0, m=887897987, x;
    for(int i=1; i<=N; i++) {
      scanf("%d", &x);
      sum += x;
      zor ^= x;
      m = min(m, x);
    }

    if(zor == 0) printf("Case #%d: %d\n", test, sum-m);
    else printf("Case #%d: NO\n", test);    
  }
}
