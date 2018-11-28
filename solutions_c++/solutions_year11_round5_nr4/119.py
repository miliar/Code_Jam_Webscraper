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

ll go(ll base, vll mask) {
  if (mask.empty()) {
    ll ans =(ll)(sqrt(1.0*base)+0.5);
    if (ans*ans == base) return base;
    else return -1;
  }
  int i = mask.back();
  mask.pop_back();
  ll ans = go(base, mask);
  if (ans != -1) return ans;
  return go(base+(1LL<<i), mask);
}

void solve(int P) {
  ll base = 0;
  vll mask;
  char str[1000];
  scanf("%s", str);
  int l = strlen(str);
  ll b = 1;
  for (int i = l-1; i >= 0; --i) {
    if (str[i] == '?') mask.push_back(l-i-1);
    else if (str[i] == '1') base |= b;
    b *= 2;
  }
  ll ans = go(base, mask);
  //  printf("%lld\n", ans);
  memset(str, 0, sizeof(str));
  for (int i = 0; ans; ++i, ans /= 2)
    str[i] = '0' + ans%2;
  reverse(str, str+strlen(str));
  print("Case #%d: %s\n", P, str);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
