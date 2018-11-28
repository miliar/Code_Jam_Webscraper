// For my Garfield
// 41 days to our 3 years
// B. Fair Warning
// Google Code Jam Qualification Round 2010
#include <cstdio>
#include <algorithm>
using namespace std;
int T, N;
long long a[1000];
long long gcd(long long a, long long b)
{
  return (b == 0)? a: gcd(b, a % b);
}
int main()
{
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("B-small-attempt0.out", "w", stdout);
  scanf("%d", &T);
  for(int t = 1; t <= T; ++ t)
  {
    scanf("%d", &N);
    for(int i = 0; i < N; ++ i)
      scanf("%lld", &a[i]);
    sort(a, a + N);
    long long d = a[1] - a[0];
    for(int i = 2; i < N; ++ i)
      d = gcd(d, a[i] - a[i - 1]);    
    printf("Case #%d: %lld\n", t, (a[0] % d == 0)? 0: d - a[0] % d);
  }
  return 0;
}
