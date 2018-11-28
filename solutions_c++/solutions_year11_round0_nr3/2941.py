#include <cstdio>
#include <iostream>
using namespace std;

#define N 20

int main()
{
  int T, n, m, maxc, x, y, sx, sy, a[N];
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("d.txt", "w");
  
  fscanf(fin, "%d", &T);
  for (int t = 1; t <= T; t++)
  {
    fscanf(fin, "%d", &n);
    for (int i = 0; i < n; i++)
      fscanf(fin, "%d", &a[i]);
    
    maxc = -1; m = 1 << (n - 1);
    for (int i = 1; i < m; i++)
    {
      x = y = sx = sy = 0;
      for (int j = 0; j < n; j++)
        if ((1 << j) & i) {sx += a[j]; x ^= a[j];}
        else {sy += a[j]; y ^= a[j];}
      
      if (x == y)
      {
        if (sx > maxc) maxc = sx;
        if (sy > maxc) maxc = sy;
      }
    }
    
    if (maxc == -1) fprintf(fout, "Case #%d: NO\n", t);
    else fprintf(fout, "Case #%d: %d\n", t, maxc);
  }
  
  fclose(fout);
  return 0;
}
