#include <stdio.h>
#include <queue>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
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

ll l, n;
ull board[110];
ull memo[101][100000];

ull calc(int depth, ull rest) {
  if (rest < 100000 && memo[depth][rest] != (ull)-1) { return memo[depth][rest]; }
  if (depth == n) { return 1ULL << 63; }
  ull ret = 1ULL << 63;
  ull ini = rest % board[depth];
  ull plus = 0;
  REP(i, 110) {
    if (ini + plus * board[depth] > rest) { break; }
    ret = min(ret, calc(depth + 1, ini + plus * board[depth]) + rest / board[depth] - plus);
    plus++;
  }
  ret = min(ret, calc(depth + 1, rest));
  if (rest < 100000) { memo[depth][rest] = ret; }
  return ret;
}


int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    MEMSET(memo, -1);
    test_case++;
    scanf("%lld %lld", &l, &n);
    memo[n][0] = 0;
    REP(i, n) {
      scanf("%lld", &board[i]);
    }
    sort(board, board + n);
    reverse(board, board + n);
    ull ans = calc(0, l);
    if (ans != 1ULL << 63) {
      printf("Case #%d: %llu\n", test_case, ans);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", test_case);
    }
  }
}
