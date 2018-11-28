#include <cstdio>

void solve()
{
  int N, K;
  scanf("%d %d", &N, &K);
  int mask = (1 << N)-1;
  if ((K & mask) == mask)
    puts("ON"); else
    puts("OFF");
}

int main()
{
  int N;
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}
