
#include <cstring>
#include <cstdio>

const int P = 10;
const int N = 1 << P;

int m[N];

int flag[N];

int solve(int p)
{
  memset(flag, 0, sizeof(int) * N);

  int r = 0;
  int n = 1 << p;
  for (int i = 0; i < n; i++)
    {
      int miss = m[i];

      for (int idx = (n + i) >> 1; idx >= 1; idx >>= 1)
	{
	  if (flag[idx] == 0 && miss <= 0)
	    {
	      flag[idx] = 1;
	      r++;
	    }

	  miss--;
	}
    }

  return r;
}

int main()
{
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++)
    {
      int p;
      scanf("%d", &p);

      int n = 1 << p;
      for (int i = 0; i < n; i++)
	scanf("%d", &m[i]);

      int price;
      for (int i = 0; i < n - 1; i++)
	scanf("%d", &price);

      printf("Case #%d: %d\n", t, solve(p) * price);
    }

  return 0;
}
