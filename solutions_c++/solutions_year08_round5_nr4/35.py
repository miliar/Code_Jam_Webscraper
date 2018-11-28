#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

#define maxn 11

vector < pair <int, int> > p;

#define mod 10007


int fc[100000001], fcmod[100000001];

long long mpow( int a, int b )
{
  long long res = 1, mul = a;
  while (b)
  {
    if (b & 1)
      res = (res * mul) % mod;
    mul = (mul * mul) % mod;
    b >>= 1;
  }
  return res;
}

long long rev( int x )
{
  return mpow(x, mod - 2);
}

int getC( int a, int b )
{
  //fprintf(stderr, "%d %d\n", a, b);
  return (((fc[a] * rev(fc[b]) % mod) * rev(fc[a - b])) % mod * mpow(mod, fcmod[a] - fcmod[b] - fcmod[a - b])) % mod;
}

int get(int a, int b, int c, int d )
{
  int d1 = c - a, d2 = d - b;
  //fprintf(stderr, "%d %d\n", d1, d2);
  if (d1 == 0 && d2 == 0)
    return  1;
  if (d1 < 0 || d2 < 0)
    return 0;
  int t = 2 * d1 - d2;
 // fprintf(stderr, "t = %d\n", t);
  if (t < 0 || t % 3 != 0)
    return 0;
  t /= 3;
  d2 -= t;
  if (d2 < 0 || d2 % 2 != 0)
    return 0;
  d2 /= 2;
  //fprintf(stderr, "d2 = %d, t = %d\n", d2, t);
  return getC(d2 + t, d2);
}

int cnt( int code )
{
  int res = 0;
  while (code)
    res++, code &= (code - 1);
  return res;
}


#define buben 70000000

int main( void )
{

  fc[0] = 1;
  
  for (int i = 1; i <= buben; i++)
  {
    if (i % 1000000 == 0)
      printf("i = %d\n", i);
    int t = i;
    fc[i] = fc[i - 1];
    fcmod[i] = fcmod[i - 1];
    while (t % mod == 0)
      fcmod[i]++, t /= mod;
    fc[i] = ((long long)fc[i] * t) % mod;
  }
//  fprintf(stderr, "end of precalc\n");
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);
    int h, w, r;
    scanf("%d%d%d", &h, &w, &r);
    p.resize(r);

    for (int i = 0; i < r; i++)
      scanf("%d%d", &p[i].first, &p[i].second);
    sort(p.begin(), p.end());
//    memset(dp, 0, sizeof(dp));
    int res = 0;
    for (int code = 0; code < (1 << r); code++)
    {
      int px = 1, py = 1;
      int curr = 1;
      for (int j = 0; j < r; j++)
        if (((code) >> j) & 1)
        {
          curr = ((long long)curr * get(px, py, p[j].first, p[j].second)) % mod;
          px = p[j].first;
          py = p[j].second;
        }
      curr = ((long long)curr * get(px, py, h, w)) % mod;
    //  fprintf(stderr, "curr = %d\n", curr);
      if (cnt(code) & 1) 
        res -= curr;
      else
        res += curr;
      res = (res % mod + mod) % mod;
    }

    printf("%d\n", res);

  }

  return 0;
}