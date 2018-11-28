#include <cstdio>
#include <iostream>
using namespace std;

#define N 110

int main()
{
  int T, n, l, h, a[N];
  bool flag;
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("d.txt", "w");
  
  fscanf(fin, "%d", &T);
  for (int t = 1; t <= T; t++)
  {
    fscanf(fin, "%d%d%d", &n, &l, &h);
    for (int i = 0; i < n; i++)
      fscanf(fin, "%d", &a[i]);
    
    fprintf(fout, "Case #%d: ", t);
    for (int i = l; i <= h; i++)
    {
      flag = true;
      for (int j = 0; j < n && flag; j++)
        flag = i % a[j] == 0 || a[j] % i == 0;
      if (flag) {fprintf(fout, "%d\n", i); break;}
    }
    if (!flag) fprintf(fout, "NO\n");
  }
  
  fclose(fout);
  return 0;
}
