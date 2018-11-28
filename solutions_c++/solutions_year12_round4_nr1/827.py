#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 100010;
const int INF = 0x3f3f3f3f;

int tree[MAXN*4];
int n;
int D[MAXN], L[MAXN];
int Dist;

int ll, rr;

void init()
{
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) scanf("%d%d", D + i, L + i);
  scanf("%d", &Dist);
}

void ins(int x, int y, int h, int high)
{
  if (y < ll || rr < x) return;
  if (ll <= x && y <= rr) {
    tree[h] = min(tree[h], high);
    return;
  }

  int mid = (x+y) >> 1;
  ins(x, mid, 2*h+1, high);
  ins(mid+1, y, 2*h+2, high);
}

int cal(int x, int y, int h)
{
  if (y < ll || ll < x) return INF;
  if (x == y) return tree[h];

  int mid = (x+y) >> 1;
  int res = tree[h];
  res = min(res, cal(x, mid, 2*h+1));
  res = min(res, cal(mid+1, y, 2*h+2));
  return res;
}

int solve()
{
  memset(tree, 0x3f, sizeof(tree));

  ll = 0; rr = 0;
  ins(0, n-1, 0, 0);

  int len, d;
  for (int i = 0; i < n; ++i) {
    ll = i;
    d = cal(0, n-1, 0);
    if (d == INF) continue;

    len = min(D[i] - d, L[i]);

    if (len + D[i] >= Dist) return 1;

    ll = i;
    rr = upper_bound(D, D+n, D[i]+len) - D - 1;

    ins(0, n-1, 0, D[i]);
  }

  return 0;
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    init();
    printf("Case #%d: ", l);
    if (solve()) puts("YES"); else puts("NO");
  }
  return 0;
}
