#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

void solve();
int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    printf("Case #%d: ", test_case);
    solve();
  }
}

int n;
void solve() {
  scanf("%d", &n);
  ll all = 0;
  ll minValue = 1 << 30;
  ll xors = 0;
  REP(i, n) {
    ll v;
    scanf("%lld", &v);
    all += v;
    minValue = min(minValue, v);
    xors ^= v;
  }
  if (xors != 0) {
    puts("NO");
  } else {
    printf("%lld\n", all - minValue);
  }
}
