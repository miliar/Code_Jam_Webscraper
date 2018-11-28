#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

typedef long double dbl;

#define maxn 40

int n;
dbl x[maxn], y[maxn], r[maxn];

dbl sqr( dbl a )
{
  return a * a;
}

vector <pair <dbl, dbl> > cross( dbl x1, dbl y1, dbl r1, dbl x2, dbl y2, dbl r2 )
{
  vector <pair <dbl, dbl> > res;
  if (sqr(x1 - x2) + sqr(y1 - y2) < 0.5 && fabs(r1 - r2) < 1e-9)
  {
    res.push_back(make_pair(x1 + r1, y1));
    return res;
  }
  if (sqr(x1 - x2) + sqr(y1 - y2) > sqr(r1 + r2) * (1 + 1e-14) || sqr(x1 - x2) + sqr(y1 - y2) < 0.5)
    return res;
  if (sqr(x1 - x2) + sqr(y1 - y2) >= sqr(r1 + r2) * (1 - 1e-14))
  {
    res.push_back(make_pair((x1 * r2 + x2 * r1) / (r1 + r2), (y1 * r2 + y2 * r1) / (r1 + r2)));
    return res;
  }
  dbl a = 2 * (x2 - x1);
  dbl b = 2 * (y2 - y1);
  dbl c = x1 * x1 - x2 * x2 + y1 * y1 - y2 * y2 + r2 * r2 - r1 * r1;
  dbl d = sqrt(a * a + b * b);
  a /= d, b /= d, c /= d;
  dbl dist = fabs(a * x1 + b * y1 + c);
  dbl move = sqrt(r1 * r1 - dist * dist);
  for (int s1 = -1; s1 <= 1; s1++)
    for (int s2 = -1; s2 <= 1; s2++)
    {
      dbl x = x1 + s1 * a * dist - s2 * b * move;
      dbl y = y1 + s1 * b * dist + s2 * a * move;
      res.push_back(make_pair(x, y));
    }
  return res;
}

bool testR( dbl rr )
{
  for (int i1 = 0; i1 < n; i1++)
    for (int j1 = i1; j1 < n; j1++)
      for (int i2 = 0; i2 < n; i2++)
        for (int j2 = i2; j2 < n; j2++)
        {
          vector <pair <dbl, dbl> > tmp1 = cross(x[i1], y[i1], rr - r[i1], x[j1], y[j1], rr - r[j1]);
          vector <pair <dbl, dbl> > tmp2 = cross(x[i2], y[i2], rr - r[i2], x[j2], y[j2], rr - r[j2]);
          for (int t1 = 0; t1 < (int)tmp1.size(); t1++)
            for (int t2 = 0; t2 < (int)tmp2.size(); t2++)
            {
              bool good = true;
              for (int k = 0; k < n; k++)
                if ( (r[k] > rr * (1 + 1e-12) || sqr(x[k] - tmp1[t1].first) + sqr(y[k] - tmp1[t1].second) > sqr(rr - r[k]) * (1 + 1e-12)) &&
                     (r[k] > rr * (1 + 1e-12) || sqr(x[k] - tmp2[t2].first) + sqr(y[k] - tmp2[t2].second) > sqr(rr - r[k]) * (1 + 1e-12)))
                  good = false, k = n;
              if (good)
                return true;
            }
        }
//  fprintf(stderr, "testR(rr = %.5Lf) = false\n", rr);
  return false;
}

int main()
{
  int testN;
  scanf("%d", &testN);
  for (int test = 1; test <= testN; test++)
  {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
      scanf("%Lf%Lf%Lf", &x[i], &y[i], &r[i]);
    dbl minR = 0.0, maxR = 10000;
//    testR(2.1);
  for (int counter = 0; counter < 100; counter++)
    {
      dbl aveR = 0.5 * (minR + maxR);
      if (testR(aveR))
        maxR = aveR;
      else
        minR = aveR;
    }
    printf("Case #%d: %.15Lf\n", test, minR);
  }
  return 0;
}

