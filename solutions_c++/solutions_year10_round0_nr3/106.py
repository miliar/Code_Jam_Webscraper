#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>

using namespace std;
typedef long long ll;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define DEC(i, s) for (int i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())

ll r, k, n;
ll g[10100];
ll loop[10100];
ll loop_time[10100];
bool visit[10100];

int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    memset(visit, false, sizeof(visit));
    test_case++;
    scanf("%lld %lld %lld", &r, &k, &n);
    REP(i, n) {
      scanf("%lld", &g[i]);
    }
    ll ans = 0;
    int index = 0;
    bool loop_check = false;
    for (int i = 0; i < r; i++) {
      ll board = 0;
      if (!loop_check && visit[index]) {
        ll rest = r - i;
        ll l = i - loop_time[index];
        ll loop_board = ans - loop[index];
        ll use = (rest / l) * l;
        //cout << rest << " " << l << " " << loop_board << " " << use << endl;
        ans += (use / l) * loop_board;
        loop_check = true;
        i += use;
        i--;
        continue;
      }
      int start = index;
      visit[index] = true;
      loop[index] = ans;
      loop_time[index] = i;
      while (board + g[index] <= k) {
        board += g[index];
        index = (index + 1) % n;
        if (start == index) { break; }
      }
      ans += board;
    }
    printf("Case #%d: %lld\n", test_case, ans);
  }
}
