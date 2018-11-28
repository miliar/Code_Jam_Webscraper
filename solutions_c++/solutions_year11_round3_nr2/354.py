#include <cstdio>
#include <iostream>
using namespace std;

#define N 1000010
int b[N], a[N];

inline bool cmp(const int &a, const int &b)
{
  return a > b;
}

int main()
{
  int T, l, n, c, len;
  long long t, dis, ans, sum;
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("d.txt", "w");
  
  fscanf(fin, "%d", &T);
  for (int k = 1; k <= T; k++)
  {
    fscanf(fin, "%d%lld%d%d", &l, &t, &n, &c);
    for (int i = 0; i < c; i++)
    {
      fscanf(fin, "%d", &a[i]);
      for (int j = i + c; j < n; j += c)
        a[j] = a[i];
    }
    
    ans = t; dis = t >> 1; sum = 0;
    for (int i = 0; i < n; i++)
    {
      sum += a[i];
      if (sum > dis)
      {
        b[0] = sum - dis;
        len = n - i;
        memcpy(b + 1, a + i + 1, (len - 1) * sizeof(int));
        sort(b, b + len, cmp);
        for (int j = 0; j < len; j++)
          if (j < l) ans += b[j];
          else ans += b[j] << 1;
        break;
      }
    }
    
    fprintf(fout, "Case #%d: ", k);
    if (sum <= dis)
    {
      sum = 0;
      for (int i = 0; i < n; i++)
        sum += a[i];
      sum <<= 1;
      fprintf(fout, "%lld\n", sum);
    }
    else fprintf(fout, "%lld\n", ans);
  }
  
  fclose(fout);
  return 0;
}
