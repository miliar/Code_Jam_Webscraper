#include <cstdio>
#include <iostream>
#include <vector>
#include <memory.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 1024;
const ld eps = 1e-9;

struct node
{
  int l, r, v;
};

bool operator<(const node& a, const node& b)
{
  if (a.v != b.v) return a.v < b.v;
  return a.r-a.l < b.r-b.l;
}

node a[maxn];
int n, x, s, r;
ld t;

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  int tc; scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {
    int _t;
    scanf("%d %d %d %d %d", &x, &s, &r, &_t, &n);
    t = _t;
    forn (i, n) scanf("%d %d %d", &a[i].l, &a[i].r, &a[i].v);
    sort(a, a+n);
    forn (i, n)
      x -= a[i].r-a[i].l;
    //cout << x << endl;  
    ld res = 0;
    if (1.0*x/r < t+eps)
      t -= 1.0*x/r, res += 1.0*x/r;
    else
      res += t + 1.0*(x-t*r)/s, t = 0;
    forn (i, n)
    {
      int d = a[i].r - a[i].l;
    //  cout << d << " " << t << endl;
      if (1.0*d/(r+a[i].v) < t+eps)
        t -= 1.0*d/(r+a[i].v), res += 1.0*d/(r+a[i].v);
      else
        res += t + 1.0*(d-t*(r+a[i].v))/(s+a[i].v), t = 0;
    }    
    printf("Case #%d: %.10f\n", tt, double(res));
  }
  
  return 0;
}
