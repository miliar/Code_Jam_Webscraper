#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>

using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
  assert(scanf("%d", &CASES) == 1);
}

int print(const char *err, ...) {
  va_list pvar;
  va_start(pvar, err);
  vfprintf(stderr, err, pvar);
  return vfprintf(stdout, err, pvar);
}

int dprint(const char *err, ...) { 
  if (debug) {
    va_list pvar;
    va_start(pvar, err);
    return vfprintf(stderr, err, pvar);
  }
  return 0;
}


int W, L, U, G;

double ub[2000], lb[2000];

double area(double x) {
  double res = 0;
  int at = 0;
  while (at+1 <= x) {
    //    printf("%lf %lf %lf %lf\n", ub[i], lb[i], ub[i-1], lb[i-1]);
    res += ((ub[at]-lb[at])+(ub[at+1]-lb[at+1]))*0.5;
    ++at;
  }
  if (at == W) return res;
  assert(at <= x && x <= at+1);
  double u = ub[at]+(ub[at+1]-ub[at])*(x-at);
  double l = lb[at]+(lb[at+1]-lb[at])*(x-at);
  //  printf("%lf: %lf %lf pre %lf", x, u, l, res);
  res += ((ub[at]-lb[at])+(u-l))*0.5*(x-at);
  return res;
}

double findx(double A) {
  double lo = 0, hi = W;
  for (int i = 0; i < 100; ++i) {
    double m = (lo+hi)/2;
    if (area(m) > A) hi = m;
    else lo = m;
  }
  return lo;
}

void solve(int P) {
  assert(scanf("%d%d%d%d", &W, &L, &U, &G) == 4);
  int px = 0;
  for (int i = 0; i < L; ++i) {
    int x, y;
    scanf("%d%d", &x, &y);
    for (int xx = px+1; xx < x; ++xx) {
      lb[xx] = lb[px]+1.0*(y-lb[px])*(xx-px)/(x-px);
    }
    lb[x] = y;
    px = x;
  }
  px = 0;
  for (int i = 0; i < U; ++i) {
    int x, y;
    scanf("%d%d", &x, &y);
    for (int xx = px+1; xx < x; ++xx) {
      ub[xx] = ub[px]+1.0*(y-ub[px])*(xx-px)/(x-px);
    }
    ub[x] = y;
    px = x;
  }
  double tot = area(W);
  //  printf("area %lf\n", tot);
  print("Case #%d:\n", P);
  for (int i = 1; i < G; ++i) {
    print("%.10lf\n", findx(tot*i/G));
  }
  
}


int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
