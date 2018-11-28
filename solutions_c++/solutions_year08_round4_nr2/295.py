#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int x1, y1, x2, y2, x3, y3, N, M, A;

bool solve()
{
  int C, D, E;
  for (x1 = 0, y1 = 0; y1 <= M; y1++)
    {
      for (y2 = M, x2 = 0; x2 <= N; x2++)
	{
	  if (x1 == x2 && y1 == y2) continue;
	  C = x2 - x1, D = y2 - y1, E = A + C * y1 - D * x1;
	  if (D) 
	    {
	      for (y3 = 0; y3 <= M; y3++)
		{
		  if ((C * y3 - E) % D == 0) 
		    {
		      x3 = (C * y3 - E) / D;
		      if (x3 >= 0 && x3 <= N) return 1;
		    }
		}
	      E = -A + C * y1 - D * x1;
	      for (y3 = 0; y3 <= M; y3++)
		{
		  if ((C * y3 - E) % D == 0) 
		    {
		      x3 = (C * y3 - E) / D;
		      if (x3 >= 0 && x3 <= N) return 1;
		    }
		}
	    }
	  else
	    {
	      for (x3 = 0; x3 <= N; x3++)
		{
		  if ((D * x3 + E) % C == 0) 
		    {
		      y3 = (D * x3 + E) / C;
		      if (y3 >= 0 && y3 <= M) return 1;
		    }
		}
	      E = -A + C * y1 - D * x1;
	      for (x3 = 0; x3 <= N; x3++)
		{
		  if ((D * x3 + E) % C == 0) 
		    {
		      y3 = (D * x3 + E) / C;
		      if (y3 >= 0 && y3 <= M) return 1;
		    }
		}
	    }
	}
    }
  return 0;
}

int main()
{
  int data;
  scanf("%d", &data);
  for (int i = 1; i <= data; i++)
    {
      scanf("%d%d%d", &N, &M, &A);
      if (solve()) printf("Case #%d: %d %d %d %d %d %d\n", i, x1, y1, x2, y2, x3, y3);
      else printf("Case #%d: IMPOSSIBLE\n", i);
    }
}
