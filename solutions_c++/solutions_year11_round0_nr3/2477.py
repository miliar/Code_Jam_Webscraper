#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

const int INF = 1000000000;

int main()
{
  int t, n;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++)
  {
    scanf("%d", &n);
    int sum = 0, xorall = 0, min = INF;
    for (int i = 0; i < n; i++)
    {
      int k;
      scanf("%d", &k);
      sum += k;
      xorall ^= k;
      min = (k < min ? k : min);
    }
    if (xorall)
      printf("Case #%d: NO\n", test);
    else
      printf("Case #%d: %d\n", test, sum - min);
  }
  return 0;
}
