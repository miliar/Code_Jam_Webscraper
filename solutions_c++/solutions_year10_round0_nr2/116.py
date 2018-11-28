
#include <iostream>
#include <algorithm>

static int gcd2(int x ,int y)
{
  if (x > y) {
    int tmp = x;
    x       = y;
    y       = tmp;
  }

  while (x != 0) {
    int tmp = x;
    x = y % x;
    y = tmp;
  }
  return y;
}

static int gcdn(int* num, int n)
{ 
  int d = num[0];
  for (int i = 1; i < n; i++) {
     d = gcd2(d, num[i]);
  }
  return d;
}

static void solve(int t, int* num, int n)
{
  std::sort(num, num+n);

  int diff[1002];
  for (int i = 0; i < n - 1; i++) {
    diff[i] = num[i + 1] - num[i];
  }
  int maxd = gcdn(diff, n - 1);
  if (num[0] % maxd == 0)
    printf("Case #%d: %d\n", t, 0);
  else
    printf("Case #%d: %d\n", t, maxd - num[0] % maxd);
}

int main()
{ 
  int c;  
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &c);
  for (int i = 1; i <= c; i++) {
    int n;
    int num[1001];

    scanf("%d", &n);
    for (int k = 0; k < n; k++)
      scanf("%d", &num[k]);

    solve(i, num, n);
  }
  return 0;
}