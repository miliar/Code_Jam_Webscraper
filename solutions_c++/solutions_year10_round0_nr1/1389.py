#include <cstdio>

using namespace std;

int T;

int main()
{
  //freopen("a.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    int n, k;
    scanf("%d %d", &n, &k);
    int s = 1 << n;
    if ((k & (s-1)) == s-1)
    	printf("Case #%d: ON\n", t + 1);
    else
        printf("Case #%d: OFF\n", t + 1);
  }
  return 0;
}