#include <algorithm>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <iostream>

#define inf 1e20
#define eps 1e-9

using namespace std;

#define maxn 1002

double x[maxn], y[maxn], z[maxn], p[maxn], mind[4], maxd[4], tmind[4], tmaxd[4];

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  cin >> tn;
  for (int tt = 1; tt <= tn; tt++)
  {
    cerr << tt << endl;
    printf("Case #%d: ", tt);

    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
      cin >> x[i] >> y[i] >> z[i] >> p[i];
    double l = 0, r = 1e10;
    while (r - l > eps)
    {
      double c = (r + l) / 2;
      for (int i = 0; i < 4; i++)
        mind[i] = -inf, maxd[i] = +inf;
      for (int i = 0; i < n; i++)
      {
        for (int j = 0; j < 4; j++)
          tmind[j] = +inf, tmaxd[j] = -inf;
        for (int code = 0; code < 8; code++)
        {
          int rcode = code;
          if (code >= 4)
            rcode = 7 & ~code;
          double val = c * p[i];
          if ((code >> 0) & 1)
            val -= x[i];
          else
            val += x[i];
          if ((code >> 1) & 1)
            val -= y[i];
          else
            val += y[i];
          if ((code >> 2) & 1)
            val -= z[i];
          else
            val += z[i];
          if (code >= 4)
            val = -val;
          tmind[rcode] <?= val;
          tmaxd[rcode] >?= val;
        }
        for (int j = 0; j < 4; j++)
        {
          mind[j] >?= tmind[j];
          maxd[j] <?= tmaxd[j];
        }
      }
      bool ok = true;
      for (int i = 0; i < 4; i++)
        ok &= mind[i] < maxd[i];
      if (ok)
        r = c;
      else
        l = c;
    }
    printf("%.20lf\n", l);

  }


  return 0;
}