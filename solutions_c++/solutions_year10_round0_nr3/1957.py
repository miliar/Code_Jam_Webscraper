
#include <cstdio>

const int N = 1000;

typedef long long ll;

int size[N];
int next[N];
ll sum[N];

int init(int k, int n)
{
  ll t_sum = 0;
  int idx;

  for (int i = 0; i < n; i++)
    {
      if (size[i] > k)
	{
	  next[i] = -1;
	  sum[i] = 0;

	  return 1;
	}

      if (i == 0)
	{
	  t_sum = 0;
	  idx = 0;
	}
      else
	{
	  t_sum = sum[i - 1] - size[i - 1];
	  idx = next[i - 1];
	}

      for (; ; )
	{
	  if (t_sum + size[idx] > (ll)k)
	    break;
	  t_sum += size[idx];

	  idx++;
	  if (idx >= n)
	    idx = 0;

	  if (idx == i)
	    break;
	}

      next[i] = idx;
      sum[i] = t_sum;
    }

  return 0;
}

ll solve(int r, int k, int n)
{
  //int st = init(k, n);
  init(k, n);

  //debug
  /*
  printf("size:\n");
  for (int i = 0; i < n; i++)
    printf("%d ", size[i]);
  putchar('\n');

  printf("next:\n");
  for (int i = 0; i < n; i++)
    printf("%d ", next[i]);
  putchar('\n');

  printf("sum:\n");
  for (int i = 0; i < n; i++)
    printf("%lld ", sum[i]);
  putchar('\n');
  */

  /*
  int t = 0;
  ll t_sum = 0;

  for (int i = 0; ; i = next[i])
    {
      t++;
      t_sum += sum[i];

      if (next[i] <= 0)
	break;
    }

  ll res = 0;
  int m = 0;

  if (st == 0)
    {
      res = (r / t) * t_sum;
      m = r % t;
    }
  else
    {
      if (r >= t)
	res = t_sum;
      else
	m = r;
    }

  for (int i = 0; m--; i = next[i])
    res += sum[i];
  */

  ll res = 0;
  for (int i = 0; r--; i = next[i])
    {
      if (i < 0)
	break;

      res += sum[i];
    }

  return res;
}

int main()
{
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++)
    {
      int r, k, n;
      scanf("%d%d%d", &r, &k, &n);

      for (int i = 0; i < n; i++)
	scanf("%d", &size[i]);

      printf("Case #%d: %lld\n", t, solve(r, k, n));
    }

  return 0;
}
