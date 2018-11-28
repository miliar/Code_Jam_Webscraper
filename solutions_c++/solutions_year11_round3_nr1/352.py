#include <cstdio>
#include <iostream>
using namespace std;

#define N 60

int main()
{
  int T, n, m;
  bool flag;
  char c, a[N][N];
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("d.txt", "w");
  
  for (int i = 0; i < 55; i++)
    for (int j = 0; j < 55; j++)
      a[i][j] = '.';
  
  fscanf(fin, "%d", &T);
  for (int t = 1; t <= T; t++)
  {
    fscanf(fin, "%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
    {
      fscanf(fin, "%c", &c);
      for (int j = 1; j <= m; j++)
        fscanf(fin, "%c", &a[i][j]);
    }
    
    flag = true;
    for (int i = 1; i <= n && flag; i++)
    {
      for (int j = 1; j <= m; j++)
        if (a[i][j] == '#')
        {
          if (a[i][j + 1] != '#' || a[i + 1][j] != '#' || a[i + 1][j + 1] != '#')
          {flag = false; break;}
          a[i][j] = a[i + 1][j + 1] = '/'; 
          a[i][j + 1] = a[i + 1][j] = '\\';
        }
    }
    
    fprintf(fout, "Case #%d:\n", t);
    if (!flag) fprintf(fout, "Impossible\n");
    else
      for (int i = 1; i <= n; i++)
      {
        for (int j = 1; j <= m; j++)
          fprintf(fout, "%c", a[i][j]);
        fprintf(fout, "\n");
      }
  }
  
  fclose(fout);
  return 0;
}
