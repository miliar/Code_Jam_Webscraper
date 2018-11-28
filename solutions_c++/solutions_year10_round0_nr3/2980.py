#include<iostream>
using namespace std;

const int MaxN = 1005;
int r, k, n;
int g[MaxN], p[MaxN];
long long ans;
long long a[MaxN];

void work()
{
  ans = 0;
  for (int i = 1; i <= n; ++i) {
    a[i] = 0; p[i] = 0; ans += g[i];
  }
  if (ans <= k) ans = ans*r;  
  else {
    ans = 0;
    int now = 1;
    while (p[now] == 0) {
      int i = now, j = 0;
      while (j+g[i] <= k) {
        j += g[i]; ++i;
        if (i > n) i = 1;
      }
      a[now] = j; p[now] = i;
      now = i; ans += j; --r;
      if (r == 0) break;
    }
    if (r != 0) {
      int i = p[now], j = 1;
      long long sum = a[now];
      while (i != now) {
        sum += a[i]; i = p[i]; ++j;
      }
      ans += sum*(r/j);
      r = r % j;
      while (r > 0) {
        ans += a[i]; --r; i = p[i];
      }
    }
  }
}

int main()
{
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("C-small.out", "w", stdout);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> r >> k >> n;
    for (int j = 1; j <= n; ++j) scanf("%d", &g[j]);
    work();
    printf("Case #%d: %d\n", i, ans); 
  }
  return 0;
}
