#include <map>
#include <cstdio>
#include <cstring>

using namespace std;

int N, K;
char a[55][55], b[55][55];

int cnt (int i, int j, int di, int dj, char c)
{
   if (i < 0 || j < 0 || i >= N || j >= N || b[i][j] != c)
      return 0;
   return 1 + cnt (i + di, j + dj, di, dj, c);
}

int main ()
{
   int cases;
   scanf ("%d", &cases);

   for (int test = 1; test <= cases; test++)
   {
      printf ("Case #%d: ", test);
      scanf ("%d%d\n", &N, &K);

      for (int i = 0; i < N; i++)
         gets (a[i]);

      memset (b, 0, sizeof(b));
      for (int i = 0; i < N; i++)
         for (int j = 0; j < N; j++)
            b[i][j] = a[N - j - 1][i];

      for (int i = N - 1; i >= 0; i--)
         for (int j = 0; j < N; j++)
            if (b[i][j] != '.')
            {
               int k = i;
               while (k < N - 1 && b[k + 1][j] == '.')
                  k++;
               b[k][j] = b[i][j];
               if (k != i)
                  b[i][j] = '.';
            }

      map < char, bool > win;
      win['B'] = false;
      win['R'] = false;
      for (int i = 0; i < N; i++)
         for (int j = 0; j < N; j++)
            if (b[i][j] != '.')
            {
               if (cnt (i, j, 0, 1, b[i][j]) >= K ||
                  cnt (i, j, 1, 0, b[i][j]) >= K ||
                  cnt (i, j, 1, 1, b[i][j]) >= K ||
                  cnt (i, j, 1, -1, b[i][j]) >= K)
                  win[b[i][j]] = true;
            }
      if (win['B'] && win['R'])
         puts ("Both");
      else if (win['B'])
         puts ("Blue");
      else if (win['R'])
         puts ("Red");
      else
         puts ("Neither");
   }

   return 0;
}
