#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define DEC(i, s) for (int i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())

ll la, ra, lb, rb;

bool gcd(ll a, ll b) {
  if (a < b) { swap(a, b); }
  if (b == 0) { return true; }
  if ((a / b) > 1) { return true; }
  return !gcd(b, a % b);
}

int main() {
  int test;
  int test_case = 0;
  scanf("%d", &test);
  while (test--) {
    test_case++;
    scanf("%lld %lld %lld %lld", &la, &ra, &lb, &rb);
    ll ans = 0;
    FOREQ(a, la, ra) {
      FOREQ(b, lb, rb) {
        if (gcd(a, b)) { ans++; }
      }
    }
    printf("Case #%d: %lld\n", test_case, ans);
  }
}
