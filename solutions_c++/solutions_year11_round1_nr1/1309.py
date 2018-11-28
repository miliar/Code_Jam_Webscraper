#include <cstdio>
#include <algorithm>

void solve()
{
  int N, PD, PG;
  scanf("%d%d%d", &N, &PD, &PG);
  if((PD<100) && (PG==100)) {
    puts("Broken");
    return;
  }
  if((PD>0) && (PG==0)) {
    puts("Broken");
    return;
  }
  N = std::min(N, 100);
  for(int i=1; i<=N; ++i) {
    if((i*PD)%100==0) {
      puts("Possible");
      return;
    }
  }
  puts("Broken");
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int Ts=1; Ts<=T; ++Ts) {
    printf("Case #%d: ", Ts);
    solve();
  }
  return 0;
}
