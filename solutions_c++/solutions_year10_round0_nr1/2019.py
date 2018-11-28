
#include <cstdio>

bool state(int n, int k)
{
  int m = 1 << n;

  return (k % m) == (m - 1);
}

int main()
{
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++)
    {
      int n, k;
      scanf("%d%d", &n, &k);

      printf("Case #%d: ", t);
      if (state(n, k))
	printf("ON\n");
      else
	printf("OFF\n");
    }

  return 0;
}
