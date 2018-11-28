#include <cstdio>

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int N, K;
    scanf("%d%d", &N, &K);
    printf("Case #%d: %s\n", t, ((K+1)%(1<<N))?"OFF":"ON");
  }
  return 0;
}
