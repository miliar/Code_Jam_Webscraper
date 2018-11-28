#include <cstdio>
#include <algorithm>

using namespace std;

long long N;
int PG, PD;

inline void
read_input()
{
  scanf("%lld %d %d", &N, &PD, &PG);
}

inline void
solve()
{
  if (0 == PG || 100 == PG) {
    if (PD == PG)
      printf("Possible\n");
    else
      printf("Broken\n");
    return;
  }

  for (int D = 1; D <= min(N, (long long)100); ++D)
    if ((PD*D) % 100 == 0) {
      printf("Possible\n");
      return;
    }
      
  printf("Broken\n");
}

int
main()
{
  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i) {
    printf("Case #%d: ", i + 1);

    read_input();
    solve();
  }

  return (0);
}
