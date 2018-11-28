#include<cstdio>

typedef long long ll;

int g[1000];
ll c[1000];
int h[1000];
int d[1000];
ll e[1000];

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; t++)
    {
      int R, k, N;
      scanf("%d%d%d", &R, &k, &N);
      for (int i = 0 ; i < N ; i++)
	scanf("%d", &g[i]);
      for (int i = 0 ; i < N ; i++)
	{
	  c[i] = g[i];
	  d[i] = -1;
	  for (h[i] = (i+1)%N ; h[i] != i ; h[i] = (h[i]+1)%N)
	    {
	      if (c[i] + g[h[i]] > k)
		break;
	      c[i] += g[h[i]];
	    }
	}
      ll C = 0;
      int H = 0;
      int r = 0;
      for ( ; d[H] < 0 && r < R ; ++r)
	{
	  //	  printf("C %lld, H %d, r %d, c[H] %lld, h[H] %d\n", C, H, r, c[H], h[H]);
	  e[H] = C;
	  C += c[H];
	  d[H] = r;
	  H = h[H];
	}
      //      printf("end C %lld, H %d, r %d, c[H] %lld, h[H] %d, d[H] %d, e[H] %lld\n", C, H, r, c[H], h[H], d[H], e[H]);
      if (r < R)
	{
	  int m = (R - d[H]) / (r - d[H]) - 1;
	  C += (C - e[H]) * m;
	  r += (r - d[H]) * m;
	  for ( ; r < R ; ++r)
	    {
	      C += c[H];
	      H = h[H];
	    }
	}
      printf("Case #%d: %lld\n", t, C);
    }
}
