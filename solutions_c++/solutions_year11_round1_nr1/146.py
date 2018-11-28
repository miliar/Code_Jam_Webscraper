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

using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
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

int gcd(int x, int y) { return x ? gcd(y % x, x) : y; }

bool ok(ll N, int Pd, int Pg) {
  if (Pg == 100) return Pd == 100;
  if (Pg == 0) return Pd == 0;
  if (!Pd) return true;
  int mul = 100 / gcd(Pd, 100);
  ll D = N / mul * mul;
  if (!D) return false;
  assert((D*Pd) % 100 == 0);
  assert(0 < D && D <= N);
  return true;
}

void solve(int P) {
  ll N, Pd, Pg;
  scanf("%lld%lld%lld", &N, &Pd, &Pg);
  print("Case #%d: %s\n", P, ok(N, Pd, Pg) ? "Possible" : "Broken");
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
