#include <cstdio>
using namespace std;

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);

  int tc;
  scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {
    int n, k; 
    scanf("%d %d", &n, &k);
    printf("Case #%d: %s\n", tt, (k&((1<<n)-1)) == (1<<n)-1 ? "ON" : "OFF");
  }

  return 0;
}