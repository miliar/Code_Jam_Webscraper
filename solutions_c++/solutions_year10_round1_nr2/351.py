#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

const int INF = (int) 1e9;
const int MAXVAL = 256;

int D, I, M, N;
int a[105];
int dp[105][MAXVAL];

int cost (int x, int y)
{
   if (M == 0)
      return INF;
   if (x == y)
      return 0;
   return ((abs (x - y) - 1) / M) * I;
}

int main ()
{
   int cases;
   scanf ("%d", &cases);

   for (int test = 1; test <= cases; test++)
   {
      printf ("Case #%d: ", test);
      scanf ("%d%d%d%d", &D, &I, &M, &N);
      for (int i = 0; i < N; i++)
         scanf ("%d", &a[i]);

      for (int i = 0; i < N; i++)
         for (int x = 0; x < MAXVAL; x++)
            dp[i][x] = INF;            

      for (int i = 0; i < MAXVAL; i++)
         dp[0][i] = min (abs (a[0] - i), D + I);

      for (int i = 0; i < N - 1; i++)
      {
         dp[i + 1][a[i + 1]] = (i + 1) * D;
         for (int x = 0; x < MAXVAL; x++)
            for (int y = 0; y < MAXVAL; y++)
            {
               if (x == y)
               {
                  dp[i + 1][y] = min (dp[i + 1][y], dp[i][x] + D);
               }

               if (abs (x - y) <= M)
               {
                  dp[i + 1][y] = min (dp[i + 1][y], dp[i][x] + abs (a[i + 1] - y));
               }

               dp[i + 1][y] = min (dp[i + 1][y], dp[i][x] + abs (a[i + 1] - y) + cost (x, y));
            }
      }


      int res = N * D;
      for (int x = 0; x < MAXVAL; x++)
         res = min (res, dp[N - 1][x]);

      printf ("%d\n", res);
   }


   return 0;
}
