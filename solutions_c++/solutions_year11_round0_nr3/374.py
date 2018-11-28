#include <cstdio>
#include <cstdlib>
#include <algorithm>

int main()
{
  int T;
  scanf("%d", &T);
  for(int cases=1; cases<=T; ++cases) {
    int N;
    int min = 1000000000;
    int mask = 0;
    int sum = 0;
    scanf("%d", &N);
    for(int i=0; i<N; ++i) {
      int x;
      scanf("%d", &x);
      min = std::min(x, min);
      mask ^= x;
      sum += x;
    }
    printf("Case #%d: ", cases);
    if(mask)
      printf("NO\n");
    else
      printf("%d\n", sum-min);
  }
  return 0;
}
