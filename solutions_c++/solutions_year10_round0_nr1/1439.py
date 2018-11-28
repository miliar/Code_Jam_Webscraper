#include<cstdio>

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; t++)
    {
      int N, K;
      scanf("%d%d", &N, &K);
      N = (1 << N) - 1;
      printf("Case #%d: O%s\n", t, (K & N) == N ? "N" : "FF");
    }
}
