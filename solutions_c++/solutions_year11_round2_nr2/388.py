#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>

#define fi first
#define se second

using namespace std;

typedef long long ll;

pair<long long, int> p[300];
int n;
long long d;

bool check(long long res)
{
  ll lastPos = p[0].fi - res - d;

//  printf("==== %d %lld\n", res, lastPos);
  for (int i = 0; i < n; i++)
  {
    lastPos = max(lastPos + d, p[i].fi - res) + d * (p[i].se - 1);
//    printf("%lld %lld %lld\n", lastPos, p[i].fi, res);
    if (lastPos > p[i].fi + res) return false;
  }
//  printf("!\n");
  return true;
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    long long right = 0;
    long long left = 0;

    scanf("%d %lld", &n, &d);
    d *= 2;
    for (int j = 0; j < n; j++)
    {
      int aa, bb;
      scanf("%d %d", &aa, &bb);
      aa *= 2;
      p[j] = make_pair(aa, bb);
      right += bb;
    }
    right *= d;
    while (left < right)
    {
//      printf("%lld %lld\n", left, right);
      long long mid = (left + right) / 2;
      if (check(mid)) right = mid - 1;
      else left = mid + 1;
    }
    for (long long j = max(0ll, left-3); j <= left + 3; j++)
//    for (int j = left; j <= right; j++)
      if (check(j))
      {
        printf("Case #%d: %lf\n", i+1, j / (double)2.0);
        break;
      }
  }
  return 0;
}
