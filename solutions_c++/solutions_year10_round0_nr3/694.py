#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>

int main()
{
  int qnum = 0;
  scanf("%d", &qnum);

  int x = 0;
  while (qnum--)
    {
      x++;
  int y = 0;

  int R;
  int K;
  int N;

  scanf("%d", &R);
  scanf("%d", &K);
  scanf("%d", &N);
  int g[1000];
  int i;
  //printf("N:%d\n", N);
  for (i = 0; i< N; ++i)
    {
      scanf("%d", &g[i]);
    }

  int c[1000];
  int n[1000];
  for (i = 0; i < N; ++i)
    {
      int p = 0;
      int j;
      for (j = 0; j < N; ++j)
	{
	  int idx = (i + j) % N;
	  if (p + g[idx] <= K)
	    {
	      p += g[idx];
	    }
	  else
	    {
	      break;
	    }
	}
      c[i] = p;
      n[i] = (i + j) % N;
      //printf("C:%d N:%d\n", c[i], n[i]);
    }

  long long cost = 0;
  int r;
  int idx = 0;
  for (int r = 0; r < R; ++r)
    {
      cost += c[idx];
      idx = n[idx];
    }


  printf("Case #%d: %lld\n", x, cost);
    }
}
