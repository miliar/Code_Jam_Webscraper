#include <stdio.h>

#include <algorithm>

const int MAXN = 10000;

int t[MAXN], p[MAXN], id[MAXN];

int n;

bool IdCmp(int a, int b)
{
  if (t[a] * p[b] != t[b] * p[a])
  {
    return t[a] * p[b] < t[b] * p[a];
  }
  else
  {
    return a < b;
  }
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt)
  {
    scanf("%d", &n);
    for (int j = 0; j < n; ++j)
    {
      scanf("%d", t + j);
      id[j] = j;
    }
    for (int j = 0; j < n; ++j)
    {
      scanf("%d", p + j);
    }
    std::sort(id, id + n, IdCmp);
    printf("Case #%d:", tt);
    for (int i = 0; i < n; ++i) printf(" %d", id[i]);
    puts("");
  }
  return 0;
}
