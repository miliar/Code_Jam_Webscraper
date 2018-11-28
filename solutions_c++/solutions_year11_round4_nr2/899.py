#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
  int T, r, c, d, mid, a[12][12];
  double midx, midy, sumx, sumy;
  char s;
  bool flag;
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("d.txt", "w");
  
  fscanf(fin, "%d", &T);
  for (int t = 1; t <= T; t++)
  {
    fscanf(fin, "%d%d%d", &r, &c, &d);
    for (int i = 0; i < r; i++)
    {
      fscanf(fin, "%c", &s);
      for (int j = 0; j < c; j++)
      {
        fscanf(fin, "%c", &s);
        a[i][j] = d + s - '0';
      }
    }
    
    flag = false;
    for (mid = min(r, c); mid >= 3 && !flag; mid--)
    {
      for (int i = 0; i <= r - mid && !flag; i++)
        for (int j = 0; j <= c - mid && !flag; j++)
        {
          sumx = sumy = 0;
          midx = i + (double)(mid - 1) / 2;
          midy = j + (double)(mid - 1) / 2;
          for (int x = i; x < i + mid; x++)
          {
            for (int y = j; y < j + mid; y++)
            {
              if (x == i && y == j) continue;
              if (x == i + mid - 1 && y == j + mid - 1) continue;
              if (x == i && y == j + mid - 1) continue;
              if (x == i + mid - 1 && y == j) continue;
              sumx += ((double)x - midx) * a[x][y];
              sumy += ((double)y - midy) * a[x][y];
            }
          }
          if (sumx == 0 && sumy == 0) flag = true;
        }
    }
    
    if (!flag) fprintf(fout, "Case #%d: IMPOSSIBLE\n", t);
    else fprintf(fout, "Case #%d: %d\n", t, mid + 1);
  }
  
  fclose(fout);
  system("pause");
  return 0;
}
