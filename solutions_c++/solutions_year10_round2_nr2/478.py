#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
  int qnum = 0;
  scanf("%d", &qnum);

  int x = 0;
  while (qnum--)
    {
      x++;

  int N,K,B,T;

  scanf("%d", &N);
  scanf("%d", &K);
  scanf("%d", &B);
  scanf("%d", &T);

  int X[50];
  int V[50];

  int i, j;
  for (i = 0; i < N; ++i)
    {
      scanf("%d", &X[i]);
    }
  for (i = 0; i < N; ++i)
    {
      scanf("%d", &V[i]);
    }

  int count = 0;

  int m[50];
  for (i = 0; i < N; ++i)
    {
      m[i] = (B - X[i] + (V[i] - 1)) / V[i];
    }

  int obs = 0;
  int ch = 0;
  for (i = N -1 ; i >=0; --i)
    {
      if (m[i] <= T)
	{
	  ch++;
	  count += obs;
	}
      else
	obs++;

      if (ch >= K)
	break;
    }

  if (ch >=K)
    printf("Case #%d: %d\n", x, count);
  else
    printf("Case #%d: IMPOSSIBLE\n", x);
    }
}
