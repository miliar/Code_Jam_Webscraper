#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;

#define eps 1e-8

int main()
{
  int T, sum, x, s, r, n, a, b, c, f[210];
  double t, tmp, ans;
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("d.txt", "w");
  
  fscanf(fin, "%d", &T);
  for (int k = 1; k <= T; k++)
  {
    memset(f, 0, sizeof(f));
    fscanf(fin, "%d%d%d%lf%d", &x, &s, &r, &t, &n);
    sum = 0;
    for (int i = 0; i < n; i++)
    {
      fscanf(fin, "%d%d%d", &a, &b, &c);
      f[s + c] += b - a;
      sum += b - a;
    }
    f[s] = x - sum;
    
    ans = 0;
    for (int i = 1; i <= 200; i++)
      if (f[i] != 0)
      {
        if (t == 0) ans += (double)f[i] / i;
        else
        {
          tmp = (double)f[i] / (i - s + r);
          if (tmp <= t) {ans += tmp; t -= tmp;}
          else {ans += t + ((double)f[i] - t * (i - s + r)) / i; t = 0;}
        }
      }
    
    fprintf(fout, "Case #%d: %.6lf\n", k, ans);
  }
  
  fclose(fout);
  system("pause");
  return 0;
}
