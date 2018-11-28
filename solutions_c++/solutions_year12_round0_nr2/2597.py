#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 100;

int res[MAXN+1][MAXN+1];
int N, S, p, tot[MAXN], tmp[2];
bool out[4]; // 0 = { < p, ns } 1 = { >= p, ns } 2 = { < p, s } 3 = { >= p, s }

void rec(int d, int prev, int left)
{
  if (d == 2) {
    if (left < tmp[0] || left - tmp[0] > 2) return;
    out[(left >= p) + 2*(left - tmp[0] == 2)] = true;
    return;
  }

  for (int c = prev; c <= 10; ++c) { tmp[d] = c; rec(d+1, c, left-c); }
}

void solve()
{
  memset(res, 0, sizeof(res));

  for (int i = 0; i < N; ++i) {
    memset(out, 0, sizeof(out));
    rec(0, 0, tot[i]);

    for (int s = 0; s <= S; ++s) {
      if (out[0]) res[i+1][s] = max(res[i+1][s], res[i][s]);
      if (out[1]) res[i+1][s] = max(res[i+1][s], res[i][s] + 1);
      if (out[2] && s < S) res[i+1][s+1] = max(res[i+1][s+1], res[i][s]);
      if (out[3] && s < S) res[i+1][s+1] = max(res[i+1][s+1], res[i][s]+1);
    }
  }

  printf("%d\n", res[N][S]);
}

int main()
{
  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    scanf("%d%d%d", &N, &S, &p);

    for (int i = 0; i < N; ++i) scanf("%d", &tot[i]);
    printf("Case #%d: ", t);
    solve();
  }
}
