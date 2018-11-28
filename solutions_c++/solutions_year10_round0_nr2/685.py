#include<cstdio>
#include<cstdlib>

int gcd(int a, int b)
{
  return b ? gcd(b, a % b) : a;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; t++)
    {
      int N;
      scanf("%d", &N);
      int n[N];
      int r = -1;
      for (int i = 0 ; i < N ; i++)
	{
	  scanf("%d", &n[i]);
	  for (int j = 0 ; j < i ; j++)
	    {
	      if (r < 0)
		r = abs(n[i] - n[j]);
	      else
		r = gcd(r, abs(n[i] - n[j]));
	    }
	}
      int s = n[0] % r;
      printf("Case #%d: %d\n", t, s == 0 ? 0 : r - s);
    }
}
