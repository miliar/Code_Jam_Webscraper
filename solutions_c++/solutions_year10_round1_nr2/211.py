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

int D, I, M, N;
int memo[300][300];
int a[300];

int calc(int depth, int color) {
  if (memo[depth][color] != -1) { return memo[depth][color]; }
  if (depth == N) { return memo[depth][color] = 0; }
  int ret = 0x0f0f0f0f;
  ret = min(ret, calc(depth + 1, color) + D);
  FOREQ(i, 0, 255) {
    int cost = abs(a[depth] - i);
    int dif = abs(color - i);
    if (dif > M) { continue; }
    ret = min(ret, calc(depth + 1, i) + cost);
  }
  FOREQ(i, 0, 255) {
    int l = min(color, a[depth]);
    int r = max(color, a[depth]);
    int dif = abs(color - i);
    if (i <= l || r <= i || dif > M) { continue; }
    ret = min(ret, calc(depth, i) + I);
  }
  return memo[depth][color] = ret;
}

int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    MEMSET(a, 0);
    MEMSET(memo, -1);
    scanf("%d %d %d %d", &D, &I, &M, &N);
    REP(i, N) { scanf("%d", &a[i]); }
    int ans = 0x0f0f0f0f;
    FOREQ(i, 0, 255) {
      ans = min(ans, calc(0, i));
    }
    printf("Case #%d: %d\n", test_case, ans);
  }
}
