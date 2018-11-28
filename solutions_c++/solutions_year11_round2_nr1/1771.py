#include <stdio.h>
#include <iostream>
using namespace std;

#define N 110

int main()
{
  char c, a[N][N];
  int T, n, y, yy;
  double x, xx, wp[N], owp[N], oowp[N];
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("d.txt", "w");
  
  fscanf(fin, "%d", &T);
  for (int t = 1; t <= T; t++)
  {
    fscanf(fin, "%d", &n);
    for (int i = 0; i < n; i++)
    {
      fscanf(fin, "%c", &c);
      for (int j = 0; j < n; j++)
        fscanf(fin, "%c", &a[i][j]);
    }
    
    for (int i = 0; i < n; i++)
    {
      x = y = 0;
      for (int j = 0; j < n; j++)
      {
        if (a[i][j] != '.') y++;
        if (a[i][j] == '1') x++;
      }
      wp[i] = x / y;
    }
    
    for (int i = 0; i < n; i++)
    {
      xx = 0; yy = 0;
      for (int j = 0; j < n; j++)
        if (a[i][j] != '.')
        {
          yy++;
          x = y = 0;
          for (int k = 0; k < n; k++)
            if (k != i)
            {
              if (a[j][k] != '.') y++;
              if (a[j][k] == '1') x++;
            }
          xx += x / y;
        }
      owp[i] = xx / yy;
    }
    
    for (int i = 0; i < n; i++)
    {
      x = y = 0;
      for (int j = 0; j < n; j++)
        if (a[i][j] != '.') {x += owp[j]; y++;}
      oowp[i] = x / y;
    }
    
    fprintf(fout, "Case #%d:\n", t);
    for (int i = 0; i < n; i++)
      fprintf(fout, "%.8lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
  }
  
  fclose(fout);
  return 0;
}
