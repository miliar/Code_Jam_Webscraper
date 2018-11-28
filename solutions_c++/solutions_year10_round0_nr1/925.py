// For my Garfield
// 41 days to our 3 years
// A. Snapper Chain
// Google Code Jam Qualification Round 2010
#include <cstdio>
using namespace std;
int T, N, K;
int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &T);
  for(int t = 1; t <= T; ++ t)
  {
    scanf("%d%d", &N, &K);
    if((K + 1) % (1 << N) == 0)
      printf("Case #%d: ON\n", t);
    else
      printf("Case #%d: OFF\n", t);
  }
  return 0;
}
