#include <cstdio>

int main()
{
  int T;
  scanf("%d", &T);
  for(int cases=1; cases<=T; ++cases) {
    int N;
    scanf("%d", &N);
    int res = N;
    for(int i=1; i<=N; ++i) {
      int x;
      scanf("%d", &x);
      if(x==i) --res;
    }
    printf("Case #%d: %.6f\n", cases, (float)res);
  }
  return 0;
}
