#include <cstdio>
#include <fstream>
#include <iostream>
using namespace std;

#define N 110

int main()
{
  int T, n, lo, lb, x, so, sb, t, io, ib, in, ao[N], po[N], ab[N], pb[N];
  bool flag;
  char c;
  ifstream cin("d.in");
  FILE *fout = fopen("d.txt", "w");
  
  cin >> T;
  for (int k = 1; k <= T; k++)
  {
    cin >> n;
    lo = lb = 0;
    for (int i = 0; i < n; i++)
    {
      cin >> c >> x;
      if (c == 'O') {ao[lo] = x; po[lo++] = i;}
      else {ab[lb] = x; pb[lb++] = i;}
    }
    
    so = sb = 1; t = io = ib = in = 0;
    while (in < n)
    {
      t++;
      flag = false;
      if (io < lo)
      if (so != ao[io]) so += so > ao[io] ? -1 : 1;
      else if (po[io] == in) {flag = true; io++;}
      if (ib < lb)
      if (sb != ab[ib]) sb += sb > ab[ib] ? -1 : 1;
      else if (pb[ib] == in) {flag = true; ib++;}
      if (flag) in++;
    }
    
    fprintf(fout, "Case #%d: %d\n", k, t);
  }
  
  fclose(fout);
  return 0;
}
