#include <cstdio>

typedef long long huge;

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for (int test = 0; test < ntests; ++test)
    {
      huge n, k;
      scanf(" %lld %lld", &n, &k);
      huge mask = (1ll<<n)-1;
      printf("Case #%d: ", test+1);
      if ((k & mask) == mask)
	printf("ON\n");
      else
	printf("OFF\n");
    }
  return 0;
}
