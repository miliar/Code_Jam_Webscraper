#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int t, n, a[2000];

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout); 
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    scanf("%d", &n);
    int xxor = 0, sum = 0, minn = 1000000000;
    for (int j = 0; j < n; j++)
    {
      scanf("%d", &a[j]);
      xxor ^= a[j];
      sum += a[j];
      minn = min(minn, a[j]);
    }
    printf("Case #%d: ", i + 1);
    if (xxor != 0)
      printf("NO\n");
    else
      printf("%d\n", sum - minn);
  }
  return 0;
}

