#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1010;

struct walk
{
  int bi, ei, wi;
  void read() { scanf("%d%d%d", &bi, &ei, &wi); }

  bool operator < (const walk &p) const
  {
    return bi < p.bi;
  }
} wa[MAXN];

double S, R, len;
int n;
double ti;

void init()
{
  scanf("%lf%lf%lf%lf%d", &len, &S, &R, &ti, &n);
  for (int i = 0; i < n; ++i) wa[i].read();
}

double ti_cal(double wi, double len) {
  double rti = len / (R + wi);
  if (rti <= ti) {
    ti -= rti;
    return rti;
  } else {
   double remain = len - (R + wi) * ti;
   rti =  remain / (S + wi) + ti;
   ti = 0.0;
   return rti;
  }
  return 0.0;
}

void solve()
{
  double ans = 0.0;
  
  sort(wa, wa+n);

  ans += ti_cal(0, wa[0].bi) + ti_cal(0, len - wa[n-1].ei);

  for (int i = 0; i < n; ++i) {
    ans += ti_cal(wa[i].wi, wa[i].ei - wa[i].bi);

    if (i) ans += ti_cal(0, wa[i].bi - wa[i-1].ei);
  }
  
  printf("%.9lf\n", ans);
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    printf("Case #%d: ", l);
    init();
    solve();
  }
  return 0;
}

